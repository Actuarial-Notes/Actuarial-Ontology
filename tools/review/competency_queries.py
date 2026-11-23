import re, collections
from rdflib import Graph, RDF, RDFS, OWL, URIRef, Namespace
import owlrl
AO=Namespace("http://actuarialnotes.com/ontology/actuarial#")
txt=open("AO-Testing-Report.md").read()
# split by question headings
secs=re.split(r"\n### (Q\d+: [^\n]+)\n",txt)
o=Graph(); o.parse("actuarial-ontology.ttl")
kb=Graph(); kb.parse("canadian-pc-insurance-knowledge-base-improved.ttl")
raw=o+kb
inf=Graph(); 
for t in raw: inf.add(t)
owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(inf)
print("raw",len(raw),"inferred",len(inf))
PFX="PREFIX ao: <http://actuarialnotes.com/ontology/actuarial#> PREFIX kb: <http://example.org/knowledge-base/> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX owl: <http://www.w3.org/2002/07/owl#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n"
for i in range(1,len(secs),2):
    title=secs[i]; body=secs[i+1]
    qs=re.findall(r"```sparql\n(.*?)```",body,re.S)
    for k,q in enumerate(qs):
        q2=re.sub(r"(?im)^\s*PREFIX[^\n]*\n","",q)
        binds=re.findall(r"(?:ex|kb|:)\w+|<[^>]+>",q2)
        res=[]
        for name,G in (("raw",raw),("inf",inf)):
            try:
                r=G.query(PFX+q2); n=(r.askAnswer if r.type=="ASK" else len(list(r)))
            except Exception as e: n="ERR "+str(e)[:80]
            res.append(f"{name}={n}")
        ph=re.findall(r"\?\w+|:\w+|ex:\w+",q2)
        print(title[:60],"| query",k+1,"|",", ".join(res),"| placeholders:",sorted(set(re.findall(r"(?<![\w?])(?:ex|kb|):\w+",q2)))[:5])
# consistency-ish checks on inferred graph
def types(G,x): return set(G.objects(x,RDF.type))
bad=[(s) for s in set(inf.subjects(RDF.type,AO.Person)) if (s,RDF.type,AO.Organization) in inf and str(s).startswith("http://example.org")]
print("individuals inferred BOTH Person and Organization:",len(bad),[str(b).split('/')[-1] for b in bad][:8])
for a,b in ((AO.Object,AO.Agent),(AO.Endurant,AO.Perdurant)):
    x=[s for s in set(inf.subjects(RDF.type,a)) if (s,RDF.type,b) in inf]; print("disjoint violation",a.split('#')[1],b.split('#')[1],len(x),[str(i).split('/')[-1] for i in x][:10])
print("Organization subClassOf Person inferred:",(AO.Organization,RDFS.subClassOf,AO.Person) in inf, "| Insurer equivalent/ sub Person:",(AO.Insurer,RDFS.subClassOf,AO.Person) in inf)
# surprising inferred types for KB individuals: asserted types vs new inferred named types not ancestors
par=collections.defaultdict(set)
for s,p in o.subject_objects(RDFS.subClassOf): par[s].add(p)
def anc(c,acc):
    for p in par[c]:
        if p not in acc: acc.add(p); anc(p,acc)
    return acc
sur=collections.Counter()
ex={}
for s in set(kb.subjects(RDF.type,None)):
    a=types(kb,s); exp=set(a)
    for c in a: anc(c,exp)
    # remove the cycle artefact
    new={t for t in types(inf,s) if str(t).startswith(str(AO))}-exp
    for t in new:
        key=(tuple(sorted(x.split('#')[1] for x in a))[:2],t.split('#')[1]); sur[key]+=1; ex[key]=str(s).split('/')[-1]
print("TYPE INFERENCES from domain/range not implied by asserted types (asserted -> inferred, count, example):")
for k,v in sur.most_common(60): print("  ",k,v,ex[k])
