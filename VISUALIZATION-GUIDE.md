# Actuarial Ontology Visualization Guide

This guide explains how to visualize and explore the Actuarial Ontology.

## Overview

The Actuarial Ontology visualization suite provides four comprehensive views of the ontology structure:

1. **Class Hierarchy** - Complete taxonomic structure
2. **Relationship Diagram** - Key object properties and connections
3. **Domain Layers** - Domain-specific concept groupings
4. **Interactive HTML** - Browsable web interface

## Generated Visualizations

### 1. Class Hierarchy (`ontology_class_hierarchy.png`)

A comprehensive visualization showing all classes in the ontology with their inheritance relationships.

**Color Coding:**
- 🔴 **Red** - Foundational categories (Endurant, Perdurant, Moment)
- 🔵 **Teal** - UFO Kinds (rigid types like Person, Organization)
- 💚 **Light Teal** - UFO Roles (anti-rigid types like Actuary, Insurer)
- 🌸 **Pink** - UFO Phases (temporary states like Paid Claim)
- 💛 **Yellow** - UFO Moments (dependent properties)
- 💜 **Purple** - Risk concepts
- 🎀 **Pink** - Insurance concepts
- 🌊 **Blue** - Financial concepts
- ⭐ **Yellow** - Actuarial activities
- 🌲 **Green** - Models and data
- 🌺 **Light Pink** - Events and activities

### 2. Relationship Diagram (`ontology_relationships.png`)

Shows the most important object properties connecting classes.

**Features:**
- Directed arrows show relationship directions
- Edge labels display property names (e.g., "insures", "manages", "covers")
- Nodes colored by domain area for easy identification
- Focuses on core concepts for clarity

**Key Relationships Shown:**
- `Insurer → insures → Insured`
- `Agent → manages → Risk`
- `Insurance Policy → covers → Risk`
- `Claim → triggered by → Event`
- `Actuary → communicates → Actuarial Communication`
- Many more...

### 3. Domain Layers (`ontology_domain_layers.png`)

Six focused views showing different conceptual areas:

1. **UFO Foundational Layer** - Core ontological distinctions
   - Endurants, Perdurants, Moments
   - Entity, Agent, Object, Event, Activity

2. **Agent Types (Kinds & Roles)** - Who participates
   - Person, Organization, Actuary
   - Insurer, Insured, Regulator, etc.

3. **Risk Concepts (COVER)** - Risk theory
   - Three facets: Quantitative Risk, Risk Experience, Risk Assessment
   - Risk categories: Mortality, Property, Market, etc.
   - Dispositions and Vulnerabilities

4. **Insurance & Coverage** - Insurance domain
   - Products: Life, Health, Property
   - Contracts: Policies, Claims
   - Coverage elements: Exclusions, Deductibles, Limits

5. **Financial Concepts** - Financial theory
   - Assets, Liabilities, Capital
   - Reserves (Case, IBNR)
   - Premium, Loss

6. **Actuarial Activities & Models** - Actuarial practice
   - Activities: Pricing, Reserving, Valuation
   - Models: Pricing Model, Reserving Model, Capital Model
   - Communications: Reports, Opinions

### 4. Interactive HTML (`ontology_interactive.html`)

A browsable web interface for exploring the ontology.

**Features:**
- 📊 Statistics dashboard
- 🏷️ UFO categories legend
- 🌳 Expandable class hierarchy tree
- 🔗 Complete relationship listing
- Hover effects for easy navigation
- Responsive design

**To Use:**
Simply open `ontology_interactive.html` in any web browser.

## UFO Category System

The ontology uses UFO (Unified Foundational Ontology) meta-properties:

### Rigidity
- **Rigid** - Cannot change type while maintaining identity (e.g., Person)
- **Anti-rigid** - Can gain/lose type (e.g., Actuary, Insurer)
- **Semi-rigid** - Some instances can change (mixed)

### UFO Categories
- **Kind** - Rigid sortal providing identity principle
- **Role** - Anti-rigid relational type (depends on external relations)
- **Phase** - Anti-rigid intrinsic type (depends on intrinsic properties)
- **Moment** - Dependent property that inheres in another entity
- **Category** - General classification spanning multiple kinds

## COVER Integration

The ontology incorporates COVER (Common Ontology of Value and Risk) distinctions:

### Three Facets of Risk
1. **Quantitative Risk** - Risk as a numerical measure
2. **Risk Experience** - Risk as an event chain (threat → loss)
3. **Risk Assessment Judgment** - Risk as agent perception

### Event Chain
```
Peril → Threat Event → Loss Event → undermines → Risk Subject
```

### Value-Risk Relationship
- Value Objects enable Value Experiences
- Risk Enablers enable Threat/Loss Events
- Risk fundamentally intertwined with value

## ASOP Alignment

The ontology aligns with Actuarial Standards of Practice:

- **ASOP 41** - Actuarial Communications
  - Actuarial Communication, Actuarial Report, Actuarial Opinion
  - Intended User, Disclosure requirements

- **ASOP 36** - Statement of Actuarial Opinion

Classes include `asopReference` annotations linking to specific standards.

## Generating Visualizations

### Prerequisites
```bash
pip install -r requirements.txt
```

### Run Visualization Script
```bash
python3 visualize_ontology.py
```

### Dependencies
- `rdflib` - RDF/OWL parsing
- `networkx` - Graph structures
- `matplotlib` - Visualization rendering

## File Structure

```
Actuarial-Ontology/
├── actuarial-ontology.ttl          # Main ontology (Turtle format)
├── visualize_ontology.py           # Visualization generator
├── requirements.txt                # Python dependencies
├── VISUALIZATION-GUIDE.md          # This guide
├── ontology_class_hierarchy.png    # Generated: full hierarchy
├── ontology_relationships.png      # Generated: relationships
├── ontology_domain_layers.png      # Generated: domain views
└── ontology_interactive.html       # Generated: interactive viewer
```

## Understanding the Visualizations

### Reading the Class Hierarchy
1. Start with foundational categories (top level)
2. Follow arrows downward to see specializations
3. Note UFO categories to understand type stability
4. Color groups show domain clustering

### Reading the Relationships
1. Domain (source) on the left
2. Property (relationship) in the middle
3. Range (target) on the right
4. Arrows show directionality

### Using Domain Layers
Each layer is self-contained:
- Shows key classes for that domain
- Includes only internal relationships
- Use for focused understanding of specific areas

## Key Insights from Visualizations

1. **Foundational Structure**: Built on solid UFO foundation
2. **Role-Heavy Design**: Many anti-rigid roles (flexible typing)
3. **COVER Integration**: Clear separation of risk facets
4. **Insurance Focus**: Comprehensive insurance domain coverage
5. **Actuarial Practice**: Well-represented actuarial activities and models
6. **Standard Compliance**: ASOP concepts explicitly represented

## Tips for Exploration

1. **Start with Interactive HTML** for overview and navigation
2. **Use Class Hierarchy** to understand taxonomic structure
3. **Check Relationships** to see how concepts connect
4. **Explore Domain Layers** for focused area study
5. **Reference UFO/COVER** documentation for deeper understanding

## Future Enhancements

Potential visualization improvements:
- Interactive graph with zoom/pan
- Filtering by domain or UFO category
- SPARQL query interface
- OWL axiom visualization
- Competency question validation views
- Example instance diagrams

## Questions or Issues?

For questions about the ontology or visualizations, please refer to:
- `ONTOLOGY-DOCUMENTATION.md` - Ontology design documentation
- `STANDARDS-REVIEW.md` - Alignment with standards
- `README.md` - Project overview

---

**Last Updated**: 2026-01-11
**Version**: 0.2.0-draft
**Generated by**: visualize_ontology.py
