# Actuarial Ontology: foundations review

Reviewed: `actuarial-ontology.ttl` v0.7.0-draft (last changed 2026-01-12), the two Canadian P&C
knowledge-base files, the documentation, and how the Actuarial Notes Wiki stores the data this
ontology is meant to organize. Date of review: 2026-11-23.

Scope agreed for the review: the ontology is the foundation of the Actuarial Coworker agent,
Canadian P&C first; the wiki's markdown frontmatter stays the source of truth for instances, and
the ontology is the schema that data is validated against and exported through.

This document describes 0.7.0 as it was reviewed. File names and line numbers refer to that
version (commit `8854b35`).

**Since the review (0.8.1):** Step 13 of section 9 is done. The lists now cover the wiki's
document types and every jurisdiction, line and assumption kind its pages use, they are published
as `lists/lists.json`, and the wiki's resource, assumption and timeline lints read a copy of it.
Institution types are published as notations on the role types, but no wiki lint checks one yet.

**Earlier (0.8.0):** Phases 1 and 2 are done too: the questions were agreed, and the
ontology was rebuilt as a small core with lists, a glossary, shapes and tests (see
[model.md](model.md) and the changelog). Still open from section 9: a resolvable IRI, French
labels, sourced glossary definitions, and all of phases 3 and 4.

**Earlier (0.7.1):** Phase 0 of the roadmap is done. F1 and F2 are fixed, CI is in place
(`tools/check.py`), the original knowledge base and the three outdated documents are removed, and
the example data is now `examples/canadian-pc-example.ttl`. The maintainer chose to shrink the
core (decision 1). The questions in section 5 are superseded by
[competency-questions.md](competency-questions.md), which restates them one question at a time.

---

## 1. Verdict

The ontology is a well-labelled glossary with a sound risk pattern at its centre. It is not yet a
foundation an agent can hold data in. Four things stand between the two:

1. **It is logically broken in two places.** One IRI is defined twice, which makes every
   organization a person (F1), and the ontology plus its own example knowledge base is
   inconsistent (F2).
2. **It models the wrong half of the domain for the Coworker.** It is deep on actuarial practice
   as US standards describe it (ASOP 23, 25, 38, 41, 51, 56) and thin on what the Coworker's data
   is about: regulations, jurisdictions, lines of business, institutions, published documents,
   filings, dated figures and events. Of 30 Coworker questions drafted for this review, 3 can be
   expressed in today's vocabulary (section 5).
3. **Nothing is enforced or tested.** There are no cardinalities, no SHACL shapes, no CI, and the
   documented "100% competency-question answerability" means only that the words exist: of the 22
   documented queries, 1 returns rows against the knowledge base (F5).
4. **It is disconnected from the wiki.** The wiki already has a working data model for
   regulators, documents, metrics and assumptions, with provenance and validity dates. The
   ontology has none of those concepts, and no file in either repo maps one to the other
   (section 6).

What is worth keeping: the naming is clean and consistent, every term has a label and a comment,
the licence is open, and the COVER pattern (peril, threat event, loss event, loss; value and risk
as two sides of one thing) is a published, defensible core that suits catastrophe and risk work.

The recommendation is a **v0.8 "foundation" release that shrinks and repairs before it grows**:
fix the logic, cut the core to what competency questions need, add the eight missing core types,
put observations, provenance and time in the model, and make the wiki's frontmatter validate
against it in CI. Section 8 sketches the target and section 9 the order of work.

---

## 2. Scorecard

Practices are the ones agreed in the review plan (A to H). Ratings: ● meets, ◐ partly, ○ does not.

| | Practice | Rating | Main evidence |
|---|---|---|---|
| A | Purpose and scope: competency questions, tested, sized to the application | ○ | 14 generic questions, none about a regulation, a jurisdiction, a filing or a dated figure; queries are templates (F5); 67 of 302 classes are reachable by no property (F6) |
| B | Model the domain, not the sources | ◐ | Business names throughout (good). Sections and classes follow ASOP numbers, not the domain (F12). Measurements are not separated from the things measured (F7) |
| C | Class hierarchy | ○ | A cycle (F1); 57 roots (F3); 22 single-child classes; 28 flat children under one class; individuals and statuses modelled as classes (F9) |
| D | Composition and roles | ◐ | Roles are annotated as roles but implemented as static subclasses; an insurer that buys reinsurance is inferred to be an Insured (F4, F9) |
| E | Properties | ○ | No cardinality, no functional properties, no restrictions; 5 inverses for 84 object properties; 4 with no range; domains infer wrong types (F4, F10) |
| F | Terms and documentation | ◐ | 412 of 412 terms have a label and a comment. No synonyms, no stable IDs, 67 source references with no section, about a third of definitions name their parent (F11) |
| G | Governance | ○ | The IRI does not resolve, no releases or tags, no CI, the docs' counts and claims are wrong, a referenced companion doc does not exist (F13) |
| H | Agent readiness: tests, SHACL, provenance, time, T-box and A-box split, reuse, actions | ○ | None present. The example data mixes real institutions with invented people and uncited figures (F8) |

---

## 3. Findings

Severity: **Critical** breaks reasoning today; **High** blocks the Coworker use; **Medium** is
quality debt that grows with every instance added.

### F1. Critical: `ao:Agent` is defined twice, so every organization is a person

`ao:Agent` is the top-level UFO category (line 685, "An entity with intentionality…") and is
declared again at line 1829 as "Insurance Agent", a subclass of `ao:Person`. Turtle merges the
two, so the graph says `Agent ⊑ Person` and `Person ⊑ Agent`. The two are therefore equivalent,
and `Organization ⊑ Agent` makes every organization a person.

Evidence: after OWL-RL inference, `Organization rdfs:subClassOf Person` holds, and all 18
organizations in the knowledge base (Intact, OSFI, Hannover Re…) are typed `Person`. The class
also carries two labels and two definitions. `CaptiveAgent`, `IndependentAgent` and
`ManagingGeneralAgent` are subclasses of this merged class, so they sit beside `Organization` at
the top level.

Fix: rename the second to `ao:InsuranceAgent`, and add a CI check that fails on any subclass
cycle and on any term with more than one `rdfs:label` per language. Ontology 101 §4.1 names
cycles as the first hierarchy error to rule out.

### F2. Critical: the ontology and its example knowledge base are inconsistent

`kb:PeerReview_Reserving_2024` is typed `ao:PeerReview` (an Activity, so a Perdurant) and is the
subject of `ao:reviewedBy`, whose domain is `ao:ActuarialCommunication` (an Object, so an
Endurant). `Endurant` and `Perdurant` are disjoint. A reasoner run on the two files together
reports an inconsistency, after which nothing it infers can be trusted.

This shows that the knowledge base was never run through a reasoner, although the Project Guide
lists that as step 8 and names FaCT++ as the testing tool.

Fix: correct the instance, and run a reasoner over ontology plus data in CI.

### F3. High: 57 root classes; the upper ontology covers under half the model

The file declares a UFO top level (`Endurant`, `Perdurant`, `Moment`), but 55 other classes have
no parent at all, including the ones the domain turns on: `Claim`, `InsurancePolicy`,
`InsuranceProduct`, `Coverage`, `Premium`, `Peril`, `Loss`, `Regulation`, `Risk`, `Portfolio`,
`Assumption`, `ActuarialModel`, `Data`.

The risk hierarchy is split across roots. `Risk` has `CreditRisk`, `MarketRisk` and so on, while
`InsurableRisk` (with `MortalityRisk`, `PropertyRisk`, `CatastropheRisk`), `SystemicRisk`,
`IdiosyncraticRisk`, `UninsurableRisk`, `PreferredRisk`, `StandardRisk`, `SubstandardRisk` and
`DeclinedRisk` are separate roots, not kinds of `Risk`. `covers` has range `Risk`, so a policy
covering a `PropertyRisk` only type-checks by inference. The four underwriting classes
(preferred, standard, substandard, declined) are not risks at all; they are the classes an
underwriter assigns an applicant to.

Fix: every class gets exactly one path to a top-level category, or the UFO layer is dropped from
the OWL file and kept as annotation (section 8 recommends the second).

### F4. High: domains and ranges are written as constraints but act as inferences

In OWL, `rdfs:domain` does not reject a bad statement; it concludes the subject has that type.
The ontology uses domains as if they validated. Results from the knowledge base:

| Asserted | Inferred as well | Cause |
|---|---|---|
| `Premium`, `Limit`, `Deductible`, `CaseReserve`, `IBNRReserve` (30 individuals) | `FinancialMeasurement`, `Measurement`, `Moment` | `hasMonetaryValue` has domain `FinancialMeasurement` |
| `Insurer` (Intact, Wawanesa) | `Insured` | `hasPolicy` has domain `Insured`; used for their reinsurance treaties |
| `Reserving`, `Pricing` (activities) | `ActuarialModel` | a model-domain property used on the activity |
| `Regulator` (OSFI) | `IntendedUser` | range of `hasIntendedUser` |
| `PeerReview` | `ActuarialCommunication` | F2 |

A `CaseReserve` thus ends up as both a `Liability` (a `FinancialInstrument`, an `Object`) and a
`Moment`. No disjointness is declared between those, so the reasoner stays silent about it.

Fix: validate with SHACL shapes (closed-world, reports errors) and keep OWL domains only where
the inference is wanted. Put shared properties on general classes: a monetary amount belongs to
anything that has one.

### F5. High: "100% competency-question answerability" is not a test result

`AO-Testing-Report.md` gives 22 SPARQL queries for 14 questions and concludes all 14 are "fully
answerable". Run as written against the ontology plus the improved knowledge base:

- 15 queries use placeholder individuals (`:SpecificEntity`, `:SpecificInsurer`) under an
  undeclared prefix and do not parse.
- 6 parse and return no rows, with or without inference (mortality risk, natural-peril claims,
  mortality tables, both Solvency II queries).
- 1 returns rows (reserves for outstanding claims).

So "answerable" means the property and class names needed to phrase the question exist. That is a
vocabulary check. Nothing runs these queries, and no data answers 13 of the 14.

The 14 questions are also not the Coworker's. None mentions a jurisdiction, a regulation's
effective date, a line of business, a filing, a published figure or a source. Palantir's
validation guidance is to take questions from the operating rhythm, not from what the model
already covers.

Fix: a `tests/` folder with one `.rq` file per competency question, a small fixture of real,
cited instances, an expected result per query, and a CI job. Section 5 drafts the questions.

### F6. High: the core types for the Coworker's data are missing

The stated purpose is to organize data about policies, regulations, events and institutions.
What the ontology has for each:

| Needed | In the ontology today |
|---|---|
| Regulation, guideline, standard, statute, with issuer, jurisdiction, effective and superseded dates | `Regulation` (no parent, one subclass: `Solvency2`), `ActuarialStandard`, `AccountingStandard` (subclasses `IFRS17`, `GAAP`). Two properties: `mandates` (no range) and `prescribesMinimum`. No dates, no issuer, no supersession |
| Jurisdiction | Nothing |
| Line of business | Product classes (`AutoInsurance`, `HomeownersInsurance`…) only; no line as a classification that a regulation, a filing or a figure can point at |
| Institution: regulator, rating board, statistical agency, professional body, insurer, reinsurer, group and subsidiary | `Regulator`, `Insurer`, `Reinsurer`, `DirectWriter`. No statistical agency or professional body (the wiki had to add `industry_bureau` locally), no ownership or group structure, no licence or regulated-by-for-what |
| Published document and its parts (source, edition, page) | `ActuarialReport`, `RegulatoryReport`, `DataSource`, `WorkPaper`. No general document, edition or locator |
| Filing: rate filing, regulatory return | `filesReport` to `RegulatoryReport`. No rate filing, no approval decision linked to one |
| Dated figure: a filed ratio, a benchmark trend, a prescribed factor | Measurement classes with a bare decimal (F7) |
| Event: catastrophe, reform, court decision, merger | `Event` with `ThreatEvent`, `LossEvent`, `ExtremeEvent`. No catastrophe event as one named thing, no regulatory or corporate event, no location |
| Policy form and coverage terms | `InsurancePolicy`, `Coverage`, `Limit`, `Deductible`, `Exclusion` exist, but no property joins a limit, deductible or premium to a coverage or a policy; the 23 such individuals in the knowledge base are linked to nothing |
| Time period, currency, unit | Nothing |
| Agent action or tool | Nothing |

At the same time 67 of the 302 classes are reached by no property, directly or by inheritance
(the whole life-product branch, pensions, embedded value, the underwriting classes), and 86 are
named in any domain or range. They are glossary entries, and the wiki's 1,402 concept pages
already do that job with definitions that have been fact checked.

Fix: decide by competency question what stays in the core (Ontology 101 §4.7: the ontology
"should not contain all the possible information about the domain"), move the glossary terms to a
SKOS vocabulary linked to the wiki's concept pages, and add the missing core types (section 8).

### F7. High: measurements are not separated from what they measure, and carry no context

`LossRatio`, `CombinedRatio`, `ReturnOnEquity`, `LapseRate` and `EmbeddedValue` are classes of
`Measurement` with `hasValue` (a decimal). Nothing says which entity the value is about, for what
period, on what basis (accident year or calendar year, gross or net, as filed or restated), in
what unit or currency, as of when, or from which document. `hasMonetaryValue` is "in base
currency", which is never defined. `hasSeverity` puts a bare decimal on a `Loss`.

There are three overlapping ways to state a number: `hasValue`, `hasMonetaryValue`, and
single-class properties (`cashValueAmount`, `deathBenefitAmount`, `embeddedValueAmount`,
`lapseRate`, `persistencyRate`, `retentionAmount`, `exposureAmount`). The Palantir guidance calls
the first two "The Misnomer" (generic `value`) and asks that identity be separated from
observation.

This is the pattern the Coworker needs most ("Intact's MCT ratio at Q3 2025, as filed with
OSFI"), and the wiki already stores it correctly: `research_metrics` has value, unit, period,
province, line of business, source page and the verbatim source text.

Fix: one `Observation` pattern (section 8) and no bare numbers elsewhere.

### F8. High: no provenance, no validity time, and example data that breaks the wiki's rules

- No term records where a fact came from or when it was true. The knowledge base states the Fort
  McMurray insured loss as 3,580,000,000 with no source, date of estimate or currency.
- The improved knowledge base mixes real institutions and events with invented people
  ("Alex Johnson, homeowner in Calgary"), invented policies, claims, reserves and named actuaries,
  with nothing marking which is which. The wiki's first rule for this kind of data is that
  nothing is invented and a sample names no particular document.
- `occurrenceDate` has range `xsd:dateTime`; all 12 uses give an `xsd:date`. Policy and claim
  numbers are untyped literals where the range is `xsd:string`. OWL does not report either.
- 47 of the 148 individuals have no object-property link to anything.
- The original knowledge base (`canadian-pc-insurance-knowledge-base.ttl`) uses the namespace
  `http://example.org/actuarial-ontology#`, so not one of its 3,034 triples refers to this
  ontology. The README links to that file as the example.

Fix: retire both files. Replace them with a small fixture generated from the wiki (real, cited)
and a clearly separate synthetic fixture for policy and claim shapes, each individual marked
synthetic.

### F9. Medium: hierarchy errors

Each of these fails the true-path rule (everything true of the parent is true of the child), or
models as a class something that is an individual, a status or a value.

| Problem | Examples | Better |
|---|---|---|
| Individuals as classes | `Solvency2`, `IFRS17`, `GAAP`, `ORSA` | Individuals of `Regulation` / `AccountingStandard`; the Coworker asks about *the* MCT guideline, 2024 edition, not about a kind of regulation |
| Status as subclass | `PaidClaim`, `OutstandingClaim`, `ReportedClaim`, `InForcePolicy`, `FraudulentClaim` | A status property with dated history; an object should not change class when it is paid (Palantir: one object per entity, history separate) |
| Value partition as classes | `FullCredibility`, `PartialCredibility`, `NoCredibility` beside `credibilityWeight` | The number alone |
| Part or input filed as a kind | `FrequencyModel` and `SeverityModel` under `CatastropheModel`; `LossDevelopmentTriangle` and `MortalityTable` under `ActuarialModel` | Components (`hasComponent`); a triangle is data and a mortality table is an assumption set |
| Method filed as model | `ChainLadderMethod` under `ReservingModel`, `GeneralizedLinearModel` under `PricingModel`, `Bootstrapping` under `StochasticModel` | A `Method` type; a GLM is used in reserving too |
| Two axes as siblings | `TreatyReinsurance`, `FacultativeReinsurance`, `ProportionalReinsurance`, `NonProportionalReinsurance` all under `ReinsuranceContract` | Two properties (placement basis, sharing basis); a contract is one of each |
| Wrong parent | `Capital ⊑ Asset`; `CashValue ⊑ Capital`; `Asset` and `Liability ⊑ FinancialInstrument`; `Reserve` defined as "funds set aside"; `AutoInsurance ⊑ PropertyInsurance`; `ReinsuranceContract ⊑ InsurancePolicy`; `IncurredButNotReported ⊑ Claim` | Capital is assets less liabilities; a reserve is a liability estimate; auto includes liability coverage; IBNR is an estimate for claims not yet made |
| Product and contract conflated | `ParticipatingPolicy ⊑ LifeInsurance ⊑ InsuranceProduct`; the knowledge base types one thing as both `InsurancePolicy` and `AutoInsurance` | A policy is a contract that is an instance of a product |
| Definition contradicts parent | `ORSA ⊑ ActuarialActivity`, defined as "a requirement" | Split the requirement from the assessment |
| Duplicates | `Persistency` and `PersistencyRate`; `LapseRate` class and `lapseRate` property | One term |
| Shape warnings | 22 classes with one child; `ActuarialActivity` with 28 flat children mixing `ORSA`, `Valuation` and `DurationMatching` | Ontology 101 §4.2: one child or more than a dozen suggests a missing level or a missing class |

Roles deserve a decision of their own. `Insurer ⊑ Organization` and `Insured ⊑ Agent` are
annotated `anti-rigid` and `role`, which is the right analysis, but as OWL subclasses they are
permanent types. With instance data that produces the Intact-is-an-Insured result in F4, and it
cannot say *when* or *for which contract* someone held a role. Section 8 proposes roles as
relationships.

### F10. Medium: properties

- 4 object properties have no range (`classifiesAs`, `mandates`, `generatesScenario`,
  `compliesWith`); `compliesWith` has no domain either, and it is the property behind the one
  regulatory competency question.
- 5 inverse declarations among 84 object properties. `insures`, `regulates`, `covers`,
  `hasPolicy`, `hasClaim`, `triggeredBy` and `causedBy` have none.
- No functional properties, cardinalities, restrictions, sub-properties or property chains. A
  policy may have five effective dates and a claim no policy.
- Two disjointness axioms in the whole file. `Person` and `Organization` are not disjoint, which
  is why F1 went unnoticed.
- One property per activity class (`identifies`, `monitors`, `mitigates`, `quantifies`,
  `calibrates`, `validates`, `documents`, `segmentsInto`) repeats what `hasSubject` already says.
- Data properties are bound to one class each. `effectiveDate` has domain `InsurancePolicy`, so a
  regulation, a guideline or a rate change cannot have one without being inferred a policy.

### F11. Medium: terms and definitions

Good: every one of the 412 terms has a label and a comment; names are singular UpperCamelCase
for classes and lowerCamelCase verb phrases for properties, with one plural
(`UnderwritingGuidelines`) and no duplicate labels.

Gaps against the NIEHS term anatomy (label, ID, definition, parent, synonyms, reference):

- **No synonyms.** The README's case for the ontology is that terms like "claim" and "risk" are
  overloaded, yet there is no `skos:altLabel`, no abbreviation and no way to record that
  "reserve", "provision", "unpaid claim liability" and "liability for incurred claims" overlap.
- **No definition sources.** 67 terms carry `asopReference`, as a bare string ("ASOP 51") with no
  section. The other 345 cite nothing. No term cites a CIA Standard of Practice, an OSFI
  guideline or IFRS 17.
- **Definitions are not genus-differentia.** The documentation says every definition follows
  "A is a B that C". About a third (103 of 302, by a text match on the parent's label) name
  their parent. `Loss` is "a reduction in value or financial detriment"; `Estimate` is "an
  approximation or best judgment of a quantity".
- **IDs are the names.** A rename breaks every reference. Opaque IDs are the OBO convention; for
  a small hand-edited ontology, readable IRIs with a strict no-rename rule and `owl:deprecated`
  are an acceptable trade, but the rule has to be written down.
- **English only.** The first scope is Canada; OSFI, the AMF and the CIA publish in French, and
  the OSFI pipeline in the wiki already keeps both languages' labels.

### F12. Medium: organized by source standard, and by a US one

More than twenty sections of the file are named for a standard or a source ontology ("ASOP 51: Risk
Assessment Components", "ASOP 56: Model Governance Activities", "UFO-C: Social and Intentional
Entities", "COVER Value Concepts"). That is modelling the source, and it shows in the result:
there are more than a dozen classes for intentions, beliefs, goals, commitments, rights and value
ascriptions, and none for a jurisdiction or a line of business. For a Canadian P&C Coworker the references
would be the CIA Standards of Practice, OSFI's guidelines (MCT, the Appointed Actuary's report),
IFRS 17, provincial rate regulation and the CAS literature the wiki already indexes.

### F13. Medium: governance

| OBO principle | State |
|---|---|
| Open | ● MIT |
| Identifier space | ○ `http://actuarialnotes.com/ontology/actuarial` redirects to the site's home page; no version IRI |
| Versioning | ○ "0.7.0-draft" in the file; no git tags or releases; the changelog is prose inside the documentation |
| Documentation | ◐ Present but inaccurate: it says about 320 classes and about 90 properties (there are 302 and 110), that domain and range restrictions are future work (most exist), and that every definition is genus-differentia |
| Locus of authority, change process | ○ No named owner, no issue templates, no contribution checks |
| Maintenance | ○ No CI. Last change ten months ago |
| Cross-references | ○ The wiki's agent plan cites `Actuarial-Ontology/docs/actuarial-agent.md`, which does not exist, and says the wiki is mapped to the ontology by `scripts/ontology_map.py`, which maps question topics to concept pages and does not mention the ontology |

---

## 4. Automated checks

| Check | Tool | Result |
|---|---|---|
| Parses | rdflib 7.6 | All three files parse. 1,845 triples in the ontology |
| Undeclared terms | script | None in the ontology or the improved knowledge base. The original knowledge base uses a different namespace throughout |
| Subclass cycles | script | 1 (`Agent`/`Person`, F1); 22 classes fall inside it |
| Consistency, ontology alone | OWL-RL closure | No clash, because only two disjointness axioms exist to clash with |
| Consistency, ontology plus improved knowledge base | OWL-RL closure | Inconsistent (F2); 18 organizations inferred persons |
| Datatypes | script | 25 literals whose datatype differs from the property's range |
| Documented competency queries | rdflib SPARQL | 15 do not parse, 6 return nothing, 1 returns rows |
| Unconnected elements | script | 57 roots; 67 classes reached by no property |
| Missing domain or range | script | 1 and 4 |
| Missing annotations | script | None |
| OOPS! pitfall scanner | not run | The session's safeguards blocked posting the file to the external service. The script covers its most relevant pitfalls (cycles, unconnected elements, missing annotations, domains, ranges and inverses, synonyms as classes). Worth running by hand once: paste the file at oops.linkeddata.es |

The closure used is OWL 2 RL. It is enough to show both critical findings; a full DL reasoner
(HermiT or ELK through ROBOT) should be the one wired into CI.

---

## 5. Purpose fit: thirty Coworker questions

These are drafts for the maintainer to edit; they become the test suite. Each was checked against
the ontology's vocabulary by hand: **Yes** means classes and properties exist to phrase it,
**Part** means the entities exist but a needed property or qualifier does not, **No** means a
core concept is absent.

| # | Question | Today | Missing |
|---|---|---|---|
| | **Regulation** | | |
| 1 | Which guidelines apply to a federally regulated P&C insurer's capital today? | No | jurisdiction, issuer, in-force dates, applies-to |
| 2 | What did OSFI's MCT guideline require before 2024, and what replaced it? | No | edition, supersedes, validity |
| 3 | What is the supervisory target MCT ratio, and where is it stated? | No | prescribed figure, locator |
| 4 | Which regulator approves private passenger auto rates in Alberta, and under what filing rules? | No | line of business, jurisdiction, regulatory domain |
| 5 | Which Ontario auto reforms changed accident benefits since 2010, in order? | No | regulatory event, date, line, jurisdiction |
| 6 | Which standards of practice govern a reserve valuation in Canada? | Part | standard as individual, applies-to activity, jurisdiction |
| 7 | Which documents does this guideline cite, and which cite it? | No | document, cites |
| | **Institutions** | | |
| 8 | Who regulates Intact for solvency and who for market conduct in Ontario? | Part | regulatory domain, jurisdiction on `regulates` |
| 9 | Which companies are in the Intact group, and which acquired RSA Canada? | No | group structure, corporate event |
| 10 | Which insurers are federally regulated and write personal auto in Alberta? | No | licence, line, jurisdiction |
| 11 | Which bodies publish loss trend benchmarks for Ontario auto? | No | publisher role, benchmark, statistical agency |
| 12 | Which reinsurers does this insurer cede to, under which treaties? | Yes | |
| | **Published figures** | | |
| 13 | What MCT ratio did each insurer file with OSFI for a given quarter? | No | observation with period, source filing |
| 14 | How has one insurer's combined ratio moved over five years, by line? | No | period, line, basis |
| 15 | What ULAE factor does GISA publish for Ontario private passenger auto, which edition? | No | assumption, edition, locator |
| 16 | What profit provision does the AIRB allow, effective when? | No | prescribed figure, effective date |
| 17 | Which figures in this workflow come from a document that has since been superseded? | No | provenance, supersedes |
| 18 | Has this figure been fact checked, and against what? | No | verification status, source |
| | **Events** | | |
| 19 | What were the five costliest insured catastrophes in Canada, by whose estimate? | Part | event as one thing, estimate source, as-of date, currency |
| 20 | Which perils and lines did the 2024 Calgary hailstorm affect? | Part | line of business, location |
| 21 | What is the impact on our loss ratio of a given event? | No | observation, attribution of losses to an event by period |
| 22 | Which events led to a regulatory change? | No | event-to-regulation link |
| | **Policies and coverage** | | |
| 23 | What does a standard Ontario auto policy (OAP 1) cover and exclude? | Part | policy form as a type, coverage part, link from limits and exclusions |
| 24 | Which coverages are mandatory for auto in each province? | No | jurisdiction, mandatory-coverage rule |
| 25 | Which claims on this book were triggered by a natural peril? | Yes | |
| 26 | What limit and deductible apply to this coverage on this policy? | Part | properties joining them |
| | **Actuarial work** | | |
| 27 | Which assumptions does this indication use, and where does each come from? | Part | assumption value, source, selected-by |
| 28 | Which calculation can take this published table as an input? | No | tool, input and output types |
| 29 | Which model produced this estimate, on what data, reviewed by whom? | Yes | |
| 30 | Which concept page defines this term, and which exam readings teach it? | No | link to the wiki's concepts |

Three Yes, seven Part, twenty No. Every No is caused by the same eight absences: jurisdiction,
line of business, document with edition and locator, observation with period, validity time,
provenance, institution structure, and tool.

---

## 6. Fit with the wiki

The wiki already holds the Coworker's data in five places. None references the ontology, and
they do not agree with each other on shared vocabulary.

| Wiki store | What it models | Ontology counterpart |
|---|---|---|
| `Resources/Regulation`, `Events`, `Benchmarks` frontmatter (`id`, `type`, `status`, `date`, `jurisdiction`, `lob`, `issuing_body`, `impact_level`, `impacted_agents`, `tags`, `aliases`, `source_url`) | Dated regulations, events, benchmarks | `Regulation` and `Event` exist; none of the keys has a property |
| Resource pages (`Title`, `Authors`, `Publisher`, `Year`, `Edition`, `Type`, `Code`, `ISBN`, `Available from`) | Published documents | None |
| `Assumptions/*.md` (`Source`, `Edition`, `Effective`, `Jurisdiction`, `Practice`, `Source sha256`, `Read`; rows of kind, value, unit, locator) | Published figures with provenance | `Assumption` exists as a bare class |
| `research_*` tables and `lib/researchOntology.ts` (agents with type, jurisdiction scope, provinces, regulatory domains, parent; documents with type, effective and expiry dates, superseded-by; metrics with value, unit, period, province, line, source page and text; relationships with valid-from and valid-until and how they were inferred) | Institutions, documents, metrics, relationships | `Regulator`, `Insurer`, `regulates`. This schema is ahead of the ontology on every point in F6 to F8 |
| `data/coworkSources.ts`, `.osfi/`, `lib/tools/` | Publishers and documents, OSFI filings by quarter with cell addresses, calculators with typed inputs | None |
| `Concepts/*.md` (1,402 pages) | Definitions | 83 of the 302 classes have a same-named page; nothing links them |
| `verification:` block and `.verify/` logs | Whether a fact was checked, against what, when | None |

Vocabulary that differs between stores today:

| Thing | Forms in use |
|---|---|
| Line of business | `"Auto-Personal"` (frontmatter), `personal_auto` (research), `ao:AutoInsurance` (ontology, a product class), `Line: …` (assumptions) |
| Jurisdiction | `"CA-ON"` (frontmatter, assumptions), `provinces: ['ON']` with a separate scope (research), free text in comments (knowledge base) |
| Institution type | six `AgentType` values (research), `EntityCategory` (source catalogue), `Regulator` / `Insurer` (ontology) |
| Document type | `Type:` on resource pages, the `document_type` enum, `ResourceKind`, lower-case `type:` on dated pages |
| One regulator's name | "Alberta Insurance Rate Board" in `researchOntology.ts`; "Automobile Insurance Rate Board" on its assumptions page |
| `Resources/Regulation` | two frontmatter shapes in one folder (7 files in the dated shape, 4 in the resource-page shape) |

This is where the ontology can earn its place soonest: as the single definition of those
vocabularies, with the wiki's lint scripts reading it. The wiki has the data discipline (hashes,
locators, fact checks, nothing invented) and lacks one shared schema; the ontology has a schema
and none of the discipline.

The instance decision (frontmatter is the source of truth) implies a concrete mechanism: a
mapping from frontmatter keys to ontology properties (a JSON-LD context is the lightest form), an
export script that turns the vault into RDF at build time, and SHACL shapes run on that export in
the wiki's CI beside `resource_lint.py` and `assumption_lint.py`.

---

## 7. Reuse

Ontology 101's step 2 and OBO principle P7 both say to reuse before coining. The ontology
imports nothing and its documentation lists FIBO and schema.org mappings as future work. For
each candidate, the recommendation is to **reference** its terms where they fit (import only
small vocabularies), since importing FIBO whole would bury a 300-class ontology under several
thousand.

| Need | Candidate | Use |
|---|---|---|
| Synonyms, glossary, the concept pages | SKOS | `skos:prefLabel`, `altLabel`, `definition`, `exactMatch`; the glossary half of today's classes becomes a SKOS concept scheme |
| Provenance | PROV-O | `prov:wasDerivedFrom`, `prov:generatedAtTime`, `prov:wasAttributedTo` |
| Documents | Dublin Core Terms, FaBiO or schema.org `CreativeWork` | title, publisher, issued, edition, `isVersionOf`, `replaces` |
| Dated statistics | RDF Data Cube (`qb:Observation`) or SOSA | the observation pattern in section 8 |
| Time | OWL-Time | periods, instants, intervals |
| Units and currency | QUDT, ISO 4217 codes | unit and currency as individuals, not strings |
| Jurisdictions | ISO 3166-1 and 3166-2 codes; GeoNames or Wikidata IRIs for places | `CA`, `CA-ON` already match the wiki's frontmatter |
| Organizations and legal entities | W3C Org, FIBO Business Entities, LEI | group structure, legal form; an LEI where one exists |
| Contracts, financial instruments | FIBO | align `InsurancePolicy` and `ReinsuranceContract` as contracts |
| Legislation | ELI (European Legislation Identifier) pattern | work, expression, in-force dates, amends, repeals |
| Upper ontology | gUFO (the published OWL form of UFO) | if the UFO layer stays, reference gUFO instead of re-declaring `Endurant`, `Perdurant` and `Moment` locally |
| Validation | SHACL | shapes for every core type |

These mappings are from knowledge of the vocabularies, not from a term-by-term comparison; each
should be confirmed against the current release when it is adopted.

---

## 8. Target shape

A proposal to react to, not a design to accept. Three layers in three files:

**`ao-core.ttl`: about 40 classes, each justified by a competency question.**

```
Party                 Organization | Person            (disjoint)
RoleAssignment        party, roleType, context, validFrom, validTo
                      roleType ∈ Insurer, Reinsurer, Regulator, RatingBoard,
                      StatisticalAgency, ProfessionalBody, Policyholder, Broker…
Jurisdiction          ISO 3166 code, parent jurisdiction
LineOfBusiness        one scheme, mapped to OSFI's and GISA's own line lists
Document              publisher, issued, edition, replaces, url, sha256
DocumentPart          locator (page, section, table, cell)
NormativeDocument     ⊑ Document: Statute, Regulation, Guideline, Standard, FilingRule
                      issuedBy, jurisdiction, appliesToLine, effectiveFrom, effectiveTo
Requirement           statedIn DocumentPart, appliesTo roleType
Event                 CatastropheEvent | RegulatoryEvent | CorporateEvent
                      date or interval, location, peril, affectedLine
Product, Contract     InsurancePolicy and ReinsuranceContract ⊑ Contract
Coverage              ofContract, peril, limit, deductible, exclusion
Claim                 underContract, arisingFrom Event, status history
Quantity kind         LossRatio, MCTRatio, Trend, ULAEFactor… (individuals, not classes)
Observation           about (any entity), quantityKind, value, unit, currency,
                      period, basis, asOf, jurisdiction, line, source DocumentPart
Assumption            ⊑ Observation with status prescribed | published | selected
Method, Model, Tool   Tool: inputType, outputType, implements Method
Activity              performedBy, uses Model, input and output Observations
```

Three patterns carry most of it:

1. **Observation.** Every number is an observation about something, for a period, from a source.
   About a third of the 30 questions need it, and it matches the Assumptions Bank and
   `research_metrics` row for row.
2. **Role as relationship.** An organization is an insurer *under a licence, in a jurisdiction,
   from a date*. This is the Palantir "object-backed link" and UFO's relator, and it removes the
   static role subclasses.
3. **Document and edition.** A guideline is a work with editions; a figure or requirement points
   at a part of one edition. This is how the wiki already treats every source.

**`ao-vocabulary.ttl`: the glossary as SKOS.** The remaining ~250 terms (life products, embedded
value, ASOP 51 components, emerging risks) keep their definitions and gain synonyms, a source
reference and a link to the wiki's concept page. They stop being OWL classes until a competency
question needs one.

**`ao-shapes.ttl`: SHACL.** One shape per core type: required properties, cardinalities,
datatypes, allowed values.

The UFO and COVER analysis stays as annotation (`ufoCategory`, `rigidity`) or as a reference to
gUFO, and comes out of the class tree. It is useful for deciding how to model something; as a
local top level that covers under half the classes and has only two disjointness axioms, it adds
cost and no checking.

---

## 9. Roadmap

**Phase 0: repair (small, no design decisions).**
1. Rename the second `ao:Agent` to `ao:InsuranceAgent` (F1).
2. Add CI: parse, cycle check, duplicate-label check, reasoner over ontology plus fixtures.
3. Correct the documentation's counts and remove the "100% answerability" claim.
4. Retire the original knowledge-base file; mark the improved one as synthetic until replaced.
5. Tag v0.7.1.

**Phase 1: purpose (the maintainer's decisions).**
6. Agree the competency questions (section 5), and write each as a `.rq` test with an expected
   result on a real, cited fixture.
7. Agree the core list and the three patterns in section 8.

**Phase 2: foundation, v0.8.**
8. Build `ao-core.ttl` to the agreed questions; move the rest to `ao-vocabulary.ttl`.
9. Add observation, provenance, validity and role patterns; reference SKOS, PROV-O, Dublin Core,
   OWL-Time, QUDT and ISO codes.
10. Write SHACL shapes; fix the hierarchy errors in F9 that survive into the core.
11. Definitions: genus-differentia, a source for each, synonyms, French labels for the core.
12. Make the IRI resolve (w3id.org redirect to the tagged file) and add a version IRI.

**Phase 3: bind the wiki.**
13. Publish the controlled lists (jurisdiction, line of business, institution type, document
    type, quantity kind) from the ontology and have the wiki's lints read them.
14. Frontmatter-to-RDF export in the wiki build; run the shapes and the competency queries on it
    in the wiki's CI.
15. Link the 1,402 concept pages to vocabulary terms (`skos:exactMatch`), starting with the 83
    that already share a name.

**Phase 4: the Coworker.**
16. Describe each tool in `lib/tools/` as a `Tool` with typed inputs and outputs, so "which
    calculation takes this table" (question 28) is a query.
17. Run the question suite through the Coworker with only the ontology and the export, and
    compare with a person doing the same, as Palantir's validation page describes.

Later, once the core is stable: US and life extensions, and FIBO alignment for contracts.

---

## 10. Decisions for the maintainer

| # | Decision | Recommendation |
|---|---|---|
| 1 | Shrink the OWL core and move the glossary to SKOS, or keep 302 classes and repair in place? | Shrink. Repairing in place means writing properties, shapes and tests for classes no question uses |
| 2 | Keep UFO as the class tree's top level? | No; keep it as annotation or reference gUFO |
| 3 | Roles as relationships with dates, or as subclasses? | Relationships |
| 4 | The competency questions in section 5 | Edit freely; they decide everything in Phase 2 |
| 5 | Readable IRIs with a no-rename rule, or opaque IDs? | Readable, with the rule written down and `owl:deprecated` for retirements |
| 6 | Where the controlled lists live | In the ontology repo, consumed by the wiki |
| 7 | Phase 0 now? | Yes; it is mechanical and independent of the rest |

---

## 11. Method and limits

- Best practices: Palantir's ontology best-practices page (read in full) and its anti-patterns,
  validation and structural-guidance pages (each read to about the first 40,000 characters, the
  rest from an extracted summary); Noy and McGuinness, *Ontology Development 101* (full text);
  Carmody, *Best Practices: Ontology Development and Curation*, NIEHS (full text); and the OBO
  Foundry principles that deck lists.
- The genus-differentia count in F11 is a text match and is approximate.
- The "Today" column in section 5 was judged by hand against the vocabulary; no data exists to
  run those questions against.
- The OOPS! scan was not run (section 4).
- The reuse mappings in section 7 were not checked against the current releases of each
  vocabulary.
- Only Canadian P&C was assessed for fit. Life, pensions and US practice were looked at only to
  confirm that the proposed core does not shut them out.
