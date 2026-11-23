import sys, collections
from rdflib import Graph, RDF, RDFS, OWL, Namespace, URIRef, Literal
AO="http://actuarialnotes.com/ontology/actuarial#"
o=Graph(); o.parse("actuarial-ontology.ttl")
decl=set(o.subjects(RDF.type,OWL.Class))|set(o.subjects(RDF.type,OWL.ObjectProperty))|set(o.subjects(RDF.type,OWL.DatatypeProperty))|set(o.subjects(RDF.type,OWL.AnnotationProperty))
for f in sys.argv[1:]:
    g=Graph()
    try: g.parse(f)
    except Exception as e: print(f,"PARSE ERROR",str(e)[:300]); continue
    n=lambda u: g.namespace_manager.normalizeUri(u)
    print("==",f,"triples",len(g)); print("namespaces",[(p,str(u)) for p,u in g.namespaces() if p not in('xml','rdf','rdfs','xsd','owl','brick','csvw','dc','dcat','dcmitype','dcam','doap','foaf','geo','odrl','org','prof','prov','qb','schema','sh','skos','sosa','ssn','time','vann','void','wgs')])
    types=collections.Counter(n(t) for t in g.objects(None,RDF.type)); print("types",types.most_common())
    preds=collections.Counter(n(p) for p in g.predicates()); print("preds",preds.most_common())
    usedao={x for t in g for x in t if isinstance(x,URIRef) and str(x).startswith(AO)}
    print("AO terms used but NOT declared in ontology:",sorted(n(x) for x in usedao-decl))
    localcls=[n(s) for s in g.subjects(RDF.type,OWL.Class)]; print("classes declared in KB:",len(localcls),localcls[:80])
    localp=[n(s) for s in g.subjects(RDF.type,OWL.ObjectProperty)]+[n(s) for s in g.subjects(RDF.type,OWL.DatatypeProperty)]; print("props declared in KB:",len(localp),localp)
    subj=set(g.subjects()); print("subjects",len(subj))
