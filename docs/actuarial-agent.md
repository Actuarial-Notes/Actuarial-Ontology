# The Actuarial Ontology as an Agent Foundation

_Last updated: 2026-07-22_

This document explains how the Actuarial Ontology serves as the **semantic foundation for an
Actuarial Agent** — the AI "agents that can perform actuarial tasks" named as benefit #3 in
the project README. It is the ontology-side companion to the full product plan, which lives in
the knowledge-base repo:

> **Full product plan:** `Actuarial-Notes-Wiki/docs/actuarial-agent-product-plan.md`

Read that for the product vision, personas, phases, and governance. This note covers only what
the Agent needs *from the ontology*, and what the ontology should add to serve it.

---

## 1. Why the ontology, not just an LLM

A general LLM is a fluent but ungrounded actuary. It will confidently misuse an overloaded term
("claim", "risk", "reserve" mean different things across practice areas — the exact problem
this project's README opens with), invent an ASOP citation, or blur jurisdictions.

The ontology is the Agent's defense against that failure mode. It provides:

1. **Disambiguation.** ~320 classes with "A is a B that C" definitions let the Agent resolve a
   user's word to a *specific sense* before answering, instead of guessing. This is the Agent's
   single most important differentiator over a general chatbot.
2. **Structure to reason over.** The class hierarchy (`subClassOf`) and object properties
   (`covers`, `triggeredBy`, `hasReserve`, `manages`, `exposedTo`, …) give the Agent a graph to
   traverse — for both retrieval (pull ontology-neighbors, not just text-similar chunks) and
   inference (is a `CatastropheExcessOfLoss` a `NonProportionalReinsurance`? yes, by the
   taxonomy).
3. **Standards-awareness.** `asopReference` annotations and the ASOP 41 communication framework
   (`ActuarialCommunication`, `ActuarialOpinion`, `Disclosure`, `IntendedUser`) let the Agent
   cite the governing standard and recognize when a request crosses into governed territory.
4. **A correctness contract.** The competency questions define what a KB built on this ontology
   *should* be able to answer — which is exactly what an Agent's evaluation harness needs.

The knowledge base supplies the *facts* (the wiki concept/exam pages, the question bank, and
the `canadian-pc-insurance-knowledge-base.ttl` instances); the ontology supplies the *meaning*
and the *structure*. The Agent is the accountable layer that joins them.

---

## 2. Competency questions = the Agent's evaluation harness

The most valuable thing the ontology already gives the Agent is its **competency questions**
(see `AO-Documentation.md` §"Competency Questions" — risk management, insurance operations,
financial analysis, actuarial processes, regulatory compliance). The documentation reports
**100% answerability at the schema level** — i.e. the ontology *can express* every competency
question.

The Agent needs the next step: **answer quality**, not just answerability. So the competency
questions become a **shared, versioned eval suite** co-owned by both repos:

- The ontology proves a question is *expressible* (schema coverage — already at 100%).
- The Agent is measured on whether it *answers it correctly, with citations* (grounding,
  factuality, faithfulness, term precision — see the product plan §7).

This suite is the single clearest signal of whether benefit #3 is being delivered. It should be
expanded well beyond the current seed set, versioned alongside the ontology, and treated as the
**contract test** that catches drift between the ontology, the wiki's `ontology_map.py`, and
the Agent's behavior.

**Recommendation:** add a machine-readable competency-question set to this repo (e.g.
`competency-questions/` with each question, its expected ontology classes/properties, and — once
the instance KB supports it — a reference SPARQL query and expected answer). That turns a
documentation section into a runnable eval.

---

## 3. What the Agent needs the ontology to add

These are the ontology's own "Future Development" items (AO-Documentation §"Status and Next
Steps"), now **demand-driven by the Agent** and roughly in the order the Agent's phases need
them:

| Need | Why the Agent needs it | Product-plan phase gated |
|------|------------------------|--------------------------|
| **SPARQL query library** | The Agent's graph/entity query tool answers "which perils are excluded?", "which insurers write X?" from *facts*, not prose. Reusable query patterns are its toolset. | Phase B (instance-KB query path) |
| **SHACL shapes / formal constraints** (domain/range, cardinality, disjointness) | Validation the Agent's graph tool relies on to trust the KB, and to catch malformed instances before they produce a wrong answer. | Phase B |
| **Expanded instance KB** beyond Canadian P&C | The Agent can only answer entity questions where instances exist. Domain/jurisdiction breadth is capped by the instance KB. | Phase D (broaden domains) |
| **FIBO / schema.org mappings** | Interoperability — lets the Agent connect to external financial data and be embedded in other systems. | Phase D (proprietary-data grounding) |
| **Property chains & advanced axioms** | Lets a reasoner infer relationships the Agent would otherwise have to be told, improving graph-biased retrieval and inference. | Phase B/C |
| **Multilingual labels** (e.g. French) | Canadian P&C is bilingual; regulator/practitioner personas may need French. | Later |

The ordering matters: **SPARQL + SHACL are the near-term blockers** (they gate the Agent's
Phase B, where it moves from "explains concepts" to "answers questions about real-world
entities"). The instance-KB expansion and external mappings are later, gating domain breadth.

---

## 4. The bridge to the knowledge base

The runtime bridge between free-text user language and the ontology already exists on the
knowledge-base side and must stay in sync:

- `Actuarial-Notes-Wiki/scripts/ontology_map.py` — the canonical topic→concept→learning-objective
  map that ties wiki content to ontology terms.
- `Actuarial-Notes-Wiki/quiz/src/lib/conceptMatch.ts` (`slugForLink`) — resolves concept name
  variants/aliases to a canonical slug at runtime.

The Agent's term-resolution step (product plan §5, step 1) sits on top of these plus an ontology
term index. **Keeping the ontology, `ontology_map.py`, and `conceptMatch` aligned is a
correctness requirement** — the shared competency-question suite (§2) is the test that enforces
it. Drift between them is one of the named product risks.

---

## 5. Summary

The ontology is not a supporting artifact for the Agent — it is the Agent's semantic core and
its evaluation contract. The concrete asks of this repo, in priority order:

1. **Promote the competency questions to a runnable, versioned eval suite** (§2) — the shared
   asset that proves benefit #3.
2. **Build the SPARQL query library and SHACL shapes** (§3) — the near-term blockers for the
   Agent's entity-reasoning phase.
3. **Grow the instance KB** beyond Canadian P&C (§3) — the cap on the Agent's domain breadth.
4. **Keep the ontology↔KB bridge aligned** (§4) — enforced by the eval suite.

See `Actuarial-Notes-Wiki/docs/actuarial-agent-product-plan.md` for the full plan.
