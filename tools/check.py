#!/usr/bin/env python3
"""Checks the ontology, its lists, glossary, shapes, fixtures and tests.

    pip install rdflib owlrl pyshacl
    python3 tools/check.py            # run every check
    python3 tools/check.py --update   # rewrite tests/expected/ from the current results

Exits 1 on an error. Run from the repo root.
"""
import collections
import glob
import os
import re
import subprocess
import sys

import owlrl
from pyshacl import validate
from rdflib import OWL, RDF, RDFS, Graph, Literal, Namespace, URIRef
from rdflib.collection import Collection

AO = Namespace("http://actuarialnotes.com/ontology/actuarial#")
PREFIXES = {
    str(AO): "ao:",
    "http://actuarialnotes.com/ontology/actuarial/glossary#": "aog:",
    "http://actuarialnotes.com/data/synthetic/": "syn:",
    "http://actuarialnotes.com/data/": "an:",
}
MODULES = sorted(glob.glob("ontology/*.ttl"))
LISTS = sorted(glob.glob("lists/*.ttl"))
VOCABULARY = sorted(glob.glob("vocabulary/*.ttl"))
FIXTURES = sorted(glob.glob("tests/fixtures/*.ttl"))
QUERIES = sorted(glob.glob("tests/queries/*.rq"))
UPDATE = "--update" in sys.argv

errors = []


def name(term):
    s = str(term)
    for ns, prefix in PREFIXES.items():
        if s.startswith(ns):
            return prefix + s[len(ns):]
    return s


def load(paths):
    g = Graph()
    for path in paths:
        g.parse(path)
    return g


onto = load(MODULES)
lists = load(LISTS)
schema = onto + lists
classes = set(onto.subjects(RDF.type, OWL.Class))
properties = set()
for kind in (OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty):
    properties |= set(onto.subjects(RDF.type, kind))
listed = {s for s in lists.subjects() if isinstance(s, URIRef)}
declared = classes | properties | listed

# 1. Every ao: term used anywhere is declared.
for path in MODULES + LISTS + VOCABULARY + FIXTURES:
    g = Graph().parse(path)
    used = {x for t in g for x in t if isinstance(x, URIRef) and str(x).startswith(str(AO))}
    for term in sorted(used - declared):
        errors.append(f"{path}: {name(term)} is used but not declared")

# 2. Every class and property has exactly one label and one definition.
for term in sorted(classes | properties):
    for prop, what in ((RDFS.label, "label"), (RDFS.comment, "definition")):
        count = len(list(onto.objects(term, prop)))
        if count != 1:
            errors.append(f"{name(term)} has {count} {what}s")

# 3. No two classes or properties share a label.
labels = collections.defaultdict(list)
for term in classes | properties:
    for label in onto.objects(term, RDFS.label):
        labels[str(label).lower()].append(name(term))
for label, terms in sorted(labels.items()):
    if len(terms) > 1:
        errors.append(f"label '{label}' is shared by {sorted(terms)}")

# 4. No cycle in the class hierarchy.
parents = collections.defaultdict(set)
for child, parent in onto.subject_objects(RDFS.subClassOf):
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
        errors.append(f"{name(cls)} is its own ancestor")

# 5. Every property has a range, or says in its definition what it relates.
for prop in sorted(properties - set(onto.subjects(RDF.type, OWL.AnnotationProperty))):
    if not list(onto.objects(prop, RDFS.range)) and not list(onto.objects(prop, RDFS.domain)):
        errors.append(f"{name(prop)} has neither a domain nor a range")

# 6. The fixtures and the glossary conform to the shapes.
shapes = load(["shapes/shapes.ttl"])
data = load(LISTS + VOCABULARY + FIXTURES)
conforms, _, report = validate(data, shacl_graph=shapes, ont_graph=onto, inference="rdfs")
if not conforms:
    for block in report.split("Constraint Violation")[1:]:
        focus = re.search(r"Focus Node: (\S+)", block)
        message = re.search(r"Message: (.+)", block)
        path = re.search(r"Result Path: (\S+)", block)
        errors.append("shape: %s %s: %s" % (focus and focus.group(1), path.group(1) if path else "",
                                             message.group(1) if message else "does not conform"))

# 7. Nothing is an instance of two disjoint classes, after OWL 2 RL inference.
everything = load(MODULES + LISTS + FIXTURES)
closure = Graph()
for t in everything:
    closure.add(t)
owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(closure)
pairs = set(onto.subject_objects(OWL.disjointWith))
for node in onto.subjects(RDF.type, OWL.AllDisjointClasses):
    members = list(Collection(onto, onto.value(node, OWL.members)))
    pairs |= {(a, b) for i, a in enumerate(members) for b in members[i + 1:]}
for a, b in sorted(pairs):
    for ind in sorted(set(closure.subjects(RDF.type, a))):
        if isinstance(ind, URIRef) and (ind, RDF.type, b) in closure:
            errors.append(f"{name(ind)} is both {name(a)} and {name(b)}, which are disjoint")

# 8. Each competency question's query returns its expected result.
world = load(MODULES + LISTS + VOCABULARY + FIXTURES)


def cell(value):
    if value is None:
        return ""
    return name(value) if isinstance(value, URIRef) else str(value)


query_terms = set()
passed = 0
for path in QUERIES:
    qid = os.path.basename(path)[:-3]
    text = open(path, encoding="utf8").read()
    query_terms |= {AO[m] for m in re.findall(r"\bao:([A-Za-z][\w-]*)", text)}
    try:
        result = world.query(text)
    except Exception as exc:  # a query that does not parse is a failed test
        errors.append(f"{qid}: query does not run: {str(exc)[:120]}")
        continue
    if result.type == "ASK":
        got = "true" if result.askAnswer else "false"
    else:
        rows = ["\t".join(cell(v) for v in row) for row in result]
        if "ORDER BY" not in text:
            rows.sort()
        got = "\n".join(["\t".join(str(v) for v in result.vars)] + rows)
    expected_path = f"tests/expected/{qid}.txt"
    if UPDATE:
        open(expected_path, "w", encoding="utf8").write(got + "\n")
    if not os.path.exists(expected_path):
        errors.append(f"{qid}: no expected result")
        continue
    expected = open(expected_path, encoding="utf8").read().strip("\n")
    query_terms |= {AO[m] for m in re.findall(r"\bao:([A-Za-z][\w-]*)", expected)}
    if got != expected:
        errors.append(f"{qid}: result differs from tests/expected/{qid}.txt")
    elif result.type != "ASK" and len(got.splitlines()) < 2:
        errors.append(f"{qid}: query returns no rows")
    else:
        passed += 1

# 9. Presuppositions: every ao: term a query names exists.
for term in sorted(query_terms - declared):
    errors.append(f"a query names {name(term)}, which is not declared")

# 10. Coverage: every class and property is needed by some question.
covered = set(query_terms)
for prop in properties & query_terms:
    covered |= set(onto.objects(prop, RDFS.domain)) | set(onto.objects(prop, RDFS.range))
changed = True
while changed:  # a class is covered if a subclass of it is
    changed = False
    for child, parent in onto.subject_objects(RDFS.subClassOf):
        if child in covered and parent not in covered:
            covered.add(parent)
            changed = True
for term in sorted((classes | properties) - covered):
    errors.append(f"{name(term)} is used by no competency question")

# 11. lists/lists.json, the form the wiki reads, is current with lists/*.ttl.
export = subprocess.run([sys.executable, "tools/export_lists.py", "--check"], capture_output=True, text=True)
for line in export.stdout.splitlines():
    if line.startswith("ERROR: "):
        errors.append(line[len("ERROR: "):])

questions = {os.path.basename(p)[:-3].split("-")[0] for p in QUERIES}
print(f"{len(classes)} classes, {len(properties)} properties, {len(listed)} listed individuals, "
      f"{len(set(load(VOCABULARY).subjects(RDF.type, URIRef('http://www.w3.org/2004/02/skos/core#Concept'))))} glossary terms")
print(f"{passed} of {len(QUERIES)} tests pass, covering {len(questions)} questions")
for e in errors:
    print("ERROR:", e)
print("FAILED" if errors else "ok")
sys.exit(1 if errors else 0)
