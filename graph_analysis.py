import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E"),
    ("D", "F"),
    ("E", "F")
])

degree = nx.degree_centrality(G)
betweenness = nx.betweenness_centrality(G)

print("DEGREE CENTRALITY")
for node, value in degree.items():
    print(node, round(value, 2))

print("\nBETWEENNESS CENTRALITY")
for node, value in betweenness.items():
    print(node, round(value, 2))

communities = nx.community.louvain_communities(G, seed=42)

print("\nCOMMUNITIES")
for i, community in enumerate(communities, 1):
    print(f"Community {i}: {community}")

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1000,
    font_size=12
)

plt.title("Centrality and Community Detection")
plt.savefig("graph.png", dpi=300, bbox_inches="tight")
plt.show()
