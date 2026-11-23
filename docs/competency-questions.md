# Competency questions

Draft for the maintainer to edit. These questions decide what goes in the 0.8 core: a class or
property is in the core only if one of them needs it. Each will become a SPARQL test in `tests/`
with an expected result on a real, cited fixture.

## Form

Each question follows five rules.

1. **One question, one answer.** No "and". "Which regulator approves auto rates in Alberta, and
   under what filing rules?" is two questions; when it fails, nobody can say which half failed.
2. **A stated answer shape**: a list, a single value, a count, or yes/no.
3. **Parameters in [brackets].** The question is a template; the test binds it to one real case.
4. **Answerable from data.** "Is this model compliant?" needs judgement, so it is not a
   competency question. "Which requirements apply to this model?" is.
5. **Small enough for one query.** A multi-step investigation is a *scenario*: a short chain of
   questions where each uses the previous answer.

The test case for each question names real entities only. Expected answers are not written here;
they come from the fixture, which is exported from the wiki's sourced pages.

## Questions

### Regulation

| # | Question | Answer | Test case |
|---|---|---|---|
| R1 | Which normative documents issued by [issuer] are in force on [date]? | list | OSFI, 2026-01-01 |
| R2 | Which normative documents apply to [role] in [jurisdiction] for [regulatory domain] on [date]? | list | federally regulated P&C insurer, Canada, solvency, 2026-01-01 |
| R3 | Which edition of [document] is in force on [date]? | value | OSFI's MCT guideline, 2023-06-30 |
| R4 | Which document replaced [document edition]? | value | MCT guideline, 2023 edition |
| R5 | From what date is [document edition] effective? | value | MCT guideline, 2024 edition |
| R6 | Which body approves rates for [line] in [jurisdiction]? | value | private passenger auto, Alberta |
| R7 | Which filing rules apply to a rate filing for [line] in [jurisdiction] on [date]? | list | private passenger auto, Alberta, 2026-01-01 |
| R8 | Which regulatory changes affected [line] in [jurisdiction] between [date] and [date], in date order? | list | personal auto, Ontario, 2010 to 2025 |
| R9 | Which standards of practice apply to [activity] in [jurisdiction]? | list | reserve valuation, Canada |
| R10 | Which documents does [document] cite? | list | AIRB Filing Guidelines (2025) |
| R11 | Which documents cite [document]? | list | OSFI's MCT guideline |
| R12 | Where in [document edition] is [requirement] stated? | value (locator) | MCT guideline 2024, supervisory target ratio |

### Institutions

| # | Question | Answer | Test case |
|---|---|---|---|
| I1 | Which body regulates [organization] for [regulatory domain] in [jurisdiction]? | value | Intact Insurance, solvency, Canada |
| I2 | Which organizations belong to [group]? | list | Intact Financial Corporation |
| I3 | Which organization acquired [organization]? | list | RSA Canada |
| I4 | On what date did [acquisition] close? | value | the RSA acquisition |
| I5 | Which insurers are licensed for [line] in [jurisdiction] on [date]? | list | personal auto, Alberta, 2026-01-01 |
| I6 | Is [organization] federally regulated? | yes/no | Wawanesa Mutual |
| I7 | Which bodies publish [quantity kind] for [line] in [jurisdiction]? | list | loss trend benchmarks, private passenger auto, Ontario |
| I8 | Which reinsurers does [insurer] cede to under contracts in force on [date]? | list | synthetic fixture |

### Published figures

| # | Question | Answer | Test case |
|---|---|---|---|
| F1 | What [quantity kind] did [organization] report for [period]? | value | MCT ratio, one insurer, one quarter of OSFI's PC4 return |
| F2 | Which organizations reported [quantity kind] below [threshold] for [period]? | list | MCT ratio, 200%, same quarter |
| F3 | What were [organization]'s [quantity kind] values for each period from [period] to [period]? | list | combined ratio, one insurer, five years |
| F4 | What is the [quantity kind] in [document edition] for [line]? | value | ULAE factor, GISA's Ontario PPA factors (2025) |
| F5 | What value of [quantity kind] does [body] prescribe for [line] in [jurisdiction], effective [date]? | value | profit provision, AIRB, private passenger auto, Alberta |
| F6 | In which document, and where in it, is [figure] stated? | value (locator) | the figure from F4 |
| F7 | Which figures come from a document edition that has been replaced? | list | the whole fixture |
| F8 | What is the fact-check status of [figure]? | value | the figure from F5 |
| F9 | In what unit and currency is [figure] stated? | value | the figure from F5 |

### Events

| # | Question | Answer | Test case |
|---|---|---|---|
| E1 | Which catastrophe events occurred in [jurisdiction] between [date] and [date]? | list | Alberta, 2013 to 2024 |
| E2 | What insured-loss estimates exist for [event]? | list | 2016 Fort McMurray wildfire |
| E3 | Which body published [estimate], and as of what date? | value | one estimate from E2 |
| E4 | Which peril caused [event]? | value | 2020 Calgary hailstorm |
| E5 | Which lines of business did [event] affect? | list | 2024 Calgary hailstorm |
| E6 | Which regulatory changes followed from [event]? | list | one sourced case from the wiki |
| E7 | Which claims on [portfolio] arose from [event]? | list | synthetic fixture |

### Policies and coverage

| # | Question | Answer | Test case |
|---|---|---|---|
| P1 | Which coverages does [policy form] include? | list | Ontario Automobile Policy (OAP 1) |
| P2 | Which exclusions apply to [coverage] in [policy form]? | list | one OAP 1 coverage |
| P3 | Which coverages are mandatory for [line] in [jurisdiction] on [date]? | list | private passenger auto, Ontario, 2026-01-01 |
| P4 | What limit applies to [coverage] on [policy]? | value | synthetic fixture |
| P5 | What deductible applies to [coverage] on [policy]? | value | synthetic fixture |
| P6 | Which claims on [portfolio] were caused by a natural peril? | list | synthetic fixture |

### Actuarial work

| # | Question | Answer | Test case |
|---|---|---|---|
| A1 | Which assumptions does [analysis] use? | list | synthetic rate indication |
| A2 | What is the source of [assumption]? | value | one assumption from A1 |
| A3 | Which tools accept [quantity kind] as an input? | list | annual loss trend |
| A4 | Which tools implement [method]? | list | Bornhuetter-Ferguson |
| A5 | Which model produced [estimate]? | value | synthetic fixture |
| A6 | Who reviewed [work product]? | list | synthetic fixture |
| A7 | Which concept page defines [term]? | value | "IBNR" |
| A8 | Which terms are synonyms of [term]? | list | "unpaid claim liability" |

## Scenarios

Chains for the end-to-end test with the Coworker (and with a person, for comparison).

- **A new capital guideline.** R1 → R3 → R4 → F7: what is in force, what it replaced, which
  figures in use now rest on the old edition.
- **An Alberta auto rate filing.** R6 → R7 → F5 → F6 → F8: who approves, under which rules, what
  is prescribed, where it is stated, whether it has been checked.
- **After a catastrophe.** E1 → E2 → E3 → E5 → E7: which events, whose estimates, which lines,
  which of our claims.
- **Peer benchmarking.** I5 → F1 → F3 → F2: who writes the line, what they filed, how it moved,
  who is below a threshold.

## Out of scope for 0.8

Life insurance, pensions, US regulation, and anything needing judgement or calculation (a
calculation is a tool's job; the ontology only says which tool takes what).
