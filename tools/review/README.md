# Review scripts

The scripts behind the numbers in `docs/ontology-review.md`. Run from the repo root with
`pip install rdflib owlrl`.

- `inventory.py [--tree]`: counts, roots, cycles, fan-out, missing domains, ranges and inverses,
  naming, classes no property reaches.
- `competency_queries.py`: runs the SPARQL in `AO-Testing-Report.md` against the ontology plus
  the improved knowledge base, then an OWL-RL closure and the type inferences it produces.
- `kb_terms.py <file.ttl>…`: which ontology terms a knowledge-base file uses.
- `kb_links.py`: unlinked individuals and datatype mismatches in the improved knowledge base.

They are review tools, written quickly. The CI checks proposed in the review should replace them.
