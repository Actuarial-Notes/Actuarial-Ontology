#!/usr/bin/env python3
"""
Actuarial Ontology Visualization Script
Generates beautiful visualizations of the actuarial ontology structure.
"""

import rdflib
from rdflib import Graph, Namespace, RDF, RDFS, OWL
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import defaultdict
import warnings
warnings.filterwarnings('ignore')

# Define namespaces
AO = Namespace("http://actuarialnotes.com/ontology/actuarial#")

def load_ontology(file_path):
    """Load the ontology from TTL file."""
    g = Graph()
    g.parse(file_path, format='turtle')
    return g

def extract_class_hierarchy(g):
    """Extract the class hierarchy from the ontology."""
    hierarchy = defaultdict(list)
    classes = set()

    # Get all classes
    for s in g.subjects(RDF.type, OWL.Class):
        classes.add(s)

    # Get subclass relationships
    for s, p, o in g.triples((None, RDFS.subClassOf, None)):
        if s in classes and o in classes:
            hierarchy[o].append(s)

    return hierarchy, classes

def get_label(g, uri):
    """Get the human-readable label for a URI."""
    for s, p, o in g.triples((uri, RDFS.label, None)):
        return str(o).replace('@en', '')
    # Fallback to local name
    return uri.split('#')[-1]

def get_ufo_category(g, uri):
    """Get the UFO category annotation if present."""
    for s, p, o in g.triples((uri, AO.ufoCategory, None)):
        return str(o).replace('@en', '')
    return None

def create_class_hierarchy_graph(g, hierarchy, classes):
    """Create a NetworkX directed graph for the class hierarchy."""
    G = nx.DiGraph()

    # Add all classes as nodes
    for cls in classes:
        label = get_label(g, cls)
        ufo_cat = get_ufo_category(g, cls)
        G.add_node(cls, label=label, ufo_category=ufo_cat)

    # Add edges for subclass relationships
    for parent, children in hierarchy.items():
        for child in children:
            G.add_edge(parent, child)

    return G

def assign_colors(G):
    """Assign colors based on UFO categories and top-level categories."""
    color_map = []
    for node in G.nodes():
        ufo_cat = G.nodes[node].get('ufo_category')
        label = G.nodes[node].get('label', '')

        # Top-level foundational categories
        if label in ['Endurant', 'Perdurant', 'Moment']:
            color_map.append('#FF6B6B')  # Red for top-level
        # UFO categories
        elif ufo_cat == 'kind':
            color_map.append('#4ECDC4')  # Teal for kinds
        elif ufo_cat == 'role':
            color_map.append('#95E1D3')  # Light teal for roles
        elif ufo_cat == 'phase':
            color_map.append('#F38181')  # Pink for phases
        elif ufo_cat == 'moment':
            color_map.append('#FFC75F')  # Yellow for moments
        # Risk-related
        elif 'Risk' in label:
            color_map.append('#AA96DA')  # Purple for risk
        # Insurance-related
        elif any(x in label for x in ['Insurance', 'Policy', 'Claim', 'Coverage']):
            color_map.append('#FCBAD3')  # Pink for insurance
        # Financial
        elif any(x in label for x in ['Asset', 'Liability', 'Capital', 'Premium', 'Reserve']):
            color_map.append('#A8D8EA')  # Blue for financial
        # Actuarial
        elif 'Actuarial' in label or label in ['Actuary', 'Pricing', 'Reserving', 'Valuation']:
            color_map.append('#FFD93D')  # Yellow for actuarial
        # Models and Data
        elif 'Model' in label or 'Data' in label:
            color_map.append('#6BCB77')  # Green for models/data
        # Events
        elif 'Event' in label or label in ['Activity']:
            color_map.append('#FFB6B9')  # Light pink for events
        # Default
        else:
            color_map.append('#E8E8E8')  # Gray for others

    return color_map

def create_hierarchical_layout(G):
    """Create a hierarchical layout for the graph."""
    # Find root nodes (nodes with no parents)
    roots = [n for n in G.nodes() if G.in_degree(n) == 0]

    if not roots:
        # If no clear roots, use all nodes as potential roots
        return nx.spring_layout(G, k=2, iterations=50, seed=42)

    # Use a more sophisticated layout
    try:
        pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
    except:
        # Fallback to spring layout if graphviz not available
        pos = nx.spring_layout(G, k=3, iterations=100, seed=42)

    return pos

def visualize_class_hierarchy(g, output_file='ontology_class_hierarchy.png', dpi=300):
    """Create a beautiful visualization of the class hierarchy."""
    hierarchy, classes = extract_class_hierarchy(g)
    G = create_class_hierarchy_graph(g, hierarchy, classes)

    # Create figure with high DPI
    plt.figure(figsize=(24, 18))

    # Create layout
    pos = create_hierarchical_layout(G)

    # Get colors
    colors = assign_colors(G)

    # Get labels
    labels = {node: G.nodes[node]['label'] for node in G.nodes()}

    # Draw the graph
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=1200,
                          alpha=0.9, linewidths=2, edgecolors='black')
    nx.draw_networkx_labels(G, pos, labels, font_size=7, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True,
                          arrowsize=15, arrowstyle='->', width=1.5,
                          alpha=0.6, connectionstyle='arc3,rad=0.1')

    # Create legend
    legend_elements = [
        mpatches.Patch(color='#FF6B6B', label='Foundational Categories'),
        mpatches.Patch(color='#4ECDC4', label='UFO Kinds'),
        mpatches.Patch(color='#95E1D3', label='UFO Roles'),
        mpatches.Patch(color='#F38181', label='UFO Phases'),
        mpatches.Patch(color='#FFC75F', label='UFO Moments'),
        mpatches.Patch(color='#AA96DA', label='Risk Concepts'),
        mpatches.Patch(color='#FCBAD3', label='Insurance'),
        mpatches.Patch(color='#A8D8EA', label='Financial'),
        mpatches.Patch(color='#FFD93D', label='Actuarial Activities'),
        mpatches.Patch(color='#6BCB77', label='Models & Data'),
        mpatches.Patch(color='#FFB6B9', label='Events & Activities'),
    ]

    plt.legend(handles=legend_elements, loc='upper left', fontsize=10,
              framealpha=0.9, edgecolor='black')

    plt.title('Actuarial Ontology - Class Hierarchy\nAligned with UFO, COVER, and ASOPs',
             fontsize=20, fontweight='bold', pad=20)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_file, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f"✓ Class hierarchy visualization saved to {output_file}")
    plt.close()

def extract_relationships(g):
    """Extract object properties and their relationships."""
    relationships = []

    for s, p, o in g.triples((None, RDF.type, OWL.ObjectProperty)):
        prop_label = get_label(g, s)

        # Get domain and range
        domain = None
        range_val = None

        for _, _, domain_o in g.triples((s, RDFS.domain, None)):
            domain = get_label(g, domain_o)

        for _, _, range_o in g.triples((s, RDFS.range, None)):
            range_val = get_label(g, range_o)

        if domain and range_val:
            relationships.append((domain, prop_label, range_val))

    return relationships

def create_relationship_graph(relationships):
    """Create a graph showing key relationships."""
    G = nx.DiGraph()

    for domain, prop, range_val in relationships:
        G.add_edge(domain, range_val, label=prop)

    return G

def visualize_key_relationships(g, output_file='ontology_relationships.png', dpi=300):
    """Visualize key relationships in the ontology."""
    relationships = extract_relationships(g)

    # Filter to most important relationships for clarity
    key_concepts = {
        'Agent', 'Actuary', 'Insurer', 'Insured', 'Risk', 'Insurance Policy',
        'Claim', 'Event', 'Loss', 'Reserve', 'Asset', 'Liability',
        'Actuarial Activity', 'Actuarial Model', 'Risk Assessment',
        'Pricing', 'Reserving', 'Threat Event', 'Loss Event', 'Risk Subject',
        'Value Object', 'Actuarial Communication', 'Intended User'
    }

    filtered_relationships = [
        (d, p, r) for d, p, r in relationships
        if d in key_concepts or r in key_concepts
    ]

    G = create_relationship_graph(filtered_relationships)

    # Create figure
    plt.figure(figsize=(20, 16))

    # Create layout
    try:
        pos = nx.spring_layout(G, k=3, iterations=100, seed=42)
    except:
        pos = nx.circular_layout(G)

    # Draw nodes with different colors for different types
    node_colors = []
    for node in G.nodes():
        if any(x in node for x in ['Risk', 'Peril', 'Threat', 'Loss']):
            node_colors.append('#AA96DA')
        elif any(x in node for x in ['Insurance', 'Policy', 'Claim', 'Coverage', 'Insured', 'Insurer']):
            node_colors.append('#FCBAD3')
        elif any(x in node for x in ['Asset', 'Liability', 'Reserve', 'Capital']):
            node_colors.append('#A8D8EA')
        elif any(x in node for x in ['Actuarial', 'Actuary', 'Pricing', 'Reserving', 'Valuation']):
            node_colors.append('#FFD93D')
        elif any(x in node for x in ['Model', 'Data']):
            node_colors.append('#6BCB77')
        elif 'Agent' in node:
            node_colors.append('#4ECDC4')
        elif 'Event' in node or 'Activity' in node:
            node_colors.append('#FFB6B9')
        else:
            node_colors.append('#E8E8E8')

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2000,
                          alpha=0.9, linewidths=2.5, edgecolors='black')
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')

    # Draw edges with labels
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True,
                          arrowsize=20, arrowstyle='->', width=2,
                          alpha=0.6, connectionstyle='arc3,rad=0.2')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=6,
                                font_color='red', bbox=dict(boxstyle='round,pad=0.3',
                                facecolor='white', edgecolor='none', alpha=0.7))

    # Legend
    legend_elements = [
        mpatches.Patch(color='#AA96DA', label='Risk Concepts'),
        mpatches.Patch(color='#FCBAD3', label='Insurance'),
        mpatches.Patch(color='#A8D8EA', label='Financial'),
        mpatches.Patch(color='#FFD93D', label='Actuarial'),
        mpatches.Patch(color='#6BCB77', label='Models & Data'),
        mpatches.Patch(color='#4ECDC4', label='Agents'),
        mpatches.Patch(color='#FFB6B9', label='Events'),
    ]

    plt.legend(handles=legend_elements, loc='upper left', fontsize=11,
              framealpha=0.9, edgecolor='black')

    plt.title('Actuarial Ontology - Key Relationships\nShowing Object Properties and Connections',
             fontsize=20, fontweight='bold', pad=20)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_file, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f"✓ Relationship visualization saved to {output_file}")
    plt.close()

def create_domain_layers_visualization(g, output_file='ontology_domain_layers.png', dpi=300):
    """Create a layered visualization showing different domain areas."""
    fig, axes = plt.subplots(2, 3, figsize=(24, 16))
    fig.suptitle('Actuarial Ontology - Domain Layers', fontsize=24, fontweight='bold', y=0.98)

    # Layer 1: UFO Foundational
    ax = axes[0, 0]
    ufo_classes = ['Endurant', 'Perdurant', 'Moment', 'Entity', 'Agent', 'Object', 'Event', 'Activity']
    create_domain_subgraph(g, ufo_classes, ax, 'UFO Foundational Layer', '#FF6B6B')

    # Layer 2: Agent Types (Kinds and Roles)
    ax = axes[0, 1]
    agent_classes = ['Person', 'Organization', 'Actuary', 'Insurer', 'Insured', 'Policyholder',
                     'Beneficiary', 'Reinsurer', 'Investor', 'Regulator', 'Risk Subject', 'Intended User']
    create_domain_subgraph(g, agent_classes, ax, 'Agent Types (Kinds & Roles)', '#4ECDC4')

    # Layer 3: Risk Concepts
    ax = axes[0, 2]
    risk_classes = ['Risk', 'Quantitative Risk', 'Risk Experience', 'Risk Assessment Judgment',
                   'Mortality Risk', 'Longevity Risk', 'Property Risk', 'Liability Risk',
                   'Market Risk', 'Catastrophe Risk', 'Disposition', 'Vulnerability']
    create_domain_subgraph(g, risk_classes, ax, 'Risk Concepts (COVER)', '#AA96DA')

    # Layer 4: Insurance & Coverage
    ax = axes[1, 0]
    insurance_classes = ['Insurance Product', 'Life Insurance', 'Health Insurance', 'Property Insurance',
                        'Insurance Policy', 'Claim', 'Reported Claim', 'Outstanding Claim', 'Paid Claim',
                        'Coverage', 'Exclusion', 'Deductible', 'Limit']
    create_domain_subgraph(g, insurance_classes, ax, 'Insurance & Coverage', '#FCBAD3')

    # Layer 5: Financial Concepts
    ax = axes[1, 1]
    financial_classes = ['Financial Instrument', 'Asset', 'Liability', 'Reserve', 'Claim Reserve',
                        'Case Reserve', 'IBNR Reserve', 'Premium', 'Loss', 'Capital',
                        'Economic Capital', 'Regulatory Capital']
    create_domain_subgraph(g, financial_classes, ax, 'Financial Concepts', '#A8D8EA')

    # Layer 6: Actuarial Work
    ax = axes[1, 2]
    actuarial_classes = ['Actuarial Activity', 'Risk Assessment', 'Pricing', 'Reserving', 'Valuation',
                        'Actuarial Model', 'Pricing Model', 'Reserving Model', 'Capital Model',
                        'Actuarial Communication', 'Actuarial Report', 'Actuarial Opinion']
    create_domain_subgraph(g, actuarial_classes, ax, 'Actuarial Activities & Models', '#FFD93D')

    plt.tight_layout()
    plt.savefig(output_file, dpi=dpi, bbox_inches='tight', facecolor='white')
    print(f"✓ Domain layers visualization saved to {output_file}")
    plt.close()

def create_domain_subgraph(g, class_labels, ax, title, color):
    """Create a subgraph for a specific domain."""
    hierarchy, all_classes = extract_class_hierarchy(g)

    # Find URIs for the given labels
    label_to_uri = {}
    for cls in all_classes:
        label = get_label(g, cls)
        if label in class_labels:
            label_to_uri[label] = cls

    # Create subgraph
    G = nx.DiGraph()
    for label, uri in label_to_uri.items():
        G.add_node(uri, label=label)

    # Add edges
    for parent, children in hierarchy.items():
        if parent in label_to_uri.values():
            for child in children:
                if child in label_to_uri.values():
                    G.add_edge(parent, child)

    if len(G.nodes()) == 0:
        ax.text(0.5, 0.5, 'No classes found', ha='center', va='center', fontsize=12)
        ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
        ax.axis('off')
        return

    # Layout
    if len(G.nodes()) > 1:
        try:
            pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
        except:
            pos = nx.circular_layout(G)
    else:
        pos = {list(G.nodes())[0]: (0.5, 0.5)}

    # Draw
    labels = {node: G.nodes[node]['label'] for node in G.nodes()}
    nx.draw_networkx_nodes(G, pos, node_color=color, node_size=800,
                          alpha=0.9, linewidths=2, edgecolors='black', ax=ax)
    nx.draw_networkx_labels(G, pos, labels, font_size=7, font_weight='bold', ax=ax)

    if len(G.edges()) > 0:
        nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True,
                              arrowsize=10, arrowstyle='->', width=1.5,
                              alpha=0.6, connectionstyle='arc3,rad=0.1', ax=ax)

    ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
    ax.axis('off')

def generate_html_visualization(g, output_file='ontology_interactive.html'):
    """Generate an interactive HTML visualization."""
    hierarchy, classes = extract_class_hierarchy(g)
    relationships = extract_relationships(g)

    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Actuarial Ontology - Interactive Visualization</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 30px;
            font-size: 1.1em;
        }
        .section {
            margin-bottom: 40px;
        }
        h2 {
            color: #34495e;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .class-tree {
            font-family: 'Courier New', monospace;
            line-height: 1.8;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
            overflow-x: auto;
        }
        .class-item {
            margin-left: 20px;
            padding: 5px;
            border-left: 2px solid #ddd;
        }
        .class-item:hover {
            background: #e8f4f8;
            border-left-color: #3498db;
        }
        .ufo-kind { color: #16a085; font-weight: bold; }
        .ufo-role { color: #2980b9; font-style: italic; }
        .ufo-phase { color: #8e44ad; font-style: italic; }
        .ufo-moment { color: #f39c12; }
        .ufo-category { color: #c0392b; font-weight: bold; }
        .relationship {
            padding: 10px;
            margin: 5px 0;
            background: #ecf0f1;
            border-radius: 5px;
            display: flex;
            align-items: center;
        }
        .domain {
            background: #3498db;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-weight: bold;
            min-width: 150px;
            text-align: center;
        }
        .property {
            background: #e74c3c;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            margin: 0 10px;
            font-style: italic;
        }
        .range {
            background: #2ecc71;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-weight: bold;
            min-width: 150px;
            text-align: center;
        }
        .arrow { margin: 0 10px; font-size: 1.5em; color: #7f8c8d; }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .stat-number {
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .stat-label {
            font-size: 1.1em;
            opacity: 0.9;
        }
        .legend {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-top: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
        }
        .legend-item {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎓 Actuarial Ontology</h1>
        <div class="subtitle">
            A comprehensive ontology for actuarial science<br>
            Aligned with UFO (Unified Foundational Ontology), COVER (Common Ontology of Value and Risk), and ASOPs (Actuarial Standards of Practice)
        </div>
"""

    # Add statistics
    num_classes = len(classes)
    num_relationships = len(relationships)

    html_content += f"""
        <div class="section">
            <h2>📊 Ontology Statistics</h2>
            <div class="stats">
                <div class="stat-card">
                    <div class="stat-number">{num_classes}</div>
                    <div class="stat-label">Classes</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{num_relationships}</div>
                    <div class="stat-label">Relationships</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{len(hierarchy)}</div>
                    <div class="stat-label">Parent Classes</div>
                </div>
            </div>
        </div>
"""

    # Add UFO legend
    html_content += """
        <div class="section">
            <h2>🏷️ UFO Categories Legend</h2>
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color" style="background: #16a085;"></div>
                    <span><strong>Kind</strong> - Rigid sortals providing identity</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #2980b9;"></div>
                    <span><strong>Role</strong> - Anti-rigid relational types</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #8e44ad;"></div>
                    <span><strong>Phase</strong> - Anti-rigid intrinsic types</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #f39c12;"></div>
                    <span><strong>Moment</strong> - Dependent properties</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #c0392b;"></div>
                    <span><strong>Category</strong> - General classifications</span>
                </div>
            </div>
        </div>
"""

    # Add class hierarchy
    html_content += """
        <div class="section">
            <h2>🌳 Class Hierarchy</h2>
            <div class="class-tree">
"""

    # Build tree structure
    def add_class_to_html(cls, level=0):
        label = get_label(g, cls)
        ufo_cat = get_ufo_category(g, cls)

        indent = "  " * level
        css_class = f"ufo-{ufo_cat}" if ufo_cat else ""

        html = f'{indent}<div class="class-item"><span class="{css_class}">{label}</span>'
        if ufo_cat:
            html += f' <small style="color: #7f8c8d;">({ufo_cat})</small>'
        html += '</div>\n'

        # Add children
        if cls in hierarchy:
            for child in sorted(hierarchy[cls], key=lambda x: get_label(g, x)):
                html += add_class_to_html(child, level + 1)

        return html

    # Find root classes
    all_children = set()
    for children in hierarchy.values():
        all_children.update(children)
    roots = [cls for cls in classes if cls not in all_children]

    for root in sorted(roots, key=lambda x: get_label(g, x)):
        html_content += add_class_to_html(root)

    html_content += """
            </div>
        </div>
"""

    # Add key relationships
    html_content += """
        <div class="section">
            <h2>🔗 Key Relationships (Object Properties)</h2>
"""

    for domain, prop, range_val in sorted(relationships[:30]):  # Show first 30
        html_content += f"""
            <div class="relationship">
                <span class="domain">{domain}</span>
                <span class="arrow">→</span>
                <span class="property">{prop}</span>
                <span class="arrow">→</span>
                <span class="range">{range_val}</span>
            </div>
"""

    html_content += """
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

    # Load ontology
    print("Loading ontology from actuarial-ontology.ttl...")
    g = load_ontology('actuarial-ontology.ttl')
    print(f"✓ Loaded ontology with {len(g)} triples")
    print()

    # Generate visualizations
    print("Generating visualizations...")
    print()

    visualize_class_hierarchy(g)
    visualize_key_relationships(g)
    create_domain_layers_visualization(g)
    generate_html_visualization(g)

    print()
    print("=" * 60)
    print("  All visualizations generated successfully!")
    print("=" * 60)
    print()
    print("Generated files:")
    print("  1. ontology_class_hierarchy.png - Complete class hierarchy")
    print("  2. ontology_relationships.png - Key relationships diagram")
    print("  3. ontology_domain_layers.png - Domain-specific layers")
    print("  4. ontology_interactive.html - Interactive HTML viewer")
    print()

if __name__ == '__main__':
    main()
