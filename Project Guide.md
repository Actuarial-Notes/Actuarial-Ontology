# 📕 Project Guide
How the Actuarial Ontology is developed. It replaces the earlier guide and applies from 0.7.1.

1. Purpose and scope
2. Rules for the model
3. Rules for terms
4. Process
5. Software
6. Sources


## 1. Purpose and scope
The ontology is the schema for the data the Actuarial Coworker agent works with: regulations,
institutions, published figures, events, policies and actuarial work. The first scope is Canadian
property and casualty insurance.

- The scope is written as **competency questions** in
  [docs/competency-questions.md](docs/competency-questions.md). A class or property belongs in
  the core only if a question needs it.
- Instances live in the [Actuarial Notes Wiki](https://github.com/ActuarialNotes/Actuarial-Notes-Wiki),
  as sourced markdown pages. This repo holds the schema and small test fixtures, not a knowledge
  base.
- Terms that only need a definition (no question asks about their instances) belong in a
  glossary, not in the class tree.


## 2. Rules for the model
**Model the domain, not the sources.**
- A type is a real-world thing: a policy, a guideline, an insurer, an event. Not a document
  section, a table or a standard's chapter.
- Separate identity from observation. A loss ratio is a dated, sourced observation *about* an
  insurer, not a property of it.
- Every figure carries its period, unit, source and the date it was true.
- A particular thing is an instance (IFRS 17, the 2024 MCT guideline), never a class.

**Hierarchy.**
- Every subclass is a true "is a": everything said of the parent holds for the child.
- No cycles, and no two classes for the same thing.
- A class with one child, or more than a dozen, is a sign of a missing or unneeded level.
- A status (paid, in force) or a value on a scale (full, partial) is a property, not a subclass.
- A role (insurer, policyholder, regulator) is a dated relationship, not a permanent type.
- Prefer composition to depth.

**Properties.**
- Every property has a domain, a range and a cardinality, and sits on the most general class
  that has it.
- Declare the inverse of any relationship read in both directions.
- OWL domains and ranges infer types; they do not reject data. Validation is done with SHACL.
- No generic names (`value`, `type`, `date`).

**Reuse.** Use an existing vocabulary before coining a term: SKOS for synonyms and the glossary,
PROV-O for provenance, Dublin Core for documents, OWL-Time, QUDT for units, ISO codes for
jurisdictions and currencies.


## 3. Rules for terms
Every term has:
- a **label**, singular, in business language (`UpperCamelCase` for classes, `lowerCamelCase`
  verb phrases for properties);
- a **definition** of the form "An A is a B that C", where B is the parent and C is what sets it
  apart: *A square is a rectangle that has equal side lengths*;
- the **source** of the definition, with its section;
- **synonyms** and abbreviations, where practice uses them;
- an IRI that is **never renamed**. A retired term is marked `owl:deprecated` and points to its
  replacement.


## 4. Process
1. Start from a competency question. If none needs the change, it does not go in the core.
2. Make the change with its test: a query for the question and the expected result on a fixture.
3. Run the checks (`python3 tools/check.py`). CI runs them on every pull request.
4. Add a line to [CHANGELOG.md](CHANGELOG.md).
5. Fixtures use real, cited facts. Anything invented for shape (a policy, a claim) is in a
   separate file and marked synthetic.

There is no one correct way to model a domain, and the work is iterative. When two designs both
answer the questions, take the smaller one.


## 5. Software
All open source and free.
- **Language**: OWL 2 in Turtle; SHACL for validation; SPARQL for tests
- **Checks**: Python with `rdflib` and `owlrl`
- **Editor**: any text editor, or [Protégé](https://protege.stanford.edu/)


## 6. Sources
1. Noy and McGuinness, [Ontology Development 101](https://protege.stanford.edu/publications/ontology_development/ontology101.pdf), Stanford.
2. Palantir, [Ontology best practices](https://www.palantir.com/docs/foundry/ontology/ontology-best-practices).
3. Carmody, [Best Practices: Ontology Development and Curation](https://www.niehs.nih.gov/sites/default/files/2025-03/CARMODY_bestpractices_508.pdf), NIEHS, and the [OBO Foundry principles](https://obofoundry.org/principles/fp-000-summary.html) it summarizes.
4. Michael K. Bergman, [A Reference Guide to Ontology Best Practices](https://www.mkbergman.com/911/a-reference-guide-to-ontology-best-practices/).
5. Sales et al., the Common Ontology of Value and Risk (COVER), and the [Unified Foundational Ontology](https://nemo.inf.ufes.br/en/projetos/ufo/).
