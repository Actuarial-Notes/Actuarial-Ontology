# Changelog

## 0.8.0 (2026-11-23)

A rebuild. The ontology is now a small core that answers a tested set of competency questions,
and the 0.7 class tree is a glossary.

- **Replaced:** `actuarial-ontology.ttl` (303 classes, 110 properties) with five modules in
  `ontology/`: 38 classes and 59 properties, each needed by a priority 1 question in
  `docs/competency-questions.md`. Every 0.7 IRI is retired; 0.7 was a draft and nothing depended
  on it.
- **Added:** three patterns in place of the old class tree: every number is an observation with
  its source; a role is a dated relationship, not a type; a document has editions, and a fact
  points at a place in one. See `docs/model.md`.
- **Added:** `lists/`, the controlled lists (jurisdictions, lines of business, role types,
  quantity kinds, units, statuses, perils), carrying the wiki's own spellings as notations.
- **Added:** `vocabulary/`, the glossary in SKOS: 286 terms carried over from 0.7 with their
  draft definitions, and 20 hand-written ones, including one term per sense of "claim", "loss",
  "policy" and "risk".
- **Added:** `shapes/shapes.ttl`, SHACL shapes for every record type.
- **Added:** `tests/`: 55 queries for the 52 priority 1 questions, with expected results, on a
  fixture transcribed from sourced pages of the Actuarial Notes Wiki, a fixture generated from its
  calculators, and a small synthetic one.
- **Changed:** `tools/check.py` now also validates the fixtures against the shapes, runs every
  query, and fails on a term no question uses.
- **Removed:** `examples/canadian-pc-example.ttl`.

## 0.7.1 (2026-11-23)

A repair release after the foundations review (`docs/ontology-review.md`). No new terms beyond
the rename below.

- **Fixed:** `ao:Agent` was declared twice, as the top-level category and as "Insurance Agent"
  under `Person`. The second is now `ao:InsuranceAgent`. The duplicate made `Agent` and `Person`
  equivalent, so every organization was inferred to be a person. `CaptiveAgent`,
  `IndependentAgent` and `ManagingGeneralAgent` are now under `InsuranceAgent`, and
  `representsInsurer` has it as its domain.
- **Fixed:** the example data was inconsistent with the ontology (a peer review typed as both an
  activity and a communication).
- **Added:** `tools/check.py` and a CI workflow: undeclared terms, duplicate declarations and
  labels, subclass cycles, and disjointness after OWL 2 RL inference.
- **Added:** `docs/competency-questions.md`, the requirements and draft competency questions
  (87, typed and prioritized, in seven modules) that 0.8 will be built to.
- **Removed:** the original Canadian P&C knowledge base, which used a different namespace and
  never referenced the ontology. The second one is now `examples/canadian-pc-example.ttl`,
  marked as unsourced example data.
- **Removed:** `AO-Documentation.md`, `AO-Testing-Report.md` and
  `PC-Knowledge-Base-Testing-Report.md`. Their term lists duplicated the Turtle file and had
  drifted from it, and the reported "100% competency-question answerability" was a vocabulary
  check, not a test result.

## 0.1.0 to 0.7.0 (2026-01-10 to 2026-01-12)

Drafts. 0.2 added the UFO and COVER alignment; 0.3 to 0.5 added risk assessment (ASOP 51), data
quality (ASOP 23), credibility (ASOP 25), model governance (ASOP 56), communications (ASOP 41),
catastrophe modelling (ASOP 38 and 39) and the regulatory classes; 0.6 added `hasMetric` and
`hasSubject`; 0.7.0 added 126 classes across underwriting, reinsurance, distribution, claims,
policyholder behaviour, asset-liability management, life products, rating, emerging risks,
portfolios, stochastic modelling, embedded value and experience studies. The full notes are in
the git history of `AO-Documentation.md`.
