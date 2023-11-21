# Actuarial Ontology (AO)
Welcome! This is the home of an open source project to develop an ontology for the domain of actuarial science.

> An **ontology** is a formal language that describes concepts and relationships within a domain of knowledge.

> **Actuarial science** is a discipline that quantifies risk and makes decisions about the redistribution of risk among groups.

## Why create an ontology?
Actuarial science has a lot of specific terminology. While actuarial standards provide definitions, the meaning of words can still differ between practice areas or products. Additionally, other professions may use the same "actuarial" word with a different meaning that's specific to their domain.

This lack of consistent meaning introduces challenges when communicating actuarial information in different contexts like law, regulation, finance, and even with other actuaries.

Effectively conveying meaning is a challenge both for humans and artificial agents.

With these challenges as context, this project has 3 targeted benefits:
1. Improve communication of actuarial concepts between actuaries and other agents.
2. Use the ontology to build an actuarial knowledge base of real-world entities.
3. Use the ontology and knowledge base to develop artificial agents that can perform actuarial tasks.


### 1. Communication
The formal language used within the actuarial practice is primarily defined by regional professional associations that produce standards of practice. Here is an incomplete but representative list of standards:

- Actuarial Standards Board's (ASB) [Actuarial Standards of Practice ](http://www.actuarialstandardsboard.org/standards-of-practice/) (ASOPs)
- Actuarial Association of Europe's (AAE) [Europeean Standards of Actuarial Practice](https://actuary.eu/about-the-aae/european-standards-of-actuarial-practice/) (ESAPs)
- International Actuarial Association's (IAA) [International Standards of Actuarial Practice](https://www.actuaries.org/iaa/IAA/Publications/ISAPs/IAA/Publications/05ISAPs.aspx?hkey=334b21a7-a3ac-4e0e-8294-3cbc755ab14a) (ISAPs)
- Institute and Faculty of Actuaries's (IFoA) [Actuarial Profession Standards](https://actuaries.org.uk/standards/standards-and-guidance/professional-standards-directory/) (ASPs)

Additionally, actuaries are qualified by professional organizations that manage educational requirements and conduct: 
- Society of Actuaries (SOA): [Syllabus](https://www.soa.org/education/exam-req/edu-fsa-req/), [Competency Framework](https://www.soa.org/professional-development/competency-framework/), [Code of Conduct](https://www.soa.org/about/governance/about-code-of-professional-conduct/)
- Casualty Actuarial Society (CAS): [Syllabus](https://www.casact.org/credential-requirements), [Capability Model](https://www.casact.org/professional-education/cas-capability-model), [Code of Conduct](https://www.casact.org/exams-admissions/resources/principles-and-policies-candidates)
- Institute and Faculty of Actuaries (IFoA): [Syllabus](https://actuaries.org.uk/curriculum/), [Code of Conduct](https://actuaries.org.uk/media/p3vdcokt/actuaries-code-v3-1.pdf)

An actuarial ontology would begin with deconstructing the language in these standards and educational resources, then connect them together in a coherent model. With such a model, communication would be precise and consistent between actuaries, non-actuarial professionals, organizations, clients, and aritifical agents.

### 2. Knowledge Base
With an ontology in place, real-world entities can then be modelled to produce a knowledge base. Here are some examples of the kinds of entities that an actuarial ontology should be able to "talk about":
- Insurance company
- Pension Plan
- Regulator
- Insurance Product
- Value
- Model
- Catastrophe
- Actuarial Opinion
- ...

### 3. Artificial Intelligence
With a knowledge base and ontology, software agents can then interact with information. For example, see Microsoft's [Azure Digital Twins documentation](https://learn.microsoft.com/en-us/azure/digital-twins/concepts-ontologies) to see how an ontology can be used to build digital twin solutions.

A useful artificial intelligence for actuaries should be capable of inference and decision tasks in:
- Pricing
- Reserving
- Valuation
- Capital modelling and allocation
- Regulatory compliance
- Product development
- ...
