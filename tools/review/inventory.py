import sys, re, collections
from rdflib import Graph, RDF, RDFS, OWL, Namespace, URIRef, Literal, BNode
AO=Namespace("http://actuarialnotes.com/ontology/actuarial#")
g=Graph(); g.parse("actuarial-ontology.ttl")
print("triples",len(g))
C=set(g.subjects(RDF.type,OWL.Class)); OP=set(g.subjects(RDF.type,OWL.ObjectProperty)); DP=set(g.subjects(RDF.type,OWL.DatatypeProperty)); AP=set(g.subjects(RDF.type,OWL.AnnotationProperty))
n=lambda u: g.namespace_manager.normalizeUri(u) if isinstance(u,URIRef) else str(u)
print("classes",len(C),"objprops",len(OP),"dataprops",len(DP),"annprops",len(AP))
# undeclared references
used=set()
for s,p,o in g:
    for x in (s,o):
        if isinstance(x,URIRef) and str(x).startswith(str(AO)): used.add(x)
undecl=used-C-OP-DP-AP
print("UNDECLARED ao terms referenced:",sorted(n(x) for x in undecl))
par=collections.defaultdict(set); ch=collections.defaultdict(set)
for s,o in g.subject_objects(RDFS.subClassOf):
    if isinstance(o,URIRef): par[s].add(o); ch[o].add(s)
    else: print("restriction on",n(s))
roots=[c for c in C if not par[c]]
print("ROOTS",len(roots),sorted(n(x) for x in roots))
multi=[(n(c),[n(p) for p in par[c]]) for c in C if len(par[c])>1]
print("MULTI-PARENT",len(multi),multi)
def depth(c,seen=()):
    if c in seen: return 99
    return 0 if not par[c] else 1+max(depth(p,seen+(c,)) for p in par[c])
d=collections.Counter(depth(c) for c in C); print("depth dist",sorted(d.items()))
one=[(n(c),n(list(ch[c])[0])) for c in C if len(ch[c])==1]; print("ONE-CHILD",len(one),one)
big=[(n(c),len(ch[c])) for c in C if len(ch[c])>12]; print(">12 children",big)
leaf=[c for c in C if not ch[c]]; print("leaves",len(leaf))
print("fanout top",sorted(((len(ch[c]),n(c)) for c in C),reverse=True)[:25])
# annotations
nolabel=[n(x) for x in C|OP|DP if not list(g.objects(x,RDFS.label))]
nocomment=[n(x) for x in C|OP|DP if not list(g.objects(x,RDFS.comment))]
print("no label",nolabel,"no comment",nocomment)
gd=0; bad=[]
for c in C:
    com=str(next(g.objects(c,RDFS.comment),""))
    ps=[str(next(g.objects(p,RDFS.label),"")) for p in par[c]]
    if re.match(r"^(An?|The) ",com) and any(pl.lower() in com.lower() for pl in ps if pl): gd+=1
    else: bad.append(n(c))
print("classes whose comment mentions parent label (genus-differentia proxy):",gd,"of",len(C))
print("predicates used:",collections.Counter(n(p) for s,p,o in g).most_common())
print("asopReference count",len(list(g.subject_objects(AO.asopReference))))
print("rigidity",collections.Counter(str(o) for o in g.objects(None,AO.rigidity)),"ufoCat",collections.Counter(str(o) for o in g.objects(None,AO.ufoCategory)))
# roles under kinds etc
# properties
for P,name in ((OP,"OP"),(DP,"DP")):
    nod=[n(p) for p in P if not list(g.objects(p,RDFS.domain))]; nor=[n(p) for p in P if not list(g.objects(p,RDFS.range))]
    md=[n(p) for p in P if len(list(g.objects(p,RDFS.domain)))>1]; mr=[n(p) for p in P if len(list(g.objects(p,RDFS.range)))>1]
    print(name,"no domain",nod,"no range",nor,"multi-domain",md,"multi-range",mr)
print("inverseOf",[(n(s),n(o)) for s,o in g.subject_objects(OWL.inverseOf)])
print("subPropertyOf",[(n(s),n(o)) for s,o in g.subject_objects(RDFS.subPropertyOf)])
print("disjoint",[(n(s),n(o)) for s,o in g.subject_objects(OWL.disjointWith)])
for t in (OWL.FunctionalProperty,OWL.TransitiveProperty,OWL.SymmetricProperty,OWL.Restriction,OWL.AllDisjointClasses): print(n(t),len(list(g.subjects(RDF.type,t))))
print("DP ranges",collections.Counter(n(o) for p in DP for o in g.objects(p,RDFS.range)))
print("OP domain counter",collections.Counter(n(o) for p in OP for o in g.objects(p,RDFS.domain)).most_common(15))
# naming
print("class names not UpperCamel",[n(c) for c in C if not re.match(r"^[A-Z][A-Za-z0-9]*$",str(c).split('#')[1])])
print("prop names not lowerCamel",[n(c) for c in OP|DP if not re.match(r"^[a-z][A-Za-z0-9]*$",str(c).split('#')[1])])
print("plural-looking classes",[n(c) for c in C if str(c).endswith('s') and not str(c).endswith('ss') and not str(c).endswith('sis')])
print("OP names not verb-ish(has/is/..)",[n(p) for p in OP if not re.match(r"^(has|is|[a-z]+s[A-Z]|[a-z]+s$|[a-z]+edBy|[a-z]+To|[a-z]+edTo|[a-z]+On|[a-z]+In)",str(p).split('#')[1])])
# classes never used in any domain/range and leaf
dr=set(g.objects(None,RDFS.domain))|set(g.objects(None,RDFS.range))
def anc(c,acc=None):
    acc=acc or set()
    for p in par[c]:
        if p not in acc: acc.add(p); anc(p,acc)
    return acc
untouched=[n(c) for c in C if c not in dr and not (anc(c)&dr)]
print("classes with no property reaching them (even inherited):",len(untouched),untouched)
direct=[c for c in C if c in dr]; print("classes directly in a domain/range:",len(direct))
# label duplicates
lab=collections.defaultdict(list)
for x in C|OP|DP:
    for l in g.objects(x,RDFS.label): lab[str(l).lower()].append(n(x))
print("dup labels",{k:v for k,v in lab.items() if len(v)>1})
# tree dump
def dump(c,i=0,seen=()):
    print("  "*i+str(c).split('#')[1]+("" if c not in seen else " (again)"))
    if c in seen: return
    for k in sorted(ch[c]): dump(k,i+1,seen+(c,))
if "--tree" in sys.argv:
    for r in sorted(roots): dump(r)
