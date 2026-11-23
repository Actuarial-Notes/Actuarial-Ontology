# Requirements and competency questions

The requirements specification for version 0.8 of the Actuarial Ontology. Draft for the
maintainer to edit: a class or property goes into 0.8 only if a question here needs it, and every
term in 0.8 must be used by at least one question.

1. Purpose, users and scope
2. How a question is written
3. The questions, by module
4. Scenarios
5. Terms the questions presuppose
6. From question to test
7. Later modules

---

## 1. Purpose, users and scope

**Purpose.** The ontology is the schema for the data the Actuarial Coworker agent works with. It
gives one definition to the things that data is about, so that a figure, a rule or a step in an
analysis can be found, traced to its source and checked.

**Users.**

| User | Uses it to |
|---|---|
| The Coworker agent | Resolve a term to one meaning, find the figure or rule that applies, and say where it came from |
| A pricing or reserving actuary | Trace an indication or a reserve estimate back to its assumptions, data and sources |
| A reviewer or regulator | See which requirements apply to a piece of work and what it rests on |
| The Actuarial Notes Wiki | Validate its pages' frontmatter against one set of shared lists and shapes |

**In scope for 0.8.** Canadian property and casualty insurance: the regulations, institutions,
published figures, events, policies and coverages the Coworker's data describes, and the
ratemaking and reserving work chain that uses them.

**Not in scope for 0.8.**
- Education: syllabi, learning objectives, prerequisites, practice questions (section 7).
- Life insurance, pensions and regulation outside Canada.
- The content of a concept: formulas, derivations, distribution properties. The wiki's concept
  pages hold those; the ontology links a term to its page.
- Anything that needs judgement ("is this compliant?") or calculation ("what is the indicated
  rate?"). A calculation is a tool's job; the ontology says which tool takes what.

**Instances** live in the Actuarial Notes Wiki as sourced pages. This repo holds the schema and
small test fixtures.

---

## 2. How a question is written

**Form.**

1. **One question, one answer.** No "and". A question with two halves fails without saying which
   half failed.
2. **A stated answer shape**: a list, a single value, or yes/no.
3. **Parameters in [brackets].** The question is a template; its test binds it to one real case.
4. **Answerable from data**, with no judgement and no calculation.
5. **Small enough for one query.** A multi-step investigation is a scenario (section 4).

**Type**, after Keet and Khan (2024). Most question sets have only the first two; the last three
are how an overloaded term like "claim" or "loss" gets settled and stays settled.

| Type | Asks | Example |
|---|---|---|
| **V** Validating | The data must return an answer | Which edition of [document] is in force on [date]? |
| **R** Relationship | How two kinds of thing are related | Which quantity kinds does [method] take as input? |
| **S** Scoping | Whether something is covered at all | Is [activity] in scope? |
| **F** Foundational | What category a thing belongs to | Is a [loss] an event or an amount? |
| **M** Metaproperty | Whether a type is permanent, a role or a phase | Is [type] a role? |

**Priority.** **1** is built and tested first and defines 0.8. **2** follows in 0.8 if the
patterns built for priority 1 already answer it. **3** waits.

**Identifiers** are stable once this draft is approved: a question may be retired, never
renumbered.

**Test cases** name real entities only. Expected answers are not written here; they come from the
fixture, which is exported from the wiki's sourced pages. "Synthetic" marks a case that needs an
invented policy, claim or analysis, kept in a separate fixture.

---

## 3. The questions

Counts: 87 questions, 52 at priority 1. **All 52 are built and tested in 0.8.0**; each has a
query in `tests/queries/` named for its identifier. Priority 2 and 3 questions have no test yet.

### 3.1 Foundations (FD)

What kind of thing each core term is. These are answered by the ontology alone, with no instance
data.

| ID | Question | Type | Answer | Pri | Test case |
|---|---|---|---|---|---|
| FD1 | Is [activity] in scope? | S | yes/no | 1 | pension valuation; ratemaking |
| FD2 | Which senses does the term [term] have? | F | list | 1 | "claim" |
| FD3 | Which category is [sense of a term]: party, contract, document, event, observation, activity or method? | F | value | 1 | each sense of "claim", "loss", "reserve", "premium" and "policy" |
| FD4 | Is [type] a role? | M | yes/no | 1 | Insurer; Organization |
| FD5 | Which kinds of party can hold [role]? | M | list | 1 | Policyholder |
| FD6 | Is [type] a status of another type? | M | yes/no | 1 | paid claim |
| FD7 | Can one thing be both [type] and [type]? | F | yes/no | 1 | Event and Document; Person and Organization |
| FD8 | Is [named thing] an individual or a class? | F | value | 1 | the 2024 MCT guideline; Guideline |
| FD9 | Which sources define [term]? | V | list | 2 | "claim liabilities" |
| FD10 | How does [source] define [term]? | V | value | 2 | one source from FD9 |
| FD11 | Which terms are synonyms of [term]? | V | list | 1 | "development technique" |
| FD12 | Which concept page defines [term]? | V | value | 1 | "IBNR" |

### 3.2 Institutions (IN)

| ID | Question | Type | Answer | Pri | Test case |
|---|---|---|---|---|---|
| IN1 | Which body regulates [organization] for [regulatory domain] in [jurisdiction]? | V | value | 1 | Intact Insurance Company, solvency, Canada |
| IN2 | Is [organization] federally regulated? | V | yes/no | 1 | The Wawanesa Mutual Insurance Company |
| IN3 | Which bodies publish [quantity kind] for [line] in [jurisdiction]? | V | list | 1 | loss trend, private passenger automobile, Ontario |
| IN4 | Which jurisdictions does [body]'s authority cover? | V | list | 1 | FSRA (the wiki states no territory for GISA, the case first drafted) |
| IN5 | Which organizations belong to [group]? | V | list | 2 | Intact Financial Corporation |
| IN6 | Which organization acquired [organization]? | V | value | 2 | RSA Canada |
| IN7 | On what date did [acquisition] close? | V | value | 3 | the RSA acquisition |
| IN8 | Which insurers are licensed for [line] in [jurisdiction] on [date]? | V | list | 2 | personal auto, Alberta, 2026-01-01 |
| IN9 | Which reinsurers does [insurer] cede to under contracts in force on [date]? | V | list | 3 | synthetic |

### 3.3 Regulation and standards (RG)

| ID | Question | Type | Answer | Pri | Test case |
|---|---|---|---|---|---|
| RG1 | Which normative documents issued by [issuer] are in force on [date]? | V | list | 1 | OSFI, 2026-01-01 |
| RG2 | Which normative documents apply to [role] in [jurisdiction] for [regulatory domain] on [date]? | V | list | 1 | insurer, Canada, solvency, 2026-01-01 |
| RG3 | Which edition of [document] is in force on [date]? | V | value | 1 | OSFI's MCT guideline, 2024-06-30 (the wiki gives the 2023 edition no dates, so a 2023 date cannot be tested) |
| RG4 | Which document replaced [document edition]? | V | value | 1 | MCT guideline, 2023 edition |
| RG5 | From what date is [document edition] effective? | V | value | 1 | MCT guideline, 2024 edition |
| RG6 | Which body approves rates for [line] in [jurisdiction]? | V | value | 1 | private passenger automobile, Alberta |
| RG7 | Which filing rules apply to a rate filing for [line] in [jurisdiction] on [date]? | V | list | 1 | private passenger automobile, Alberta, 2026-01-01 |
| RG8 | Which standards of practice apply to [activity] in [jurisdiction]? | R | list | 1 | ratemaking, Canada |
| RG9 | Where in [document edition] is [requirement] stated? | V | value (locator) | 1 | MCT guideline 2024, supervisory target MCT ratio |
| RG10 | Which rating variables are prohibited for [line] in [jurisdiction] on [date]? | V | list | 2 | private passenger auto, Ontario, 2026-01-01 |
| RG11 | Which regulatory changes affected [line] in [jurisdiction] between [date] and [date], in date order? | V | list | 2 | personal auto, Ontario, 2010 to 2025 |
| RG12 | Which disclosure requirements does [standard] place on [work product type]? | R | list | 2 | a CIA standard, a rate filing's actuarial report |
| RG13 | Which documents does [document] cite? | V | list | 3 | AIRB Filing Guidelines (2025) |
| RG14 | Which documents cite [document]? | V | list | 3 | OSFI's MCT guideline |

### 3.4 Published figures (FG)

| ID | Question | Type | Answer | Pri | Test case |
|---|---|---|---|---|---|
| FG1 | What [quantity kind] did [organization] report for [period]? | V | value | 1 | MCT ratio, Intact Insurance Company, the quarter ending 2025-12-31 |
| FG2 | What is the [quantity kind] in [document edition] for [line]? | V | value | 1 | ULAE factor, GISA's 2025 exhibit, private passenger automobile (one value per accident year held) |
| FG3 | What value of [quantity kind] does [body] prescribe for [line] in [jurisdiction], effective [date]? | V | value | 1 | profit provision, AIRB, private passenger automobile, Alberta, 2026-10-01 |
| FG4 | At which locator (document edition, then page, table or cell) is [figure] stated? | V | value | 1 | GISA's ULAE factor for accident year 2025 |
| FG5 | In what unit is [figure] stated? | V | value | 1 | the AIRB's profit provision |
| FG6 | On which basis is [figure] stated (accident, policy or calendar year; gross or net; written or earned)? | V | value | 1 | GISA's ULAE factor for accident year 2025 (the wiki holds no filed loss ratio, the case first drafted) |
| FG7 | What is the fact-check status of [figure]? | V | value | 1 | the AIRB's profit provision |
| FG8 | Which figures come from a document edition that has been replaced? | V | list | 1 | the whole fixture |
| FG9 | What were [organization]'s [quantity kind] values for each period from [period] to [period]? | V | list | 2 | combined ratio, one insurer, five years |
| FG10 | Which organizations reported [quantity kind] below [threshold] for [period]? | V | list | 2 | MCT ratio, 200%, one quarter |

### 3.5 Actuarial work (WK)

The ratemaking and reserving chain. The first group describes methods and tools in general; the
second describes one piece of work and what it rests on.

**Methods and tools**

| ID | Question | Type | Answer | Pri | Test case |
|---|---|---|---|---|---|
| WK1 | What is the exposure base for [line]? | V | value | 1 | private passenger automobile (the wiki states it for personal automobile, the wider line) |
| WK2 | Which steps make up [method], in order? | R | list | 1 | the ratemaking chain |
| WK3 | Which quantity kinds does [method] take as input? | R | list | 1 | Bornhuetter-Ferguson Method |
| WK4 | Which quantity kind does [method] produce? | R | value | 1 | Bornhuetter-Ferguson Method |
| WK5 | Which methods produce [quantity kind]? | R | list | 1 | ultimate claims |
| WK6 | Which tools implement [method]? | R | list | 1 | Bornhuetter-Ferguson Method |
| WK7 | Which tools accept [quantity kind] as an input? | R | list | 1 | loss trend |
| WK8 | Which tools can supply an input of [tool]? | R | list | 1 | Trend Factor |
| WK9 | Which components make up [quantity kind]? | R | list | 1 | unpaid claims |
| WK10 | Which period bases can a claim be assigned on? | S | list | 2 | (accident, policy, report, calendar year) |
| WK11 | Which methods estimate [quantity kind] from [data kind]? | R | list | 2 | credibility, claim counts |

**One analysis**

| ID | Question | Type | Answer | Pri | Test case |
|---|---|---|---|---|---|
| WK12 | Which assumptions does [analysis] use? | V | list | 1 | the synthetic rate indication |
| WK13 | What is the source of [assumption]? | V | value | 1 | the AIRB's profit provision |
| WK14 | Was [assumption] prescribed, published or selected? | V | value | 1 | each assumption of the synthetic rate indication |
| WK15 | Who selected [assumption]? | V | value | 1 | the synthetic selected trend |
| WK16 | What rationale is recorded for [assumption]? | V | value | 2 | the same |
| WK17 | Which analyses use [assumption]? | V | list | 1 | the AIRB's profit provision |
| WK18 | Which data sets did [analysis] use? | V | list | 1 | the synthetic rate indication |
| WK19 | Which method did [analysis] use for [step]? | V | value | 1 | the synthetic rate indication, the last step of the ratemaking chain |
| WK20 | Which development factors did [analysis] apply? | V | list | 2 | synthetic |
| WK21 | From which date to which date was [trend factor] applied? | V | value | 2 | synthetic |
| WK22 | What is the complement of credibility in [analysis]? | V | value | 2 | synthetic |
| WK23 | Which expense provisions enter [indication]? | V | list | 2 | synthetic |
| WK24 | Which triangles exist for [segment] at [valuation date]? | V | list | 2 | synthetic |
| WK25 | Which analysis produced [estimate]? | V | value | 1 | the synthetic indicated rate change |
| WK26 | Who reviewed [work product]? | V | list | 2 | synthetic |
| WK27 | Which rate filing contains [indication]? | V | value | 3 | synthetic |
| WK28 | With which body was [filing] filed? | V | value | 3 | synthetic |

### 3.6 Events (EV)

| ID | Question | Type | Answer | Pri | Test case |
|---|---|---|---|---|---|
| EV1 | Which catastrophe events occurred in [jurisdiction] between [date] and [date]? | V | list | 1 | Ontario, 2025-01-01 to 2025-12-31 (the wiki's catastrophe pages cover Ontario and Quebec, not Alberta, the case first drafted) |
| EV2 | Which peril caused [event]? | V | value | 1 | the Ontario and Quebec ice storm of March 2025 |
| EV3 | What insured-loss estimates exist for [event]? | V | list | 1 | the Ontario and Quebec ice storm of March 2025 |
| EV4 | Which body published [estimate]? | V | value | 1 | the final estimate for the ice storm |
| EV5 | As of what date was [estimate] made? | V | value | 2 | the same |
| EV6 | Which lines of business did [event] affect? | V | list | 2 | 2024 Calgary hailstorm |
| EV7 | Which regulatory changes followed from [event]? | V | list | 3 | one sourced case from the wiki |
| EV8 | Which claims on [portfolio] arose from [event]? | V | list | 3 | synthetic |

### 3.7 Policies and coverage (PC)

| ID | Question | Type | Answer | Pri | Test case |
|---|---|---|---|---|---|
| PC1 | Which coverages does [policy form] include? | V | list | 2 | Ontario Automobile Policy (OAP 1) |
| PC2 | Which coverages are mandatory for [line] in [jurisdiction] on [date]? | V | list | 2 | private passenger auto, Ontario, 2026-01-01 |
| PC3 | Which exclusions apply to [coverage] in [policy form]? | V | list | 3 | one OAP 1 coverage |
| PC4 | What limit applies to [coverage] on [policy]? | V | value | 3 | synthetic |
| PC5 | What deductible applies to [coverage] on [policy]? | V | value | 3 | synthetic |
| PC6 | Which claims on [portfolio] were caused by a natural peril? | V | list | 3 | synthetic |

---

## 4. Scenarios

Chains of questions for the end-to-end test, run once with the Coworker and once with a person.
Each step uses the answer to the one before.

| Scenario | Chain |
|---|---|
| A new capital guideline | RG1 → RG3 → RG4 → FG8 |
| An Alberta auto rate filing | RG6 → RG7 → FG3 → FG4 → FG7 |
| Tracing an indication | WK25 → WK12 → WK14 → WK13 → FG8 |
| Choosing a reserving method | WK5 → WK3 → WK6 → WK8 |
| After a catastrophe | EV1 → EV3 → EV4 → EV6 |
| Peer benchmarking | IN8 → FG1 → FG9 → FG10 |

---

## 5. Terms the questions presuppose

Each question assumes certain types exist and are connected. This is the candidate term list for
0.8, read off the priority 1 questions; nothing else goes in.

| Module | Types | Relationships and attributes |
|---|---|---|
| Shared core | Party (Organization, Person), Role assignment, Jurisdiction, Line of business, Document, Document edition, Locator, Period, Unit, Quantity kind, Observation, Term (glossary) | holds role, in jurisdiction, for line, valid from and to, edition of, replaces, stated at, about, for period, on basis, in unit, fact-check status, synonym, defined on page |
| Institutions | Role types: insurer, reinsurer, regulator, rating board, statistical agency, professional body. Regulatory domain | regulates for domain, publishes, authority covers |
| Regulation | Normative document (statute, regulation, guideline, standard, filing rule), Requirement | issued by, applies to role, applies to activity, effective from and to |
| Actuarial work | Method, Step, Tool, Analysis, Assumption, Data set, Estimate, Work product | has step in order, takes input, produces, implements, uses, selected by, status (prescribed, published, selected), source |
| Events | Event (catastrophe, regulatory, corporate), Peril | occurred on, located in, caused by, estimate of |

Policies and coverage have no priority 1 question, so they add no terms until a priority 2
question is taken up.

---

## 6. From question to test

Each priority 1 question has a query in `tests/queries/<ID>.rq` and its expected result in
`tests/expected/<ID>.txt`. A question tested on two cases has a second file (`FD1-no`). The
queries run on three fixtures in `tests/fixtures/`:

| Fixture | Holds | Source |
|---|---|---|
| `wiki.ttl` | Organizations, documents and editions, filed and published figures, one catastrophe event, method inputs and outputs | Transcribed from pages of the Actuarial Notes Wiki; each record names its page |
| `tools.ttl` | The calculators, their methods, hand-offs and chains | Generated from the wiki's calculator engine |
| `synthetic.ttl` | One invented rate indication | Invented, in its own namespace, for the questions about a single analysis |

`python3 tools/check.py` runs every query and compares, and adds two checks on the set as a
whole:

- **Presuppositions.** Every class and property a query names exists in the ontology.
- **Coverage.** Every class and property in the ontology is named by a query, or is the domain
  or range of a property that is. A term no question uses fails the build.

Some test cases differ from the ones first drafted, because the fixture holds only what the wiki
states: the test case column says where and why.

---

## 7. Later modules

| Module | Covers | Why later |
|---|---|---|
| Education | Exam, learning objective, concept, prerequisite, reading, practice question; which workflow step uses a concept from which exam | The wiki already structures this data without the ontology; the Coworker's data comes first |
| Reinsurance | Treaty and facultative contracts, layers, cessions | No open ontology covers it; it needs its own questions |
| Capital | Risk categories and measures under the MCT | Follows the regulation module |
| Life and pensions | Mortality tables, products, plans | Outside the first scope |
| Other jurisdictions | US and European regulation | Outside the first scope |

## Sources

- Grüninger and Fox (1995), "The Role of Competency Questions in Enterprise Engineering".
- Keet and Khan (2024), "Discerning and Characterising Types of Competency Questions for
  Ontologies", for the five types.
- Ren et al. (2014), "Towards Competency Question-driven Ontology Authoring", for templates and
  presuppositions.
- Poveda-Villalón et al. (2022), "LOT: An industrial oriented ontology engineering framework",
  for the requirements specification and test suite.
- The FIBO ontology guide, for the coverage rule.
