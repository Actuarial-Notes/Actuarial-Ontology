import collections
from rdflib import Graph, RDF, RDFS, OWL, URIRef, Literal, Namespace
AO=Namespace("http://actuarialnotes.com/ontology/actuarial#")
o=Graph(); o.parse("actuarial-ontology.ttl"); kb=Graph(); kb.parse("canadian-pc-insurance-knowledge-base-improved.ttl")
OP=set(o.subjects(RDF.type,OWL.ObjectProperty))
linked=set()
for s,p,x in kb:
    if p in OP: linked|={s,x}
subs=set(kb.subjects(RDF.type,None))
orph=collections.Counter(); ex={}
for s in subs-linked:
    for t in kb.objects(s,RDF.type): orph[t.split('#')[1]]+=1; ex[t.split('#')[1]]=s.split('/')[-1]
print("individuals with NO object-property link at all:",len(subs-linked),"of",len(subs)); print(dict(orph)); print(ex)
mis=collections.Counter()
for s,p,x in kb:
    if isinstance(x,Literal):
        for r in o.objects(p,RDFS.range):
            if x.datatype!=r: mis[(p.split('#')[1],str(x.datatype).split('#')[-1],r.split('#')[1])]+=1
print("datatype mismatches",dict(mis))
usedC={t for t in kb.objects(None,RDF.type)}; usedP={p for p in kb.predicates() if str(p).startswith(str(AO))}
C=set(o.subjects(RDF.type,OWL.Class)); DP=set(o.subjects(RDF.type,OWL.DatatypeProperty))
print("ontology classes instantiated in KB:",len(usedC&C),"of",len(C),"| props used:",len(usedP&(OP|DP)),"of",len(OP|DP))
