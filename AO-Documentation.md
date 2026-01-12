# Actuarial Ontology - Documentation

## Overview

This document describes the Actuarial Ontology (AO), version 0.7.0-draft. The ontology is written in Turtle (TTL) format and can be opened in Protégé or other OWL ontology editors.

**Current Version (v0.7.0):** Comprehensive domain expansion with 126+ new classes and 14+ new properties across 13 critical actuarial domains.

**Phase 4 (v0.5.0)** - Domain expansion with:
- **ASOP 38/39** - Catastrophe modeling, scenario analysis, and extreme event concepts
- **Professional Practice** - Professional judgment, peer review, and quality control concepts
- **Detailed Regulatory Framework** - Enhanced Solvency II, IFRS 17, and regulatory reporting concepts

**Previous Phases** included foundational alignment with:
- **UFO** (Unified Foundational Ontology) - ontological rigor for endurants/perdurants, kinds/roles/phases
- **COVER** (Common Ontology of Value and Risk) - value-risk integration and event chains
- **ASOPs** (Actuarial Standards of Practice) - professional practice framework

See [AO-Testing-Report](https://github.com/Actuarial-Notes/Actuarial-Ontology/blob/main/AO-Testing-Report.md) for detailed testing results.

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

#### Underwriting (New in v0.7)
- Underwriting taxonomy:
  - RiskSelection
  - RiskClassification
  - MedicalUnderwriting
  - FinancialUnderwriting
- UnderwritingGuidelines, UnderwritingCriteria
- Risk classifications: PreferredRisk, StandardRisk, SubstandardRisk, DeclinedRisk
- AdverseSelection, MoralHazard

#### Reinsurance Structures (Expanded in v0.7)
- Treaty vs. Facultative:
  - TreatyReinsurance
  - FacultativeReinsurance
- Proportional structures:
  - QuotaShareReinsurance
  - SurplusReinsurance
- Non-proportional structures:
  - ExcessOfLossReinsurance
  - CatastropheExcessOfLoss
  - StopLossReinsurance
- RetentionLimit, ReinsuranceCession, CedingCommission, Retrocession

#### Distribution and Marketing (New in v0.7)
- Roles: Agent, Broker, ClaimsAdjuster
- Agent types: CaptiveAgent, IndependentAgent, ManagingGeneralAgent
- Adjuster types: IndependentAdjuster, PublicAdjuster
- DistributionChannel, DirectWriter

#### Claims Management (Expanded in v0.7)
- Activities: ClaimsAdjustment, ClaimsInvestigation, ClaimsSettlement
- FraudDetection, FraudulentClaim
- Salvage, Subrogation

#### Policyholder Behavior (New in v0.7)
- Events: Lapse, Surrender, PolicyWithdrawal
- Measurements: LapseRate, PersistencyRate, Persistency
- PolicyLoan

#### Asset-Liability Management (New in v0.7)
- AssetLiabilityManagement
- Strategies: DurationMatching, CashFlowMatching, ImmunizationStrategy
- AssetAllocation
- Risks: InterestRateRisk, ReinvestmentRisk

#### Life Insurance Specifics (Expanded in v0.7)
- Values: CashValue, SurrenderValue, NonForfeitureValue
- Product types: UniversalLifeInsurance, VariableLifeInsurance
- Policy types: ParticipatingPolicy, NonParticipatingPolicy
- PolicyDividend
- Benefits: DeathBenefit, LivingBenefit, AcceleratedDeathBenefit
- Guarantees: GuaranteedMinimumDeathBenefit
- Riders: RiderBenefit, WaiverOfPremiumRider

#### Premium and Rating (Expanded in v0.7)
- Premium types: GrossPremium, NetPremium, LoadedPremium
- PremiumRate, RatingFactor
- Rating methods: ExperienceRating, ManualRating, ScheduleRating, RetrospectiveRating
- LossCost
- Expenses: ExpenseLoading, AcquisitionExpense, MaintenanceExpense

#### Emerging Risks (New in v0.7)
- EmergingRisk
- CyberRisk
- PandemicRisk
- ClimateRisk
- ESGRisk
- TechnologyRisk

#### Portfolio and Exposure Management (New in v0.7)
- Portfolio types: InsurancePortfolio, InvestmentPortfolio
- BookOfBusiness
- ExposureUnit
- InForcePolicy
- PortfolioSegmentation

#### Stochastic and Statistical Modeling (New in v0.7)
- Model types: StochasticModel, DeterministicModel
- Techniques: MonteCarloSimulation, Bootstrapping
- Activities: ScenarioGeneration, StressTesting, SensitivityAnalysis, BackTesting

#### Embedded Value and Appraisal (New in v0.7)
- EmbeddedValue
- AppraisalValue
- ValueOfNewBusiness (VNB)
- ValueOfInForceBusiness (VIF)
- MarketConsistentEmbeddedValue (MCEV)
- EuropeanEmbeddedValue (EEV)

#### Experience Studies (New in v0.7)
- ExperienceStudy
- MortalityStudy
- LapseStudy
- ExpenseStudy
- ClaimsExperienceStudy

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

## Status and Next Steps

**Completed:**
- ✅ All 4 improvement phases implemented (v0.6.0)
- ✅ 100% competency question answerability achieved
- ✅ Foundational alignment with UFO, COVER, and ASOPs complete
- ✅ Comprehensive domain expansion (v0.7.0) - added 126+ classes across 13 critical domains:
  - Underwriting (13 classes) - complete coverage of risk selection and classification
  - Reinsurance structures (13 classes) - treaty/facultative, proportional/non-proportional
  - Distribution and marketing (7 classes) - agents, brokers, channels
  - Claims management (10 classes) - adjustment, fraud, settlement
  - Policyholder behavior (7 classes) - lapse, surrender, persistency
  - Asset-liability management (7 classes) - duration matching, immunization
  - Life insurance specifics (14 classes) - cash values, riders, benefits
  - Premium and rating (13 classes) - gross/net premium, rating methods
  - Emerging risks (6 classes) - cyber, pandemic, climate, ESG
  - Portfolio management (7 classes) - exposure units, segmentation
  - Stochastic modeling (8 classes) - Monte Carlo, stress testing
  - Embedded value (6 classes) - MCEV, EEV, VNB, VIF
  - Experience studies (5 classes) - mortality, lapse, expense studies
- ✅ Now the most comprehensive actuarial ontology with ~320 classes and ~90 properties

**Future Development:**
1. **Add Formal Constraints**: Define domain/range restrictions, cardinality constraints, and disjointness axioms
2. **Expand Knowledge Base**: Populate with more real-world instances beyond Canadian P&C insurance
3. **Add SPARQL Query Library**: Create reusable query patterns for common use cases
4. **Define Advanced Axioms**: Add property chains, value restrictions, and logical rules
5. **Community Review**: Gather feedback from actuarial professionals and practitioners
6. **Integration**: Map to external ontologies (FIBO, schema.org) for broader interoperability
7. **Multilingual Support**: Add labels and definitions in other languages (French, Spanish, etc.)
8. **Validation Framework**: Implement SHACL shapes for enhanced data quality validation

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

- **0.7.0-draft** (2026-01-12): Major domain expansion - comprehensive coverage of actuarial practice
  - Added underwriting domain: Underwriting, RiskSelection, RiskClassification, MedicalUnderwriting, FinancialUnderwriting, UnderwritingGuidelines, UnderwritingCriteria, AdverseSelection, MoralHazard, PreferredRisk, StandardRisk, SubstandardRisk, DeclinedRisk (13 new classes)
  - Expanded reinsurance: TreatyReinsurance, FacultativeReinsurance, ProportionalReinsurance, QuotaShareReinsurance, SurplusReinsurance, NonProportionalReinsurance, ExcessOfLossReinsurance, CatastropheExcessOfLoss, StopLossReinsurance, RetentionLimit, ReinsuranceCession, CedingCommission, Retrocession (13 new classes)
  - Added distribution and marketing: Agent, Broker, DistributionChannel, DirectWriter, CaptiveAgent, IndependentAgent, ManagingGeneralAgent (7 new classes)
  - Expanded claims management: ClaimsAdjustment, ClaimsInvestigation, ClaimsSettlement, ClaimsAdjuster, IndependentAdjuster, PublicAdjuster, FraudDetection, FraudulentClaim, Salvage, Subrogation (10 new classes)
  - Added policyholder behavior: Lapse, Surrender, Persistency, LapseRate, PersistencyRate, PolicyWithdrawal, PolicyLoan (7 new classes)
  - Added asset-liability management: AssetLiabilityManagement, DurationMatching, CashFlowMatching, ImmunizationStrategy, AssetAllocation, InterestRateRisk, ReinvestmentRisk (7 new classes)
  - Expanded life insurance: CashValue, SurrenderValue, NonForfeitureValue, PolicyDividend, ParticipatingPolicy, NonParticipatingPolicy, UniversalLifeInsurance, VariableLifeInsurance, RiderBenefit, LivingBenefit, DeathBenefit, AcceleratedDeathBenefit, GuaranteedMinimumDeathBenefit, WaiverOfPremiumRider (14 new classes)
  - Expanded premium and rating: GrossPremium, NetPremium, LoadedPremium, PremiumRate, RatingFactor, ExperienceRating, ManualRating, ScheduleRating, RetrospectiveRating, LossCost, ExpenseLoading, AcquisitionExpense, MaintenanceExpense (13 new classes)
  - Added emerging risks: EmergingRisk, CyberRisk, PandemicRisk, ClimateRisk, ESGRisk, TechnologyRisk (6 new classes)
  - Added portfolio management: Portfolio, InsurancePortfolio, InvestmentPortfolio, ExposureUnit, InForcePolicy, BookOfBusiness, PortfolioSegmentation (7 new classes)
  - Added stochastic modeling: StochasticModel, DeterministicModel, MonteCarloSimulation, ScenarioGeneration, StressTesting, SensitivityAnalysis, BackTesting, Bootstrapping (8 new classes)
  - Added embedded value: EmbeddedValue, AppraisalValue, ValueOfNewBusiness, ValueOfInForceBusiness, MarketConsistentEmbeddedValue, EuropeanEmbeddedValue (6 new classes)
  - Added experience studies: ExperienceStudy, MortalityStudy, LapseStudy, ExpenseStudy, ClaimsExperienceStudy (5 new classes)
  - Added 14 new object properties: underwrites, classifiesAs, sellsThrough, representsInsurer, investigates, settles, cedesTo, assumesFrom, hasExposure, segmentsInto, generatesScenario, containsPolicy, belongsToPortfolio, and domain-specific relationships
  - Added 8 new data properties: retentionAmount, lapseRate, persistencyRate, cashValueAmount, deathBenefitAmount, loadingPercentage, exposureAmount, embeddedValueAmount
  - Total: ~320 classes (+126), ~90 object properties (+14), ~30 data properties (+8)
  - Achieved comprehensive coverage across all major actuarial practice areas

- **0.6.0-draft** (2026-01-12): Competency gap closure - 100% answerability achieved
  - Added `ao:hasMetric` property to enable financial metric and performance measure queries
  - Added `ao:hasSubject` / `ao:subjectOf` inverse property pair to link entities to actuarial activities
  - All 14 competency questions now fully answerable (up from 7/14 in v0.4.0)
  - Improved from 50% to 100% competency question coverage
  - Total: 194 classes, 76 object properties

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
