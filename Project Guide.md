# 📕 Project Guide
This **project guide** defines _how_ the Actuarial Ontology is developed.
1. Examples
2. Design Principles
3. Steps
4. Software
5. Best Practices
6. Sources


## 1. Examples
Examples and templates are available from the [Ontology Design Patterns](http://ontologydesignpatterns.org/wiki/Main_Page.) (ODPs) Wiki. ODPs are **reusable successful solutions to a recurrent modeling problem**.

To see what a good final product looks like, take a look at their [Exemplary Ontologies](http://ontologydesignpatterns.org/wiki/Ontology:Main).


## 2. Design Principles

In their Ontology 101 guide, Stanford's Protégé group suggests 3 fundamental rules of ontology design:

> 1) There is **no one correct way** to model a domain— there are always viable alternatives. The best solution almost always depends on the application that you have in mind and the extensions that you anticipate. 
>
> 2) Ontology development is necessarily an **iterative process.** 
>
> 3) Concepts in the ontology should be **close to objects** (physical or logical) and relationships in your domain of interest. These are most likely to be nouns (objects) or verbs (relationships) in sentences that describe your domain.


## 3. Steps
The [Ontology Development 101](https://protege.stanford.edu/publications/ontology_development/ontology101.pdf) guide defines 8 steps in building an ontology:
1. Decide **domain** and **scope**.
2. Reuse **existing ontologies**.
3. Enumerate **terms**.
4. Define **classes** and **class hierarchy**.
5. Define the **properties** of classes (slots).
6. Define the **facets** of slots.
7. Create **instances**.
8. Test **consistency** and **coherency**.


## 4. Software
All software used in this project is open source and free.
- **Languages**: Ontology Web Language (OWL), OntoUML
- **Upper Ontology**: Unified Foundational Ontology (UFO)
- **Development Software**: Protégé
- **Testing Software**: Fact++ (Reasoner)
- **Project Management**: Open Source Guide


## 5. Best Practices
The following is a tiny excerpt of a extensive list of practical tips offered by [Michael K. Bergman's Reference Guide to Ontology Best Practices](https://www.mkbergman.com/911/a-reference-guide-to-ontology-best-practices/)

1. Balance breadth and depth of scope (roughly equal)
2. Reuse structure and vocabularies as much as possible (internally and externally).
3. Concepts are single nouns (like "Person")
4. Properties are verbs that can be read as a triple (like "hasProperty" )
5. Everything (Concepts + Properties) needs a clear **definition**.
6. Document with flowcharts.
7. Test with reasoners to identify inconsistencies and with external knowledge bases (ex: CYC, UMBEL) to evaluate coherence.
8. Definitions should look like this: "A is a B that C", Where B is the "parent term" of A in the ontology, and C is what uniquely differentiates As from Bs.
   Example: A square [A] is a rectangle  [B] that has equal side lengths [C].



## 6. Sources
1. An [Ontology Development 101](https://protege.stanford.edu/publications/ontology_development/ontology101.pdf) guide from Noy and McGuinness at Stanford.
2. The [User Guide](https://protegewiki.stanford.edu/wiki/Pr4_UG_mi_Outline) for the ontology modelling software Protégé.
3. [A Reference Guide to Ontology Best Practices](https://www.mkbergman.com/911/a-reference-guide-to-ontology-best-practices/) by Michael K. Bergman.
4. The [Wiki for Ontology Designs Patterns](http://ontologydesignpatterns.org/wiki/Main_Page.).
5. [CUBRC - 2016 - Best Practices of Ontology Development](https://www.nist.gov/system/files/documents/2021/10/14/nist-ai-rfi-cubrc_inc_002.pdf)
6. [Gruber's view on Ontology (1992)](http://www-ksl.stanford.edu/kst/what-is-an-ontology.html) 
