# Actuarial Ontology (AO)
Welcome! This is the home of an open source project to develop **an ontology for the domain of actuarial science**.
- [Actuarial Ontology (.ttl)](https://github.com/Actuarial-Notes/Actuarial-Ontology/blob/main/actuarial-ontology.ttl)
- [Documentation](https://github.com/Actuarial-Notes/Actuarial-Ontology/blob/main/AO-Documentation.md)

**Example** [Canadian P&C Insurance Knowledge Base.ttl](https://github.com/Actuarial-Notes/Actuarial-Ontology/blob/main/canadian-pc-insurance-knowledge-base.ttl)

> **Actuarial science** is the discipline of measuring and managing financial risk.
>

👉 Check out our [Project Guide](https://github.com/Actuarial-Notes/Actuarial-Ontology/blob/main/Project%20Guide.md) and [Code of Conduct](https://github.com/Actuarial-Notes/Actuarial-Ontology/blob/main/Code%20of%20Conduct.md) if you're interested in contributing!

---

## What's an Ontology?
> An **Ontology** defines a set of representational primitives with which to model a domain of knowledge or discourse.
> - [📄 Tom Gruber - Definition of Ontology (2008)](https://tomgruber.org/writing/definition-of-ontology/)
>




## Why create an ontology?
> "In a sample of 100 companies, it was found that 63 companies who reported operating profit in the financial statements used **at least nine different definitions.**"
> - [📄 Consolidating economic exchange ontologies for financial reporting standard setting](https://www.sciencedirect.com/science/article/pii/S0169023X23000083#fn2) - 2023 - Data & Knowledge Engineering

Actuarial science has a large body of terminology that is used in day-to-day practice. Official actuarial standards provide common definitions, however the precise meaning of words such as "claim" or "risk" can still differ signficiantly between different practice areas or products.

Ontologists call these terms "overloaded"; a term with more than one definition. Multiple meanings introduces challenges when communicating in adjacent contexts such as legal, sales, or finance. Effectively conveying meaning is a challenge both for humans and artificial agents.

### Benefits of an ontology
With these challenges as context, this project to develop an Actuarial Ontology has 3 targeted benefits:
1. **Improve communication** of actuarial concepts between actuaries and other agents.
2. Use the ontology to build a coherent actuarial knowledge base that can **answer questions about real-world entities.**
3. Use the ontology and knowledge base to develop artificial intelligence **agents that can perform actuarial tasks.**


### 1. Communication
The formal language used within the actuarial practice is primarily defined by regional professional associations that produce standards of practice. Here is an incomplete list of standards:

- Actuarial Standards Board's (ASB) [Actuarial Standards of Practice ](http://www.actuarialstandardsboard.org/standards-of-practice/) (ASOPs)
- Actuarial Association of Europe's (AAE) [Europeean Standards of Actuarial Practice](https://actuary.eu/about-the-aae/european-standards-of-actuarial-practice/) (ESAPs)
- International Actuarial Association's (IAA) [International Standards of Actuarial Practice](https://www.actuaries.org/iaa/IAA/Publications/ISAPs/IAA/Publications/05ISAPs.aspx?hkey=334b21a7-a3ac-4e0e-8294-3cbc755ab14a) (ISAPs)
- Institute and Faculty of Actuaries' (IFoA) [Actuarial Profession Standards](https://actuaries.org.uk/standards/standards-and-guidance/professional-standards-directory/) (ASPs)
- Canadian Institute of Actuaries' (CIA) [Standards of Practice](https://www.cia-ica.ca/publications/standards-of-practice) (SOPs) 

Additionally, actuaries are qualified by professional organizations that manage educational requirements and conduct: 
- Society of Actuaries (SOA): [Syllabus](https://www.soa.org/education/exam-req/edu-fsa-req/), [Competency Framework](https://www.soa.org/professional-development/competency-framework/), [Code of Conduct](https://www.soa.org/about/governance/about-code-of-professional-conduct/)
- Casualty Actuarial Society (CAS): [Syllabus](https://www.casact.org/credential-requirements), [Capability Model](https://www.casact.org/professional-education/cas-capability-model), [Code of Conduct](https://www.casact.org/exams-admissions/resources/principles-and-policies-candidates)
- Institute and Faculty of Actuaries (IFoA): [Syllabus](https://actuaries.org.uk/curriculum/), [Code of Conduct](https://actuaries.org.uk/media/p3vdcokt/actuaries-code-v3-1.pdf)

Developping an actuarial ontology would begin with deconstructing the language in these standards and educational resources, then connecting them together in a coherent model. With such a model, communication would be precise and consistent between actuaries, non-actuarial professionals, organizations, governments, regulators, clients, and aritifical agents.

### 2. Knowledge Base
With an ontology in place, real-world entities can then be modelled to produce a knowledge base. The [**🧠 Actuarial Notes Wiki**](https://wiki.actuarialnotes.com/Actuarial+Notes+Wiki) is a knowledge base founded on the Actuarial Ontology.

A knowledge base is used to answer queries about the real world. "Competency Questions" are used to test ontologies and illustrate the kinds of questions that a knowledge base built on that ontology should be able to answer.
- "Which companies acquired Royal Sun Alliance (RSA)?"
- "Is this rating model compliant with regulations in California?"
- "What is the impact on our loss ratio from the 2021 Calgary, Alberta hail storm?"


### 3. Artificial Intelligence
With a knowledge base and ontology, software agents can then interact with information. For example, see Microsoft's [📄 Azure Digital Twins documentation](https://learn.microsoft.com/en-us/azure/digital-twins/concepts-ontologies) to see how an ontology can be used to build digital twin solutions.

A useful artificial intelligence for actuaries should be capable of inference and decision tasks in the following domains:
- [Risk Assessment](https://wiki.actuarialnotes.com/Tools/Techniques/Risk+Assessment)
- [Pricing](https://wiki.actuarialnotes.com/Tools/Techniques/Insurance+Pricing)
- Reserving
- Valuation
- [Investment](https://wiki.actuarialnotes.com/Concepts/Investment#Determining+Value)
- Capital Modelling
- Capital Allocation
- Regulatory Compliance
- Product Development

