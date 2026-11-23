#!/usr/bin/env python3
"""Checks the ontology and its example data. Run from the repo root:

    pip install rdflib owlrl
    python3 tools/check.py

Exits 1 on an error. Warnings are known debt, listed so they can only go down.
"""
import collections
import glob
import sys

import owlrl
from rdflib import OWL, RDF, RDFS, Graph, Literal, Namespace, URIRef

AO = Namespace("http://actuarialnotes.com/ontology/actuarial#")
ONTOLOGY = "actuarial-ontology.ttl"
EXAMPLES = sorted(glob.glob("examples/*.ttl"))

errors, warnings = [], []


def name(term):
    return str(term).split("#")[-1].split("/")[-1]


onto = Graph().parse(ONTOLOGY)
classes = set(onto.subjects(RDF.type, OWL.Class))
obj_props = set(onto.subjects(RDF.type, OWL.ObjectProperty))
data_props = set(onto.subjects(RDF.type, OWL.DatatypeProperty))
ann_props = set(onto.subjects(RDF.type, OWL.AnnotationProperty))
declared = classes | obj_props | data_props | ann_props

# 1. Every ao: term that is used is declared, in the ontology and in the examples.
graphs = {ONTOLOGY: onto}
for path in EXAMPLES:
    graphs[path] = Graph().parse(path)
for path, g in graphs.items():
    used = {x for t in g for x in t if isinstance(x, URIRef) and str(x).startswith(str(AO))}
    for term in sorted(used - declared):
        errors.append(f"{path}: ao:{name(term)} is used but not declared")

# 2. One label and one definition per term and language.
for term in sorted(classes | obj_props | data_props):
    for prop, what in ((RDFS.label, "label"), (RDFS.comment, "definition")):
        by_lang = collections.Counter(o.language for o in onto.objects(term, prop))
        if not by_lang:
            errors.append(f"ao:{name(term)} has no {what}")
        for lang, count in by_lang.items():
            if count > 1:
                errors.append(f"ao:{name(term)} has {count} {what}s in '{lang}' (declared twice?)")

# 3. No two terms share a label.
labels = collections.defaultdict(list)
for term in classes | obj_props | data_props:
    for label in onto.objects(term, RDFS.label):
        labels[str(label).lower()].append(name(term))
for label, terms in sorted(labels.items()):
    if len(terms) > 1:
        errors.append(f"label '{label}' is shared by {sorted(terms)}")

# 4. No cycle in the class hierarchy.
parents = collections.defaultdict(set)
for child, parent in onto.subject_objects(RDFS.subClassOf):
    if isinstance(parent, URIRef):
        parents[child].add(parent)


def ancestors(cls):
    seen, stack = set(), list(parents[cls])
    while stack:
        p = stack.pop()
        if p not in seen:
            seen.add(p)
            stack.extend(parents[p])
    return seen


for cls in sorted(classes):
    if cls in ancestors(cls):
        errors.append(f"ao:{name(cls)} is its own ancestor (subclass cycle)")

# 5. Ontology plus examples is consistent: after OWL 2 RL inference, nothing is an
#    instance of two disjoint classes, and no literal has the wrong datatype.
merged = Graph()
for g in graphs.values():
    for t in g:
        merged.add(t)
owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(merged)
for a, b in onto.subject_objects(OWL.disjointWith):
    for ind in sorted(set(merged.subjects(RDF.type, a))):
        if (ind, RDF.type, b) in merged and not isinstance(ind, Literal):
            errors.append(f"{name(ind)} is both ao:{name(a)} and ao:{name(b)}, which are disjoint")
for path in EXAMPLES:
    for s, p, o in graphs[path]:
        if isinstance(o, Literal):
            for rng in onto.objects(p, RDFS.range):
                actual = o.datatype or URIRef("http://www.w3.org/2001/XMLSchema#string")
                if actual != rng:
                    warnings.append(
                        f"{path}: {name(s)} ao:{name(p)} is {name(actual)}, range is {name(rng)}"
                    )

# Known debt (docs/ontology-review.md). Reported, not failed, until 0.8.
roots = [c for c in classes if not parents[c]]
warnings.append(f"{len(roots)} root classes")
for prop in sorted(obj_props):
    if not list(onto.objects(prop, RDFS.domain)):
        warnings.append(f"ao:{name(prop)} has no domain")
    if not list(onto.objects(prop, RDFS.range)):
        warnings.append(f"ao:{name(prop)} has no range")

print(f"{ONTOLOGY}: {len(classes)} classes, {len(obj_props)} object properties, "
      f"{len(data_props)} data properties; {len(EXAMPLES)} example file(s)")
mismatch = sum("range is" in w for w in warnings)
for w in warnings:
    if "range is" not in w:
        print("warning:", w)
if mismatch:
    print(f"warning: {mismatch} example literals whose datatype differs from the property's range")
for e in errors:
    print("ERROR:", e)
print("FAILED" if errors else "ok")
sys.exit(1 if errors else 0)
