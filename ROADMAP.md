# Actuarial Ontology Development Roadmap

**Version:** 1.0
**Last Updated:** January 2026
**Current Ontology Version:** 0.7.0

This roadmap outlines the strategic development plan for the Actuarial Ontology project, organized into multiple phases with clear objectives and deliverables.

---

## Executive Summary

The Actuarial Ontology has achieved significant maturity with 301 classes, 110 properties, and 100% competency question answerability. This roadmap charts the path from a well-structured knowledge representation to a comprehensive, industry-standard semantic framework with validation, tooling, and broad adoption.

### Development Phases Overview

| Phase | Focus Area | Key Outcomes |
|-------|-----------|--------------|
| **Phase 1** | Validation & Constraints | SHACL shapes, axioms, data quality rules |
| **Phase 2** | Knowledge Base Expansion | Life, Health, Pensions knowledge bases |
| **Phase 3** | Tooling & Integration | SPARQL library, FIBO mapping, APIs |
| **Phase 4** | Advanced Semantics | Reasoning rules, property chains, inference |
| **Phase 5** | Internationalization | Multi-language support, jurisdictional variants |
| **Phase 6** | Community & Governance | Standards body engagement, governance model |

---

## Phase 1: Validation & Formal Constraints

**Objective:** Establish robust data quality validation and formal semantic constraints to ensure knowledge base consistency and correctness.

### 1.1 SHACL Shape Development

**Goal:** Create comprehensive SHACL (Shapes Constraint Language) shapes for all major classes.

#### Deliverables:

1. **Core Entity Shapes**
   - `InsuranceCompanyShape` - Required properties (name, regulatoryID), cardinality constraints
   - `InsuredEntityShape` - Policyholder validation rules
   - `ActuaryShape` - Professional qualification constraints
   - `PolicyShape` - Required coverage, premium, and date validations

2. **Financial Shapes**
   - `ClaimShape` - Amount validation, date sequence constraints (occurrence < reporting < settlement)
   - `ReserveShape` - Non-negative amounts, reserve type classification
   - `PremiumShape` - Premium component validations (gross >= net)
   - `MetricShape` - Ratio bounds (e.g., combined ratio typically 0-200%)

3. **Risk Shapes**
   - `RiskShape` - Risk classification validation
   - `CatastropheEventShape` - Location, severity, peril type requirements
   - `ExposureShape` - Exposure unit and value constraints

4. **Regulatory Shapes**
   - `RegulatoryReportShape` - Filing date, jurisdiction, format requirements
   - `CapitalRequirementShape` - SCR/MCR relationship constraints

#### Implementation Structure:
```
/shapes/
  core-shapes.ttl          # Core entity shapes
  financial-shapes.ttl     # Financial and claims shapes
  risk-shapes.ttl          # Risk management shapes
  regulatory-shapes.ttl    # Compliance shapes
  product-shapes.ttl       # Insurance product shapes
```

### 1.2 OWL Axiom Enhancement

**Goal:** Add formal OWL axioms for logical consistency and reasoning support.

#### Deliverables:

1. **Disjointness Axioms**
   - `InsurableRisk disjointWith UninsurableRisk`
   - `ProportionalReinsurance disjointWith NonProportionalReinsurance`
   - `DefinedBenefit disjointWith DefinedContribution`
   - `PaidClaim disjointWith OutstandingClaim`
   - Product type disjointness (Life vs P&C vs Health)

2. **Cardinality Constraints**
   - `Policy hasInsurer exactly 1 InsuranceCompany`
   - `Claim hasPolicy exactly 1 Policy`
   - `InsuranceCompany hasRegulator min 1 Regulator`

3. **Domain/Range Refinements**
   - Strengthen existing property constraints
   - Add inverse property definitions where missing
   - Define functional properties (e.g., `policyNumber`)

4. **Class Equivalence & Subsumption**
   - Define equivalent class expressions where appropriate
   - Establish complete subclass hierarchies

### 1.3 Data Quality Rules

**Goal:** Implement ASOP 23-aligned data quality validation rules.

#### Deliverables:

1. **Completeness Rules**
   - Required field validation per entity type
   - Reference data completeness checks

2. **Consistency Rules**
   - Cross-entity consistency validation
   - Temporal consistency (date sequences)
   - Hierarchical consistency (portfolio → policy → claim)

3. **Reasonableness Rules**
   - Range checks for financial values
   - Statistical outlier detection rules
   - Premium-to-exposure ratio bounds

---

## Phase 2: Knowledge Base Expansion

**Objective:** Develop comprehensive knowledge bases across all major actuarial domains beyond the existing Canadian P&C example.

### 2.1 Life Insurance Knowledge Base

**Goal:** Create a detailed life insurance knowledge base demonstrating life-specific concepts.

#### Deliverables:

1. **Product Instances**
   - Term life policies (10, 20, 30-year terms)
   - Whole life with dividend illustrations
   - Universal life with COI and crediting rates
   - Variable life with separate account structures
   - Index-linked products

2. **Mortality & Longevity Data**
   - Sample mortality tables (SOA tables)
   - Age/gender/smoker classification examples
   - Improvement scale illustrations

3. **Policyholder Behavior**
   - Lapse rate examples by duration
   - Surrender value calculations
   - Policy loan utilization patterns

4. **Reserves & Valuation**
   - Statutory reserve calculations
   - GAAP/IFRS 17 reserve examples
   - Embedded value demonstrations

5. **Life-Specific Scenarios**
   - New business pricing examples
   - In-force management illustrations
   - Reinsurance arrangements (YRT, coinsurance)

### 2.2 Health Insurance Knowledge Base

**Goal:** Develop health insurance domain coverage including medical, disability, and long-term care.

#### Deliverables:

1. **Product Types**
   - Medical expense insurance
   - Disability income (short-term, long-term)
   - Long-term care insurance
   - Critical illness coverage
   - Supplemental health products

2. **Claims & Utilization**
   - Medical claims with diagnosis codes
   - Disability claim duration patterns
   - Long-term care benefit triggers

3. **Morbidity Data**
   - Incidence rate examples
   - Continuance/termination rates
   - Recovery and mortality in disabled state

4. **Healthcare-Specific Concepts**
   - Provider networks
   - Managed care arrangements
   - Prescription drug coverage tiers

### 2.3 Pension & Retirement Knowledge Base

**Goal:** Cover employer-sponsored retirement plans and individual retirement products.

#### Deliverables:

1. **Plan Types**
   - Defined benefit plans (final average, career average)
   - Defined contribution plans (401k, 403b equivalents)
   - Cash balance plans
   - Hybrid arrangements

2. **Actuarial Valuations**
   - Funding valuations with sample assumptions
   - Accounting valuations (ASC 715, IAS 19)
   - Asset-liability studies

3. **Participant Data**
   - Census data examples
   - Service and compensation patterns
   - Benefit accrual illustrations

4. **Regulatory Examples**
   - Funding requirement calculations
   - PBGC premium illustrations
   - Disclosure requirements

### 2.4 Reinsurance Knowledge Base

**Goal:** Detailed reinsurance structures and transactions.

#### Deliverables:

1. **Treaty Structures**
   - Quota share with sliding scale commissions
   - Surplus treaties with line limits
   - Excess of loss with reinstatement provisions
   - Aggregate stop loss

2. **Retrocession**
   - Retrocession arrangements
   - Catastrophe bond structures
   - Industry loss warranties

3. **Financial Analysis**
   - Ceding commission calculations
   - Loss corridor provisions
   - Profit commission mechanics

---

## Phase 3: Tooling & Integration

**Objective:** Develop practical tools and integrate with external standards to maximize ontology utility.

### 3.1 SPARQL Query Library

**Goal:** Create a comprehensive library of reusable SPARQL queries for common actuarial analyses.

#### Deliverables:

1. **Risk Analysis Queries**
   - Exposure aggregation by peril type
   - Risk concentration analysis
   - Correlated risk identification
   - Emerging risk detection

2. **Financial Queries**
   - Loss ratio calculation by line of business
   - Reserve adequacy analysis
   - Premium trend analysis
   - Combined ratio decomposition

3. **Claims Queries**
   - Claims triangle generation
   - Large loss identification
   - Claims development patterns
   - IBNR estimation support

4. **Regulatory Queries**
   - Capital requirement calculation
   - Solvency ratio monitoring
   - Compliance status reporting

5. **Portfolio Queries**
   - Portfolio composition analysis
   - Concentration risk assessment
   - Retention analysis

#### Implementation Structure:
```
/queries/
  risk-analysis/
    exposure-aggregation.rq
    concentration-analysis.rq
    correlated-risks.rq
  financial-analysis/
    loss-ratio.rq
    combined-ratio.rq
    premium-trends.rq
  claims-analysis/
    triangle-generation.rq
    development-patterns.rq
    large-loss-identification.rq
  regulatory/
    capital-requirements.rq
    solvency-monitoring.rq
  portfolio/
    composition.rq
    concentration.rq
```

### 3.2 External Ontology Mapping

**Goal:** Establish formal mappings to major financial and industry ontologies.

#### Deliverables:

1. **FIBO (Financial Industry Business Ontology) Mapping**
   - Map core financial concepts
   - Align legal entity representations
   - Connect contract structures
   - Harmonize temporal concepts

2. **Schema.org Alignment**
   - Map organizations and people
   - Connect product concepts
   - Enable web discoverability

3. **Insurance Industry Standards**
   - ACORD data model alignment
   - NAIC reporting taxonomy mapping
   - Lloyd's market standards connection

4. **Risk Standards**
   - COSO ERM framework alignment
   - ISO 31000 risk management concepts
   - Basel framework connections (operational risk)

#### Implementation:
```
/mappings/
  fibo-mapping.ttl
  schema-org-mapping.ttl
  acord-mapping.ttl
  naic-mapping.ttl
```

### 3.3 API & Application Support

**Goal:** Enable programmatic access and application integration.

#### Deliverables:

1. **REST API Specification**
   - OpenAPI/Swagger specification
   - Query endpoint definitions
   - CRUD operations for knowledge base management

2. **Python Library**
   - RDFLib-based utilities
   - Query helper functions
   - Knowledge base population tools

3. **Visualization Tools**
   - Ontology browser configuration
   - Network visualization templates
   - Dashboard components

4. **Integration Examples**
   - Jupyter notebook tutorials
   - Sample applications
   - CI/CD pipeline templates

---

## Phase 4: Advanced Semantics

**Objective:** Implement sophisticated reasoning capabilities and advanced ontological constructs.

### 4.1 Reasoning Rules

**Goal:** Develop inference rules for automated knowledge derivation.

#### Deliverables:

1. **Risk Classification Rules**
   - Automatic risk categorization based on characteristics
   - Insurability determination
   - Risk correlation inference

2. **Financial Rules**
   - Reserve adequacy inference
   - Solvency status determination
   - Profitability classification

3. **Compliance Rules**
   - Regulatory requirement determination
   - Compliance status inference
   - Deadline calculations

4. **Temporal Rules**
   - Policy status derivation (active, expired, cancelled)
   - Claim status transitions
   - Reporting period calculations

### 4.2 Property Chains

**Goal:** Define complex relationships through property composition.

#### Deliverables:

1. **Transitive Relationships**
   - `isReinsuredBy` transitivity through retrocession
   - `exposedTo` through portfolio membership
   - `regulatedBy` through jurisdictional hierarchy

2. **Composite Properties**
   - `hasUltimateLoss` = `hasClaim` o `hasUltimateCost`
   - `isAffectedByPeril` = `hasPolicy` o `covers` o `hasPeril`

### 4.3 Advanced OWL Constructs

**Goal:** Leverage OWL 2 capabilities for richer semantics.

#### Deliverables:

1. **Qualified Cardinality Restrictions**
   - "Policy with at least 2 named insureds"
   - "Reinsurance treaty with exactly 1 cedent"

2. **Self Restrictions**
   - Captive insurer definitions
   - Self-insurance constructs

3. **Keys and Identification**
   - Policy identification axioms
   - Claim uniqueness constraints
   - Entity resolution rules

4. **Negative Property Assertions**
   - Exclusion modeling
   - Non-coverage declarations

---

## Phase 5: Internationalization

**Objective:** Extend the ontology for global applicability with multi-language and multi-jurisdictional support.

### 5.1 Multi-Language Support

**Goal:** Add labels and definitions in major languages.

#### Deliverables:

1. **Primary Languages**
   - French (Canadian French priority)
   - Spanish
   - German
   - Japanese
   - Mandarin Chinese

2. **Implementation Approach**
   - `rdfs:label` with language tags
   - `rdfs:comment` translations
   - `skos:prefLabel` / `skos:altLabel` for terminology variants

3. **Translation Workflow**
   - Professional actuarial translator engagement
   - Terminology validation with local actuarial societies
   - Ongoing maintenance process

### 5.2 Jurisdictional Variants

**Goal:** Model jurisdiction-specific regulatory and practice variations.

#### Deliverables:

1. **Regulatory Frameworks**
   - US (state-based regulation, NAIC)
   - EU (Solvency II, EIOPA)
   - UK (PRA, FCA post-Brexit)
   - Canada (OSFI, provincial regulators)
   - Australia (APRA)
   - Japan (FSA)

2. **Accounting Standards**
   - US GAAP
   - IFRS 17
   - Local GAAP variants

3. **Professional Standards**
   - US ASOPs (current alignment)
   - UK TMPs (Technical Memoranda)
   - Canadian Standards of Practice
   - IAA International Standards

4. **Implementation Approach**
   - Modular jurisdiction files
   - Inheritance from core concepts
   - Clear jurisdiction tagging

#### Structure:
```
/jurisdictions/
  us/
    us-regulatory.ttl
    us-gaap.ttl
    us-asop.ttl
  eu/
    solvency2.ttl
    ifrs17.ttl
    eiopa-guidelines.ttl
  uk/
    uk-regulatory.ttl
    uk-tmps.ttl
  canada/
    canada-regulatory.ttl
    canada-standards.ttl
```

---

## Phase 6: Community & Governance

**Objective:** Build sustainable community engagement and governance structures for long-term ontology evolution.

### 6.1 Standards Body Engagement

**Goal:** Gain recognition and adoption from actuarial professional organizations.

#### Deliverables:

1. **Society of Actuaries (SOA)**
   - Present at annual meetings
   - Publish in actuarial journals
   - Engage with technology section

2. **Casualty Actuarial Society (CAS)**
   - Connect with research initiatives
   - Engage with automation/AI working groups

3. **International Actuarial Association (IAA)**
   - Present at international congress
   - Engage with ISAP development

4. **ACORD**
   - Propose alignment with ACORD standards
   - Participate in data standards initiatives

### 6.2 Governance Model

**Goal:** Establish formal governance for ontology evolution.

#### Deliverables:

1. **Governance Structure**
   - Technical steering committee
   - Domain working groups (Life, P&C, Health, Pensions)
   - Release management process

2. **Contribution Guidelines**
   - Change proposal process
   - Review and approval workflow
   - Version control procedures

3. **Maintenance Procedures**
   - Deprecation policy
   - Backward compatibility guidelines
   - Migration support

### 6.3 Education & Adoption

**Goal:** Enable broad adoption through education and support.

#### Deliverables:

1. **Educational Materials**
   - Video tutorials
   - Interactive exercises
   - Certification program concept

2. **Case Studies**
   - Implementation success stories
   - ROI documentation
   - Best practice guides

3. **Support Infrastructure**
   - Discussion forums
   - FAQ documentation
   - Implementation consulting network

---

## Implementation Priorities

### Immediate Priorities (Next Release - v0.8.0)

1. **SHACL Core Shapes** - Essential validation for existing knowledge base
2. **Disjointness Axioms** - Logical consistency foundation
3. **Life Insurance KB** - Expand domain coverage
4. **SPARQL Query Templates** - Immediate utility for users

### Medium-Term Priorities (v0.9.0 - v1.0.0)

1. **Complete SHACL Coverage** - All major classes validated
2. **Health & Pensions KBs** - Full domain coverage
3. **FIBO Mapping** - Industry standard alignment
4. **Python Library** - Programmatic access

### Long-Term Priorities (v1.0.0+)

1. **Reasoning Rules** - Automated inference
2. **Multi-Language** - Global accessibility
3. **Jurisdictional Variants** - International applicability
4. **Governance Model** - Sustainable evolution

---

## Success Metrics

### Technical Metrics
- SHACL shape coverage: 100% of major classes
- Knowledge base instances: 1000+ across all domains
- SPARQL query library: 50+ production queries
- External mappings: 4+ major ontologies

### Adoption Metrics
- GitHub stars: 500+
- Active contributors: 20+
- Production implementations: 10+
- Academic citations: 25+

### Quality Metrics
- Competency question answerability: Maintain 100%
- Validation error rate: <1% on new submissions
- Documentation completeness: 100% for public APIs
- Test coverage: 95%+ for validation rules

---

## Version History

| Version | Milestone | Key Deliverables |
|---------|-----------|------------------|
| 0.8.0 | Validation | Core SHACL shapes, disjointness axioms |
| 0.9.0 | Expansion | Life & Health KBs, SPARQL library |
| 0.10.0 | Integration | FIBO mapping, Python library |
| 1.0.0 | Production | Full validation, all domains, governance |
| 1.1.0 | International | Multi-language, jurisdictional variants |
| 2.0.0 | Reasoning | Advanced inference, property chains |

---

## Contributing

We welcome contributions to help achieve this roadmap. Key areas where help is needed:

1. **Domain Expertise** - Actuaries to review and validate concepts
2. **Technical Development** - SHACL shapes, SPARQL queries, tooling
3. **Translation** - Multi-language label and definition translation
4. **Testing** - Knowledge base population and validation
5. **Documentation** - Tutorials, examples, case studies

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

---

## Contact & Resources

- **Repository:** https://github.com/Actuarial-Notes/Actuarial-Ontology
- **Issues:** GitHub Issues for bug reports and feature requests
- **Discussions:** GitHub Discussions for questions and ideas
- **License:** MIT License

---

*This roadmap is a living document and will be updated as the project evolves.*
