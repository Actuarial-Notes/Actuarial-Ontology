#!/usr/bin/env python3
"""
Actuarial Ontology Visualization Script
Generates a clear, legible visualization of the ontology domain structure.
"""

import rdflib
from rdflib import Graph, Namespace, RDF, RDFS, OWL
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import warnings
warnings.filterwarnings('ignore')

# Define namespaces
AO = Namespace("http://actuarialnotes.com/ontology/actuarial#")

def load_ontology(file_path):
    """Load the ontology from TTL file."""
    g = Graph()
    g.parse(file_path, format='turtle')
    return g

def get_label(g, uri):
    """Get the human-readable label for a URI."""
    for s, p, o in g.triples((uri, RDFS.label, None)):
        return str(o).replace('@en', '')
    return uri.split('#')[-1]

def create_domain_visualization(g, output_file='ontology_visualization.png', dpi=150):
    """Create a single, clear domain-based visualization."""

    # Define domain structure with key concepts
    domains = {
        'UFO Foundation': {
            'color': '#FF6B6B',
            'concepts': ['Endurant', 'Perdurant', 'Moment', 'Entity', 'Agent', 'Event', 'Activity'],
            'description': 'Core ontological categories'
        },
        'Agents & Roles': {
            'color': '#4ECDC4',
            'concepts': ['Person', 'Organization', 'Actuary', 'Insurer', 'Insured', 'Regulator', 'Risk Subject'],
            'description': 'Who participates in actuarial contexts'
        },
        'Risk Concepts': {
            'color': '#9B59B6',
            'concepts': ['Risk', 'Quantitative Risk', 'Risk Experience', 'Risk Assessment', 'Threat Event', 'Loss Event'],
            'description': 'COVER risk facets and classifications'
        },
        'Insurance': {
            'color': '#E91E63',
            'concepts': ['Insurance Policy', 'Claim', 'Coverage', 'Reserve', 'Premium', 'Deductible'],
            'description': 'Insurance products and contracts'
        },
        'Financial': {
            'color': '#3498DB',
            'concepts': ['Asset', 'Liability', 'Capital', 'Loss', 'Financial Measurement', 'Reserve'],
            'description': 'Financial instruments and metrics'
        },
        'Actuarial Practice': {
            'color': '#F39C12',
            'concepts': ['Pricing', 'Reserving', 'Valuation', 'Actuarial Model', 'Actuarial Communication', 'Risk Assessment'],
            'description': 'Activities, models, and standards'
        }
    }

    # Create figure
    fig = plt.figure(figsize=(20, 14))
    ax = fig.add_subplot(111)

    # Title
    fig.suptitle('Actuarial Ontology',
                 fontsize=32, fontweight='bold', y=0.98)
    ax.text(0.5, 0.96, 'Domain Structure aligned with UFO, COVER, and ASOPs',
            ha='center', va='top', transform=ax.transAxes,
            fontsize=16, style='italic', color='#555')

    # Layout parameters
    box_width = 0.28
    box_height = 0.26
    x_margin = 0.05
    y_margin = 0.02
    x_gap = 0.03
    y_gap = 0.04

    # Calculate positions (3 columns, 2 rows)
    positions = [
        (x_margin, 0.66),                           # Row 1, Col 1
        (x_margin + box_width + x_gap, 0.66),       # Row 1, Col 2
        (x_margin + 2*(box_width + x_gap), 0.66),   # Row 1, Col 3
        (x_margin, 0.34),                           # Row 2, Col 1
        (x_margin + box_width + x_gap, 0.34),       # Row 2, Col 2
        (x_margin + 2*(box_width + x_gap), 0.34),   # Row 2, Col 3
    ]

    domain_names = list(domains.keys())

    for idx, (domain_name, pos) in enumerate(zip(domain_names, positions)):
        domain = domains[domain_name]
        x, y = pos

        # Draw domain box
        box = FancyBboxPatch(
            (x, y), box_width, box_height,
            boxstyle="round,pad=0.01",
            facecolor=domain['color'],
            edgecolor='black',
            linewidth=2.5,
            alpha=0.15,
            transform=ax.transAxes,
            zorder=1
        )
        ax.add_patch(box)

        # Domain title
        ax.text(x + box_width/2, y + box_height - 0.02,
                domain_name,
                ha='center', va='top',
                fontsize=18, fontweight='bold',
                color=domain['color'],
                transform=ax.transAxes,
                zorder=3)

        # Description
        ax.text(x + box_width/2, y + box_height - 0.05,
                domain['description'],
                ha='center', va='top',
                fontsize=11, style='italic',
                color='#666',
                transform=ax.transAxes,
                zorder=3)

        # Concepts (arranged vertically)
        concepts = domain['concepts'][:7]  # Limit to 7 for space
        concept_y_start = y + box_height - 0.09
        concept_spacing = (box_height - 0.11) / max(len(concepts), 1)

        for i, concept in enumerate(concepts):
            concept_y = concept_y_start - i * concept_spacing

            # Concept bubble
            concept_box = FancyBboxPatch(
                (x + 0.02, concept_y - 0.015),
                box_width - 0.04, 0.028,
                boxstyle="round,pad=0.005",
                facecolor='white',
                edgecolor=domain['color'],
                linewidth=1.8,
                alpha=0.95,
                transform=ax.transAxes,
                zorder=2
            )
            ax.add_patch(concept_box)

            # Concept text
            ax.text(x + box_width/2, concept_y,
                    concept,
                    ha='center', va='center',
                    fontsize=12, fontweight='normal',
                    color='#222',
                    transform=ax.transAxes,
                    zorder=3)

    # Add key relationships as arrows
    relationships = [
        # (from_domain_idx, to_domain_idx, label)
        (1, 2, 'exposed to'),     # Agents → Risk
        (1, 3, 'holds'),          # Agents → Insurance
        (2, 3, 'covered by'),     # Risk → Insurance
        (3, 4, 'backed by'),      # Insurance → Financial
        (5, 2, 'assesses'),       # Actuarial → Risk
        (5, 3, 'prices'),         # Actuarial → Insurance
    ]

    for from_idx, to_idx, label in relationships:
        from_x, from_y = positions[from_idx]
        to_x, to_y = positions[to_idx]

        # Calculate arrow positions
        from_center_x = from_x + box_width/2
        from_center_y = from_y + box_height/2
        to_center_x = to_x + box_width/2
        to_center_y = to_y + box_height/2

        # Create arrow
        arrow = FancyArrowPatch(
            (from_center_x, from_center_y),
            (to_center_x, to_center_y),
            transform=ax.transAxes,
            arrowstyle='->,head_width=0.4,head_length=0.4',
            color='#999',
            linewidth=2,
            alpha=0.4,
            zorder=0,
            connectionstyle="arc3,rad=0.2"
        )
        ax.add_patch(arrow)

        # Arrow label
        mid_x = (from_center_x + to_center_x) / 2
        mid_y = (from_center_y + to_center_y) / 2
        ax.text(mid_x, mid_y, label,
                ha='center', va='center',
                fontsize=9, style='italic',
                color='#666',
                bbox=dict(boxstyle='round,pad=0.3',
                         facecolor='white',
                         edgecolor='none',
                         alpha=0.8),
                transform=ax.transAxes,
                zorder=1)

    # Add legend at bottom
    legend_y = 0.12
    ax.text(0.5, legend_y, 'Alignment & Standards',
            ha='center', va='top',
            fontsize=14, fontweight='bold',
            color='#333',
            transform=ax.transAxes)

    standards = [
        ('UFO', 'Unified Foundational Ontology - ontological categories'),
        ('COVER', 'Common Ontology of Value and Risk - risk facets'),
        ('ASOPs', 'Actuarial Standards of Practice - professional standards')
    ]

    for i, (name, desc) in enumerate(standards):
        y_pos = legend_y - 0.04 - i * 0.03
        ax.text(0.5, y_pos, f'• {name}: {desc}',
                ha='center', va='top',
                fontsize=11,
                color='#555',
                transform=ax.transAxes)

    # Statistics
    from collections import defaultdict
    hierarchy = defaultdict(list)
    classes = set()
    for s in g.subjects(RDF.type, OWL.Class):
        classes.add(s)
    for s, p, o in g.triples((None, RDFS.subClassOf, None)):
        if s in classes and o in classes:
            hierarchy[o].append(s)

    relationships_count = len(list(g.subjects(RDF.type, OWL.ObjectProperty)))

    stats_text = f'{len(classes)} Classes  •  {relationships_count} Relationships  •  {len(hierarchy)} Parent Classes'
    ax.text(0.5, 0.02,
            stats_text,
            ha='center', va='bottom',
            fontsize=12,
            color='#888',
            transform=ax.transAxes)

    # Remove axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(output_file, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f"✓ Ontology visualization saved to {output_file}")
    plt.close()

def generate_html_visualization(g, output_file='ontology_interactive.html'):
    """Generate an interactive HTML visualization."""
    from collections import defaultdict

    hierarchy = defaultdict(list)
    classes = set()

    for s in g.subjects(RDF.type, OWL.Class):
        classes.add(s)

    for s, p, o in g.triples((None, RDFS.subClassOf, None)):
        if s in classes and o in classes:
            hierarchy[o].append(s)

    relationships = []
    for s in g.subjects(RDF.type, OWL.ObjectProperty):
        prop_label = get_label(g, s)
        domain = None
        range_val = None

        for _, _, domain_o in g.triples((s, RDFS.domain, None)):
            domain = get_label(g, domain_o)

        for _, _, range_o in g.triples((s, RDFS.range, None)):
            range_val = get_label(g, range_o)

        if domain and range_val:
            relationships.append((domain, prop_label, range_val))

    def get_ufo_category(uri):
        for s, p, o in g.triples((uri, AO.ufoCategory, None)):
            return str(o).replace('@en', '')
        return None

    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Actuarial Ontology - Interactive Explorer</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }
        .container {
            max-width: 1600px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }
        .header h1 {
            font-size: 3em;
            margin-bottom: 10px;
            font-weight: 700;
        }
        .header p {
            font-size: 1.2em;
            opacity: 0.95;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 0;
            background: #f8f9fa;
            border-bottom: 3px solid #e0e0e0;
        }
        .stat {
            padding: 30px;
            text-align: center;
            border-right: 1px solid #e0e0e0;
        }
        .stat:last-child { border-right: none; }
        .stat-number {
            font-size: 3em;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 10px;
        }
        .stat-label {
            font-size: 1.1em;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 600;
        }
        .content {
            padding: 40px;
        }
        .section {
            margin-bottom: 50px;
        }
        h2 {
            font-size: 2em;
            color: #2c3e50;
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 4px solid #667eea;
        }
        .domains {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }
        .domain {
            background: white;
            border: 3px solid;
            border-radius: 15px;
            padding: 25px;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .domain:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }
        .domain-title {
            font-size: 1.5em;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .domain-desc {
            font-style: italic;
            color: #666;
            margin-bottom: 20px;
            font-size: 1.05em;
        }
        .concept-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .concept {
            background: white;
            border: 2px solid;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.95em;
            font-weight: 500;
            transition: transform 0.2s;
        }
        .concept:hover {
            transform: scale(1.05);
        }
        .relationships {
            display: grid;
            gap: 15px;
            margin-top: 20px;
        }
        .relationship {
            display: flex;
            align-items: center;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            border-left: 5px solid #667eea;
            flex-wrap: wrap;
            gap: 15px;
        }
        .rel-domain {
            background: #3498db;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: bold;
            min-width: 160px;
            text-align: center;
        }
        .rel-arrow {
            font-size: 1.5em;
            color: #999;
        }
        .rel-prop {
            background: #e74c3c;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-style: italic;
            min-width: 140px;
            text-align: center;
        }
        .rel-range {
            background: #2ecc71;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: bold;
            min-width: 160px;
            text-align: center;
        }
        .legend {
            background: #f8f9fa;
            padding: 30px;
            border-radius: 15px;
            margin-top: 20px;
        }
        .legend h3 {
            font-size: 1.5em;
            margin-bottom: 20px;
            color: #2c3e50;
        }
        .legend-items {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 15px;
        }
        .legend-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px;
            background: white;
            border-radius: 8px;
        }
        .legend-color {
            width: 30px;
            height: 30px;
            border-radius: 6px;
            border: 2px solid #333;
        }
        .legend-text {
            font-size: 1.05em;
        }
        .legend-text strong {
            display: block;
            margin-bottom: 3px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎓 Actuarial Ontology</h1>
            <p>A comprehensive ontology for actuarial science<br>
            Aligned with UFO, COVER, and ASOPs</p>
        </div>

        <div class="stats">
            <div class="stat">
                <div class="stat-number">""" + str(len(classes)) + """</div>
                <div class="stat-label">Classes</div>
            </div>
            <div class="stat">
                <div class="stat-number">""" + str(len(relationships)) + """</div>
                <div class="stat-label">Relationships</div>
            </div>
            <div class="stat">
                <div class="stat-number">""" + str(len(hierarchy)) + """</div>
                <div class="stat-label">Parent Classes</div>
            </div>
        </div>

        <div class="content">
            <div class="section">
                <h2>📚 Domain Structure</h2>
                <div class="domains">
"""

    # Add domain boxes
    domain_configs = [
        ('UFO Foundation', '#FF6B6B',
         ['Endurant', 'Perdurant', 'Moment', 'Entity', 'Agent', 'Event', 'Activity'],
         'Core ontological categories'),
        ('Agents & Roles', '#4ECDC4',
         ['Person', 'Organization', 'Actuary', 'Insurer', 'Insured', 'Regulator', 'Risk Subject'],
         'Who participates in actuarial contexts'),
        ('Risk Concepts', '#9B59B6',
         ['Risk', 'Quantitative Risk', 'Risk Experience', 'Risk Assessment', 'Threat Event', 'Loss Event'],
         'COVER risk facets and classifications'),
        ('Insurance', '#E91E63',
         ['Insurance Policy', 'Claim', 'Coverage', 'Reserve', 'Premium', 'Deductible'],
         'Insurance products and contracts'),
        ('Financial', '#3498DB',
         ['Asset', 'Liability', 'Capital', 'Loss', 'Financial Measurement', 'Reserve'],
         'Financial instruments and metrics'),
        ('Actuarial Practice', '#F39C12',
         ['Pricing', 'Reserving', 'Valuation', 'Actuarial Model', 'Actuarial Communication', 'Risk Assessment'],
         'Activities, models, and standards'),
    ]

    for name, color, concepts, desc in domain_configs:
        html_content += f"""
                    <div class="domain" style="border-color: {color};">
                        <div class="domain-title" style="color: {color};">{name}</div>
                        <div class="domain-desc">{desc}</div>
                        <div class="concept-list">
"""
        for concept in concepts:
            html_content += f'                            <div class="concept" style="border-color: {color}; color: {color};">{concept}</div>\n'

        html_content += """                        </div>
                    </div>
"""

    html_content += """
                </div>
            </div>

            <div class="section">
                <h2>🔗 Key Relationships</h2>
                <div class="relationships">
"""

    # Add top 20 relationships
    for domain, prop, range_val in sorted(relationships[:20]):
        html_content += f"""
                    <div class="relationship">
                        <div class="rel-domain">{domain}</div>
                        <div class="rel-arrow">→</div>
                        <div class="rel-prop">{prop}</div>
                        <div class="rel-arrow">→</div>
                        <div class="rel-range">{range_val}</div>
                    </div>
"""

    html_content += """
                </div>
            </div>

            <div class="legend">
                <h3>🏷️ Standards & Alignment</h3>
                <div class="legend-items">
                    <div class="legend-item">
                        <div class="legend-color" style="background: #FF6B6B;"></div>
                        <div class="legend-text">
                            <strong>UFO</strong>
                            Unified Foundational Ontology
                        </div>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color" style="background: #9B59B6;"></div>
                        <div class="legend-text">
                            <strong>COVER</strong>
                            Common Ontology of Value and Risk
                        </div>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color" style="background: #F39C12;"></div>
                        <div class="legend-text">
                            <strong>ASOPs</strong>
                            Actuarial Standards of Practice
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ Interactive HTML visualization saved to {output_file}")

def main():
    print("=" * 60)
    print("  Actuarial Ontology Visualization Generator")
    print("=" * 60)
    print()

    print("Loading ontology from actuarial-ontology.ttl...")
    g = load_ontology('actuarial-ontology.ttl')
    print(f"✓ Loaded ontology with {len(g)} triples")
    print()

    print("Generating visualizations...")
    print()

    create_domain_visualization(g)
    generate_html_visualization(g)

    print()
    print("=" * 60)
    print("  Visualization complete!")
    print("=" * 60)
    print()
    print("Generated files:")
    print("  1. ontology_visualization.png - Clear domain structure")
    print("  2. ontology_interactive.html - Interactive web explorer")
    print()

if __name__ == '__main__':
    main()
