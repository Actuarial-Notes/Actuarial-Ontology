# The model

How version 0.8 is put together, for someone adding data or a term. The reasons behind it are in
the [review](ontology-review.md); the questions it is built to answer are in
[competency-questions.md](competency-questions.md).

## Files

| Path | Holds |
|---|---|
| `ontology/core.ttl` | The types every module shares |
| `ontology/institutions.ttl` | Supervision; which bodies publish what |
| `ontology/regulation.ttl` | Normative documents and requirements |
| `ontology/work.ttl` | Methods, steps, tools; one analysis and what it rests on |
| `ontology/events.ttl` | Catastrophe events and perils |
| `lists/` | The controlled lists: jurisdictions, lines of business, role types, regulatory domains, activity types, quantity kinds, units, bases, statuses, perils |
| `vocabulary/` | The glossary, in SKOS: 306 terms that need a definition but no structure |
| `shapes/shapes.ttl` | SHACL: what a record must have to be accepted |
| `tests/` | One query and expected result per competency question, and the fixtures they run on |

All terms share one namespace, `http://actuarialnotes.com/ontology/actuarial#` (`ao:`). Glossary
terms are in `…/actuarial/glossary#` (`aog:`).

## Seven categories

Everything is one of seven things, and nothing is two of them: **Party**, **Document**,
**Event**, **Observation**, **Activity**, **Method**, **Contract**. (Contract is reserved for the
policies module and has no properties yet.)

This is what settles an overloaded word. "Claim" is four glossary terms, one per sense: a demand
for payment and an insured occurrence (events), a claim file (a document) and an amount (an
observation).

## Three patterns

**1. Every number is an observation.** An observation states one value of one quantity kind, in
a unit, and says what it is about, for which period and on which basis, where it applies, and
how it came to be:

| Provenance status | The record must also give |
|---|---|
| Prescribed, Published, Reported | where it is stated (`ao:statedAt` a locator) |
| Selected | who selected it (`ao:selectedBy`) |
| Estimated | the analysis that produced it (`ao:producedBy`) |

A filed MCT ratio, a published ULAE factor, a prescribed profit provision, a catastrophe loss
estimate and an actuary's selected trend are all the same shape. An assumption is not a type: it
is an observation that an analysis uses (`ao:usesAssumption`).

**2. A role is a relationship.** An organization is not *an insurer* or *a regulator* by type.
A `RoleAssignment` says a party holds a role type, in a jurisdiction, for a line. A `Supervision`
says one organization oversees another for a regulatory domain in a jurisdiction. So one
organization can hold several roles, and a role can be limited to where and what it covers.

**3. A document has editions, and facts point at a place in one.** The `Document` is the work
(OSFI's Minimum Capital Test); a `DocumentEdition` is one dated version (Guideline A, 2024),
with its effective date and the edition it replaces; a `Locator` is a place in an edition
(section 1.2.1). A figure or a requirement points at a locator. That is what makes "which
edition is in force on this date" and "which figures rest on a replaced edition" answerable.

## What is deliberately not here

- **Statuses as classes.** A paid claim is a claim with a status, not a kind of claim.
- **Particular things as classes.** IFRS 17 or the 2024 MCT guideline is an individual.
- **A class per quantity.** Loss ratio, MCT ratio and IBNR are individuals of `QuantityKind`.
- **Instance data.** Real records live in the Actuarial Notes Wiki. `tests/fixtures/wiki.ttl` is a
  small hand transcription of some of them, standing in for the export the wiki will produce.
- **Anything no competency question needs.** The check fails on a class or property that no
  query uses.

## Adding something

1. Find or write the competency question that needs it.
2. Add the term to the right module, with a label and a definition of the form "An A is a B
   that C". If it is one of a fixed set of values, add an individual to a list instead.
3. Add or extend the shape in `shapes/shapes.ttl`.
4. Add the query in `tests/queries/`, the fixture records it needs, and run
   `python3 tools/check.py --update` to write the expected result. Read the result against the
   source before committing it.
