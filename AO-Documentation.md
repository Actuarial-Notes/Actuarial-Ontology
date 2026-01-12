# Actuarial Ontology - Documentation

## Overview

This document describes the Actuarial Ontology (AO), version 0.5.0-draft. The ontology is written in Turtle (TTL) format and can be opened in Protégé or other OWL ontology editors.

**Major Update (v0.5.0):** This version completes Phase 4 domain expansion with:
- **ASOP 38/39** - Catastrophe modeling, scenario analysis, and extreme event concepts
- **Professional Practice** - Professional judgment, peer review, and quality control concepts
- **Detailed Regulatory Framework** - Enhanced Solvency II, IFRS 17, and regulatory reporting concepts

Previous phases included foundational alignment with:
- **UFO** (Unified Foundational Ontology) - ontological rigor for endurants/perdurants, kinds/roles/phases
- **COVER** (Common Ontology of Value and Risk) - value-risk integration and event chains
- **ASOPs** (Actuarial Standards of Practice) - professional practice framework

See [AO-Standards-Review](https://github.com/Actuarial-Notes/Actuarial-Ontology/blob/main/AO-Standards-Review.md) for detailed analysis.

## Purpose

The Actuarial Ontology defines core concepts, relationships, and practices in actuarial science - the discipline of measuring and managing financial risk. It covers domains including:

- Insurance (life, health, property, casualty)
- Pensions and annuities
- Risk management
- Investment and capital modeling
- Actuarial processes and methods
- Value assessment and risk-value connections
- Actuarial professional communications and standards

## Structure

The ontology follows ontological engineering best practices and aligns with established frameworks:

1. **Domain & Scope**: Actuarial science and related financial risk management
2. **Top-Level Categories**: Aligned with UFO - Endurants (entities persisting through time) and Perdurants (events occurring in time)
3. **Rigidity Distinctions**: Kinds (rigid types like Person), Roles (anti-rigid like Insured), Phases (anti-rigid intrinsic like PaidClaim)
4. **Clear Definitions**: Each class and property includes rdfs:comment with definitions
5. **Hierarchical Organization**: Classes organized in meaningful taxonomies
6. **Standards Alignment**: Explicit references to ASOPs and ontological patterns

## Main Components

### 1. Object Properties (Relationships)

Object properties define relationships between entities:

#### Core Relationships
- `hasAgent` - relates activities to agents
- `manages` - relates agents to risks they manage
- `exposedTo` - relates agents to risks they face
- `causedBy` - relates events to perils
- `resultsIn` - relates events to losses

#### Insurance Relationships
- `insures` - relates insurers to insured parties
- `hasPolicy` - relates insured to their policies
- `covers` - relates policies to risks covered
- `hasClaim` - relates policies to claims
- `triggeredBy` - relates claims to triggering events
- `hasReserve` - relates claims to reserves

#### Financial Relationships
- `hasAsset` - relates entities to their assets
- `hasLiability` - relates entities to their liabilities
- `investsIn` - relates investors to assets

#### Model Relationships
- `usesModel` - relates activities to models
- `basedOnData` - relates models to data
- `producesEstimate` - relates models to estimates

### 2. Data Properties

Data properties define measurable attributes:

#### Measurement Properties
- `hasValue` - numeric value of measurements
- `hasMonetaryValue` - monetary values
- `hasProbability` - probability values (0 to 1)
- `hasSeverity` - magnitude of losses
- `hasFrequency` - frequency of events

#### Temporal Properties
- `effectiveDate` - when policies become effective
- `expirationDate` - when policies expire
- `occurrenceDate` - when events occurred
- `reportingDate` - when claims were reported

#### Identification Properties
- `policyNumber` - unique policy identifiers
- `claimNumber` - unique claim identifiers

### 3. Classes

Classes are organized hierarchically with clear parent-child relationships:

#### Top-Level Categories
- **Entity**: Things that exist and can be distinguished
- **Agent**: Entities that can act or make decisions
- **Event**: Things that happen at a time and place
- **Activity**: Processes performed by agents
- **Object**: Physical or abstract things

#### Agent Types
- Person, Organization
- Actuary (specialized Person)
- Insurer, Reinsurer (specialized Organizations)
- Insured, Policyholder, Beneficiary
- Investor, Regulator

#### Risk Concepts
Core risk taxonomy:
- **Risk**: Uncertainty of financial loss
  - InsurableRisk / UninsurableRisk
  - SystemicRisk / IdiosyncraticRisk

Specific risk types:
- MortalityRisk, LongevityRisk, MorbidityRisk
- PropertyRisk, LiabilityRisk
- MarketRisk, CreditRisk, OperationalRisk
- CatastropheRisk

#### Perils and Events
- **Peril**: Specific cause of loss
  - NaturalPeril (earthquake, hurricane, flood)
  - ManmadePeril (fire, theft, terrorism)
- **LossEvent**: Events resulting in financial loss
- **ClaimEvent**: Events triggering claims

#### Insurance Products
- LifeInsurance (TermLife, WholeLife)
- HealthInsurance
- PropertyInsurance (Auto, Homeowners)
- CasualtyInsurance
- Annuity
- Pension (DefinedBenefit, DefinedContribution)

#### Insurance Contracts
- InsurancePolicy, ReinsuranceContract
- Coverage, Exclusion
- Deductible, Limit

#### Claims
- Claim taxonomy:
  - ReportedClaim (Paid, Outstanding)
  - IncurredButNotReported (IBNR)

#### Financial Concepts
- FinancialInstrument
  - Asset
  - Liability
    - Reserve (ClaimReserve, CaseReserve, IBNRReserve)
  - Capital (EconomicCapital, RegulatoryCapital)
- Premium, Loss, UltimateClaimCost

#### Actuarial Activities
Professional activities:
- RiskAssessment
- Pricing
- Reserving
- Valuation
- CapitalModeling
- ExperienceAnalysis
- ProductDevelopment

#### Actuarial Models and Methods
- PricingModel (GeneralizedLinearModel)
- ReservingModel (ChainLadderMethod, LossDevelopmentTriangle)
- CapitalModel
- MortalityTable

#### Data and Measurements
- Data (ClaimData, ExposureData, PremiumData)
- Measurement, FinancialMeasurement
- Estimate, Assumption

#### Metrics and Ratios
- LossRatio
- ExpenseRatio
- CombinedRatio
- ReturnOnEquity

#### Regulatory and Standards
- Regulation (Solvency2)
  - RegulatoryRequirement
  - CapitalRequirement (SolvencyCapitalRequirement, MinimumCapitalRequirement, RiskBasedCapital)
  - RegulatoryApproval
- ActuarialStandard
- AccountingStandard (IFRS17, GAAP)
- RegulatoryReporting, RegulatoryReport
- ORSA (Own Risk and Solvency Assessment)
- ContractualServiceMargin, RiskAdjustment
- InternalModel

#### Catastrophe Modeling (ASOP 38/39)
- CatastropheModel
  - FrequencyModel
  - SeverityModel
- ScenarioAnalysis
- CatastropheScenario
- TailRisk, ExtremeEvent
- ReturnPeriod

#### Professional Practice
- ProfessionalJudgment
- Deviation
- PeerReview
- QualityControl
- AuditTrail
- WorkPaper

## Design Principles Applied

1. **Nouns for Classes**: All classes are single nouns (e.g., "Person", "Risk", "Claim")
2. **Verbs for Properties**: Properties are verbs readable as triples (e.g., "hasAgent", "covers")
3. **Clear Definitions**: Every class and property has a definition following the pattern "A is a B that C"
4. **Hierarchical Structure**: Classes organized with appropriate parent-child relationships
5. **Domain Relevance**: Concepts close to real objects and relationships in actuarial practice

## Competency Questions

This ontology should enable answering questions such as:

1. **Risk Management**:
   - What risks is this entity exposed to?
   - Which agents manage mortality risk?
   - Is this risk insurable?

2. **Insurance Operations**:
   - What policies cover this risk?
   - Which claims were triggered by natural perils?
   - What reserves are established for outstanding claims?

3. **Financial Analysis**:
   - What is the loss ratio for this portfolio?
   - What capital does this insurer hold?
   - What assets does this investor hold?

4. **Actuarial Processes**:
   - What models are used in pricing this product?
   - What data is this reserving model based on?
   - Which actuarial activities use mortality tables?

5. **Regulatory Compliance**:
   - Does this practice comply with IFRS 17?
   - What regulatory capital is required under Solvency II?

## Usage with Protégé

To work with this ontology:

1. Download Protégé from https://protege.stanford.edu/
2. Open the `actuarial-ontology.ttl` file
3. Use the Class hierarchy tab to explore concepts
4. Use the Object Properties tab to see relationships
5. Use the Data Properties tab to see attributes
6. Run reasoners (Fact++, HermiT) to check consistency

## Next Steps

This is a first draft. Future development should:

1. **Expand Coverage**: Add more specific concepts from actuarial standards
2. **Add Instances**: Create example entities to test the ontology
3. **Define Constraints**: Add domain/range restrictions, cardinality constraints
4. **Align with Upper Ontologies**: Map to UFO (Unified Foundational Ontology)
5. **Cross-reference Standards**: Link to specific ASOP, ESAP, ISAP definitions
6. **Add Axioms**: Define logical rules and constraints
7. **Community Review**: Gather feedback from actuarial professionals
8. **Test with Reasoners**: Validate logical consistency
9. **Build Knowledge Base**: Populate with real-world instances

## Contributing

See the project [README.md](README.md) and [Code of Conduct](Code%20of%20Conduct.md) for contribution guidelines.

## References

**Foundational Ontologies:**
- UFO (Unified Foundational Ontology) - [nemo.inf.ufes.br/en/projetos/ufo](https://nemo.inf.ufes.br/en/projetos/ufo/)
- COVER (Common Ontology of Value and Risk) - Sales & Baião (2018)
- gUFO - Lightweight UFO implementation - [nemo-ufes.github.io/gufo](https://nemo-ufes.github.io/gufo/)

**Actuarial Standards:**
- Actuarial Standards of Practice (ASOPs) - [actuarialstandardsboard.org](http://www.actuarialstandardsboard.org/)
- International Standards of Actuarial Practice (ISAPs)
- European Standards of Actuarial Practice (ESAPs)
- SOA Competency Framework
- CAS Capability Model

**Regulatory Frameworks:**
- IFRS 17 - Insurance Contracts
- Solvency II Framework
- GAAP - Generally Accepted Accounting Principles

## License

This ontology is released under the MIT License. See [LICENSE](LICENSE) file for details.

## Version History

- **0.5.0-draft** (2026-01-12): Phase 4 domain expansion
  - Added catastrophe modeling (ASOP 38/39): CatastropheModel, FrequencyModel, SeverityModel, ScenarioAnalysis, TailRisk, ExtremeEvent, ReturnPeriod, CatastropheScenario
  - Added professional practice concepts: ProfessionalJudgment, Deviation, PeerReview, QualityControl, AuditTrail, WorkPaper
  - Enhanced regulatory framework: RegulatoryReporting, RegulatoryReport, RegulatoryRequirement, CapitalRequirement, SolvencyCapitalRequirement, MinimumCapitalRequirement, RiskBasedCapital, ORSA, ContractualServiceMargin, RiskAdjustment, RegulatoryApproval, InternalModel
  - Added 14 new object properties for catastrophe modeling, professional practice, and regulatory compliance
  - Total: 194 classes (+31), 76 object properties (+14)

- **0.4.0-draft** (2026-01-12): Phase 3 data and model governance
  - Added ASOP 23 data quality concepts
  - Added ASOP 56 model governance
  - Added ASOP 25 credibility theory

- **0.3.0-draft** (2026-01-12): Phase 2 risk and value modeling
  - Enhanced risk assessment (ASOP 51)
  - Added UFO-C social and intentional entities
  - Enhanced risk tolerance and appetite concepts

- **0.2.0-draft** (2026-01-11): Phase 1 foundational alignment
  - Restructured top-level categories aligned with UFO (Endurants/Perdurants)
  - Added rigidity distinctions (Kinds: Person, Organization; Roles: Actuary, Insured; Phases: PaidClaim, OutstandingClaim)
  - Integrated COVER's tripartite risk distinction (QuantitativeRisk, RiskExperience, RiskAssessmentJudgment)
  - Added COVER value concepts (Value, ValueObject, ValueExperience, ValueAscription)
  - Enhanced event chain with ThreatEvent (Peril → ThreatEvent → LossEvent)
  - Added dispositions and vulnerabilities (COVER/UFO pattern)
  - Added ASOP 41 communication framework (ActuarialCommunication, ActuarialOpinion, Disclosure, IntendedUser)
  - Added UFO-C social concepts (Commitment, Right, Goal)
  - Added annotation properties (rigidity, ufoCategory, asopReference)
  - Added UFO participation model (participatesIn, hasParticipant, inheresIn)
  - Updated Measurement as subclass of Moment (UFO pattern)
  - Total: 134 classes (↑34), 31 object properties (↑18), 3 annotation properties (new)

- **0.1.0-draft** (2026-01-10): Initial draft covering core actuarial concepts across insurance, pensions, risk management, and financial domains.
