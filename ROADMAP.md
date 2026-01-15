# Actuarial Ontology Development Roadmap

**Version:** 2.0
**Last Updated:** January 2026
**Current Ontology Version:** 0.7.0

---

## Vision

**Empower actuaries with AI agents capable of performing actuarial tasks.**

The ontology is not the end goal - it's foundational infrastructure. The real goal is AI systems that can assist actuaries with:

- Risk Assessment
- Pricing
- Reserving
- Valuation
- Investment
- Capital Modelling
- Regulatory Compliance
- Product Development

This roadmap prioritizes capabilities that directly enable AI-powered actuarial work.

---

## Why an Ontology for AI?

Large Language Models are powerful but lack:

1. **Domain precision** - "claim" means different things in different contexts
2. **Structured reasoning** - actuarial calculations require formal relationships
3. **Verifiable outputs** - AI work must be auditable and validated
4. **Knowledge grounding** - reducing hallucination through factual anchoring

The Actuarial Ontology provides:
- **Unambiguous vocabulary** for AI to understand actuarial concepts
- **Formal relationships** enabling structured reasoning
- **Validation schemas** to verify AI outputs are correct
- **Knowledge graphs** for retrieval-augmented generation (RAG)

---

## Development Phases

| Phase | Focus | Outcome |
|-------|-------|---------|
| **Phase 1** | AI Task Frameworks | Agents can perform core actuarial tasks |
| **Phase 2** | Knowledge Infrastructure | RAG-ready knowledge bases with validation |
| **Phase 3** | Tool Ecosystem | Function calling, APIs, software integration |
| **Phase 4** | Production Deployment | Enterprise-ready with governance |
| **Phase 5** | Advanced Capabilities | Autonomous workflows, multi-agent systems |

---

## Phase 1: AI Task Frameworks

**Objective:** Define how AI agents perform specific actuarial tasks using the ontology.

### 1.1 Task Ontology Extension

Define the structure of actuarial tasks AI agents can perform:

```turtle
ao:ActuarialTask a owl:Class ;
    rdfs:subClassOf ao:Activity ;
    rdfs:comment "A task an AI agent can perform to assist actuaries" .

ao:hasInput a owl:ObjectProperty ;
    rdfs:domain ao:ActuarialTask ;
    rdfs:comment "Data or knowledge required to perform the task" .

ao:hasOutput a owl:ObjectProperty ;
    rdfs:domain ao:ActuarialTask ;
    rdfs:comment "Deliverable produced by the task" .

ao:requiresJudgment a owl:DatatypeProperty ;
    rdfs:domain ao:ActuarialTask ;
    rdfs:range xsd:boolean ;
    rdfs:comment "Whether task requires human actuarial judgment" .
```

#### Core Task Definitions

| Task | Inputs | Outputs | Requires Judgment |
|------|--------|---------|-------------------|
| **RiskAssessmentTask** | ExposureData, HistoricalLosses | RiskProfile, RiskScore | Yes |
| **PricingTask** | RiskProfile, ExpenseAssumptions, TargetReturn | PremiumIndication | Yes |
| **ReservingTask** | ClaimsTriangle, DevelopmentPatterns | ReserveEstimate, RangeOfEstimates | Yes |
| **ValuationTask** | PolicyData, Assumptions, Discount Rates | LiabilityEstimate | Yes |
| **ExperienceStudyTask** | ExposureData, ClaimsData | MortalityRates, LapseRates | No |
| **DataValidationTask** | RawData, DataQualityRules | ValidationReport, CleanedData | No |
| **RegulatoryReportTask** | FinancialData, ReportingRules | FilingDocument | Partial |
| **ModelValidationTask** | Model, TestData, Benchmarks | ValidationReport | Yes |

### 1.2 Prompt Templates

Create ontology-grounded prompt templates for each task:

```markdown
## Reserve Estimation Prompt Template

You are an actuarial AI assistant. Using the Actuarial Ontology definitions:

**Task:** ao:ReservingTask
**Context:** {knowledge_base_context}

**Inputs provided:**
- Claims Triangle: {claims_data}
- Development Patterns: {development_factors}
- Line of Business: {lob} (ao:LineOfBusiness)

**Required Output (ao:ReserveEstimate):**
1. Point estimate with method used
2. Range of reasonable estimates
3. Key assumptions (ao:Assumption)
4. Data limitations (ao:DataLimitation per ASOP 23)
5. Uncertainty assessment (ao:ModelUncertainty per ASOP 56)

**Constraints:**
- Use terminology from ao: namespace
- Reference applicable ASOPs
- Flag items requiring ao:ProfessionalJudgment
```

#### Deliverables:
- `/prompts/risk-assessment.md`
- `/prompts/pricing.md`
- `/prompts/reserving.md`
- `/prompts/valuation.md`
- `/prompts/experience-study.md`
- `/prompts/data-validation.md`
- `/prompts/regulatory-reporting.md`
- `/prompts/model-validation.md`

### 1.3 Output Schemas

Define JSON schemas for AI outputs that map to ontology classes:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ReserveEstimate",
  "description": "AI-generated reserve estimate per ao:ReserveEstimate",
  "type": "object",
  "properties": {
    "pointEstimate": {
      "type": "object",
      "properties": {
        "value": { "type": "number" },
        "currency": { "type": "string" },
        "method": {
          "type": "string",
          "enum": ["ChainLadder", "BornhuetterFerguson", "CapeCod", "FrequencySeverity"]
        },
        "asOfDate": { "type": "string", "format": "date" }
      },
      "required": ["value", "currency", "method", "asOfDate"]
    },
    "rangeOfEstimates": {
      "type": "object",
      "properties": {
        "low": { "type": "number" },
        "high": { "type": "number" },
        "confidence": { "type": "number", "minimum": 0, "maximum": 1 }
      }
    },
    "assumptions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "description": { "type": "string" },
          "asopReference": { "type": "string" },
          "sensitivity": { "type": "string", "enum": ["low", "medium", "high"] }
        }
      }
    },
    "dataLimitations": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Per ASOP 23 data quality requirements"
    },
    "uncertaintyAssessment": {
      "type": "string",
      "description": "Per ASOP 56 model uncertainty requirements"
    },
    "judgmentItems": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Items flagged for human actuarial review"
    }
  },
  "required": ["pointEstimate", "assumptions", "judgmentItems"]
}
```

#### Deliverables:
- `/schemas/reserve-estimate.json`
- `/schemas/risk-assessment.json`
- `/schemas/premium-indication.json`
- `/schemas/experience-study-results.json`
- `/schemas/validation-report.json`

### 1.4 Human-in-the-Loop Workflows

Define where human actuarial judgment is required:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   AI Agent      │────▶│  Judgment Gate  │────▶│    Actuary      │
│   (Task Exec)   │     │  (ao:requires   │     │   (Review &     │
│                 │     │   Judgment=true)│     │    Approve)     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
         │                                               │
         │              ┌─────────────────┐              │
         └─────────────▶│   Final Output  │◀─────────────┘
                        │  (Validated &   │
                        │   Documented)   │
                        └─────────────────┘
```

**Automatic (No Judgment Required):**
- Data extraction and cleaning
- Standard calculations (loss ratios, development factors)
- Report formatting
- Compliance checklist verification

**Human Review Required:**
- Assumption selection
- Method selection for non-standard situations
- Professional judgment on uncertainty
- Sign-off on regulatory filings
- Deviation from standards (ASOP 41)

---

## Phase 2: Knowledge Infrastructure

**Objective:** Build RAG-ready knowledge bases that ground AI responses in verified actuarial knowledge.

### 2.1 Chunking Strategy for RAG

Structure knowledge for optimal retrieval:

```
/knowledge-base/
  /concepts/           # Ontology class definitions (small chunks)
    mortality-risk.md
    loss-ratio.md
    ibnr-reserve.md
  /methods/            # Actuarial methods (medium chunks)
    chain-ladder.md
    bornhuetter-ferguson.md
    mortality-table-construction.md
  /standards/          # ASOP summaries (medium chunks)
    asop-23-data-quality.md
    asop-41-communications.md
    asop-56-modeling.md
  /examples/           # Worked examples (large chunks)
    auto-liability-reserving.md
    term-life-pricing.md
  /regulations/        # Regulatory requirements
    solvency-ii-overview.md
    ifrs-17-overview.md
```

### 2.2 Knowledge Base Expansion

Priority order based on AI task enablement:

| Priority | Knowledge Base | Enables Tasks |
|----------|---------------|---------------|
| 1 | **Reserving Methods KB** | ReservingTask, ModelValidationTask |
| 2 | **Pricing Methods KB** | PricingTask, RiskAssessmentTask |
| 3 | **ASOP Reference KB** | All tasks (compliance grounding) |
| 4 | **Life Insurance KB** | Life-specific pricing, valuation |
| 5 | **Health Insurance KB** | Health-specific tasks |
| 6 | **Regulatory KB** | RegulatoryReportTask |

#### Reserving Methods KB Content:
- Chain Ladder method with worked examples
- Bornhuetter-Ferguson with credibility weighting
- Cape Cod method
- Frequency-Severity approaches
- Stochastic reserving (bootstrap, Mack)
- Selection criteria and when to use each

### 2.3 Validation Layer (SHACL)

SHACL shapes serve AI output validation:

```turtle
ao:ReserveEstimateShape a sh:NodeShape ;
    sh:targetClass ao:ReserveEstimate ;
    sh:property [
        sh:path ao:hasMonetaryValue ;
        sh:minCount 1 ;
        sh:datatype xsd:decimal ;
        sh:minInclusive 0 ;
        sh:message "Reserve estimate must have non-negative monetary value"
    ] ;
    sh:property [
        sh:path ao:hasAssumption ;
        sh:minCount 1 ;
        sh:message "Reserve estimate must document assumptions per ASOP 41"
    ] ;
    sh:property [
        sh:path ao:asOfDate ;
        sh:minCount 1 ;
        sh:datatype xsd:date ;
        sh:message "Reserve estimate must have valuation date"
    ] .
```

**Purpose:** When AI generates a reserve estimate, validate it conforms to professional standards before presenting to actuary.

### 2.4 Embedding Strategy

Generate embeddings optimized for actuarial retrieval:

```python
# Conceptual approach
embedding_config = {
    "model": "text-embedding-3-large",
    "chunk_strategy": {
        "concepts": {"size": 200, "overlap": 50},
        "methods": {"size": 500, "overlap": 100},
        "examples": {"size": 1000, "overlap": 200}
    },
    "metadata": {
        "ontology_class": "ao:ChainLadderMethod",
        "applicable_tasks": ["ReservingTask"],
        "asop_references": ["ASOP 43"],
        "practice_area": ["P&C"]
    }
}
```

---

## Phase 3: Tool Ecosystem

**Objective:** Enable AI agents to execute actuarial calculations and integrate with existing tools.

### 3.1 Function Calling Definitions

Define tools AI agents can invoke:

```json
{
  "name": "calculate_loss_development_factors",
  "description": "Calculate age-to-age loss development factors from a claims triangle",
  "parameters": {
    "type": "object",
    "properties": {
      "triangle": {
        "type": "array",
        "description": "Claims triangle as 2D array [accident_period][development_period]"
      },
      "method": {
        "type": "string",
        "enum": ["volume_weighted", "simple_average", "medial"],
        "default": "volume_weighted"
      },
      "exclude_high_low": {
        "type": "boolean",
        "default": false
      }
    },
    "required": ["triangle"]
  }
}
```

#### Core Tools:
| Tool | Purpose |
|------|---------|
| `calculate_loss_development_factors` | Development factor selection |
| `project_ultimate_losses` | Apply factors to project ultimates |
| `calculate_ibnr` | IBNR = Ultimate - Paid |
| `calculate_loss_ratio` | Loss ratio computation |
| `apply_trend_factors` | Trend loss data |
| `calculate_present_value` | Discount cash flows |
| `generate_mortality_rates` | Extract rates from tables |
| `run_experience_study` | A/E analysis |
| `validate_against_shacl` | Validate outputs |

### 3.2 MCP Server Implementation

Build a Model Context Protocol server for actuarial tools:

```
/mcp-server/
  server.py              # MCP server implementation
  tools/
    reserving.py         # Reserving calculations
    pricing.py           # Pricing calculations
    experience.py        # Experience studies
    validation.py        # SHACL validation
  resources/
    ontology.py          # Serve ontology as resource
    knowledge_base.py    # Serve KB for RAG
```

This enables Claude and other AI systems to:
- Query the ontology for definitions
- Retrieve relevant knowledge base content
- Execute actuarial calculations
- Validate outputs against SHACL shapes

### 3.3 Software Integration

Priority integrations for actuary workflows:

| Integration | Purpose | Approach |
|-------------|---------|----------|
| **Excel/VBA** | Most actuaries work in Excel | COM add-in, Office Scripts |
| **Python** | Growing adoption, modeling | pip package |
| **R** | Statistical analysis | CRAN package |
| **Jupyter** | Documentation, analysis | Kernel extension |
| **Actuarial Platforms** | Enterprise systems | API adapters |

#### Python Package Structure:
```python
from actuarial_ontology import (
    # Knowledge access
    get_definition,      # "What is IBNR?"
    get_relationships,   # "What risks affect life insurance?"

    # Task execution
    ReservingTask,
    PricingTask,

    # Validation
    validate_output,

    # RAG support
    get_relevant_context,
    embed_query
)

# Example usage
task = ReservingTask(
    claims_triangle=data,
    line_of_business="auto_liability"
)
result = task.execute(ai_model="claude-3-opus")
validation = validate_output(result, "ReserveEstimateShape")
```

### 3.4 SPARQL for AI Context

Pre-built queries AI uses to gather context:

```sparql
# Get all risks that affect a given product type
PREFIX ao: <http://actuarialnotes.com/ontology/actuarial#>

SELECT ?risk ?riskType ?description
WHERE {
    ?product a ao:TermLifeInsurance .
    ?product ao:exposedTo ?risk .
    ?risk a ?riskType .
    ?risk rdfs:comment ?description .
    ?riskType rdfs:subClassOf* ao:Risk .
}
```

```sparql
# Get applicable ASOPs for a task
SELECT ?asop ?title ?relevance
WHERE {
    ao:ReservingTask ao:governedBy ?asop .
    ?asop rdfs:label ?title .
    ?asop ao:relevanceNote ?relevance .
}
```

---

## Phase 4: Production Deployment

**Objective:** Enterprise-ready deployment with appropriate governance and controls.

### 4.1 Actuarial AI Governance

Align with professional standards:

**ASOP 56 (Modeling) Compliance:**
- Document AI model selection rationale
- Validate AI outputs against known results
- Assess AI model limitations
- Maintain audit trail of AI-assisted work

**ASOP 41 (Communications) Compliance:**
- Disclose use of AI assistance
- Document AI limitations
- Identify items requiring professional judgment
- Enable actuarial sign-off workflow

**Governance Framework:**
```
┌─────────────────────────────────────────────────────────────┐
│                    AI Governance Layer                       │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   Access    │  │   Audit     │  │  Disclosure │         │
│  │   Control   │  │   Logging   │  │  Management │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   Output    │  │  Judgment   │  │   Version   │         │
│  │  Validation │  │   Routing   │  │   Control   │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Deployment Patterns

**Pattern 1: Copilot Mode**
- AI assists actuary in real-time
- Human reviews all outputs
- Lowest risk, immediate value

**Pattern 2: Draft Mode**
- AI generates initial work product
- Human reviews and edits
- Higher productivity, maintained oversight

**Pattern 3: Automation Mode**
- AI handles routine tasks end-to-end
- Human spot-checks and exceptions
- Highest efficiency, requires mature validation

### 4.3 Quality Assurance

**Backtesting Framework:**
- Compare AI outputs to historical actuary work
- Measure accuracy, identify systematic biases
- Continuous improvement feedback loop

**Benchmark Suite:**
- Standard test cases with known answers
- CAS exam problems
- SOA case studies
- Real-world anonymized examples

---

## Phase 5: Advanced Capabilities

**Objective:** Expand AI capabilities toward more autonomous actuarial work.

### 5.1 Multi-Agent Workflows

Complex actuarial projects as agent orchestration:

```
Product Development Workflow:
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Market     │────▶│    Risk      │────▶│   Pricing    │
│   Research   │     │  Assessment  │     │   Agent      │
│   Agent      │     │    Agent     │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
                                                  │
┌──────────────┐     ┌──────────────┐             │
│  Regulatory  │◀────│   Product    │◀────────────┘
│   Review     │     │   Design     │
│   Agent      │     │   Agent      │
└──────────────┘     └──────────────┘
```

### 5.2 Reasoning Capabilities

Enable formal reasoning over knowledge:

**Inference Examples:**
- If Product has MortalityRisk AND no reinsurance → Flag concentration risk
- If Reserve < 70th percentile historical → Flag potential inadequacy
- If Assumption changed > 10% from prior → Require documentation

**Property Chains:**
```turtle
# Infer indirect risk exposure
ao:hasIndirectExposure owl:propertyChainAxiom (
    ao:reinsures
    ao:exposedTo
) .

# Portfolio inherits policy risks
ao:portfolioExposedTo owl:propertyChainAxiom (
    ao:containsPolicy
    ao:exposedTo
) .
```

### 5.3 Continuous Learning

**Feedback Integration:**
- Capture actuary corrections to AI outputs
- Identify common error patterns
- Update prompts and knowledge base
- Improve task-specific fine-tuning

**Knowledge Expansion:**
- Extract knowledge from new ASOPs
- Incorporate regulatory changes
- Add emerging risk concepts
- Update from industry publications

---

## Implementation Priorities

### Immediate (v0.8.0)
1. **Task ontology extension** - Define 8 core actuarial tasks
2. **Reserving prompt template** - Most common task
3. **Reserve estimate schema** - Output validation
4. **Basic MCP server** - Enable tool calling

### Near-term (v0.9.0)
1. **Pricing and valuation templates** - Expand task coverage
2. **SHACL validation shapes** - Output quality assurance
3. **Reserving methods KB** - RAG content
4. **Python package alpha** - Developer access

### Medium-term (v1.0.0)
1. **Full task coverage** - All 8+ tasks operational
2. **Production MCP server** - Enterprise-ready
3. **Excel integration** - Actuary workflow
4. **Governance framework** - ASOP compliance

### Long-term (v2.0.0)
1. **Multi-agent workflows** - Complex projects
2. **Reasoning rules** - Automated inference
3. **Continuous learning** - Self-improvement
4. **Industry adoption** - Standards recognition

---

## Success Metrics

### AI Effectiveness
| Metric | Target |
|--------|--------|
| Task completion accuracy | >95% (vs actuary benchmark) |
| Time savings per task | >50% reduction |
| Judgment items correctly flagged | >99% |
| False positive rate | <5% |

### Adoption
| Metric | Target |
|--------|--------|
| Actuaries using AI tools | 1,000+ |
| Tasks completed with AI assist | 100,000+ |
| Organizations deployed | 50+ |
| Integration downloads | 10,000+ |

### Quality
| Metric | Target |
|--------|--------|
| SHACL validation pass rate | >98% |
| Actuary override rate | <10% |
| Audit findings | 0 critical |
| User satisfaction | >4.5/5 |

---

## Comparison: Traditional vs AI-First Approach

| Aspect | Traditional Ontology | AI-First Ontology |
|--------|---------------------|-------------------|
| **Primary user** | Semantic web developers | Actuaries via AI |
| **Success metric** | Completeness, consistency | Task completion, accuracy |
| **Validation** | Logical consistency | Output correctness |
| **Knowledge bases** | Comprehensive coverage | Task-relevant depth |
| **Tooling** | SPARQL endpoints | Function calling, MCP |
| **Documentation** | Technical reference | Prompt templates |

---

## Repository Structure

```
/actuarial-ontology/
  actuarial-ontology.ttl       # Core ontology

  /tasks/                       # Phase 1: Task frameworks
    task-ontology.ttl          # Task class definitions
    /prompts/                  # Prompt templates
    /schemas/                  # Output JSON schemas

  /knowledge-base/             # Phase 2: RAG content
    /concepts/
    /methods/
    /standards/
    /examples/

  /shapes/                     # Validation
    output-shapes.ttl          # AI output validation

  /mcp-server/                 # Phase 3: Tools
    server.py
    /tools/

  /packages/                   # Integrations
    /python/
    /excel/

  /governance/                 # Phase 4: Enterprise
    asop-compliance.md
    audit-requirements.md
```

---

## Contributing

Priority contribution areas:

1. **Prompt Engineering** - Improve task prompts
2. **Knowledge Content** - Add methods, examples
3. **Tool Development** - MCP tools, integrations
4. **Validation** - Test cases, benchmarks
5. **Domain Expertise** - Review AI outputs for accuracy

---

## Summary

This roadmap shifts focus from building a complete ontology to **building AI systems that empower actuaries**. The ontology is essential infrastructure, but the measure of success is:

> Can an actuary use AI to complete their work faster, more accurately, and with appropriate professional oversight?

Every phase, every deliverable should be evaluated against this question.

---

*This roadmap is a living document aligned with the vision of empowering actuaries with AI.*
