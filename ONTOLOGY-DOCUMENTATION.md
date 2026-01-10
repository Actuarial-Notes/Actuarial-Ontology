# Actuarial Ontology - Documentation

## Overview

This document describes the first draft of the Actuarial Ontology (AO), version 0.1.0-draft. The ontology is written in Turtle (TTL) format and can be opened in Protégé or other OWL ontology editors.

## Purpose

The Actuarial Ontology defines core concepts, relationships, and practices in actuarial science - the discipline of measuring and managing financial risk. It covers domains including:

- Insurance (life, health, property, casualty)
- Pensions and annuities
- Risk management
- Investment and capital modeling
- Actuarial processes and methods

## Structure

The ontology follows best practices outlined in the Project Guide:

1. **Domain & Scope**: Actuarial science and related financial risk management
2. **Top-Level Categories**: Entities, Agents, Events, Activities, Objects
3. **Clear Definitions**: Each class and property includes rdfs:comment with definitions
4. **Hierarchical Organization**: Classes organized in meaningful taxonomies

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
- ActuarialStandard
- AccountingStandard (IFRS17, GAAP)

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

- Actuarial Standards of Practice (ASOPs)
- International Standards of Actuarial Practice (ISAPs)
- SOA Competency Framework
- CAS Capability Model
- IFRS 17 - Insurance Contracts
- Solvency II Framework

## License

This ontology is released under the MIT License. See [LICENSE](LICENSE) file for details.

## Version History

- **0.1.0-draft** (2026-01-10): Initial draft covering core actuarial concepts across insurance, pensions, risk management, and financial domains.
