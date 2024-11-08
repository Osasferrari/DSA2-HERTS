import matplotlib.pyplot as plt
import networkx as nx

# Define the Union-Find (Disjoint Set Union) data structure
class UnionFind:
    def __init__(self, n):
        # Each node is initially its own parent
        self.parent = list(range(n))
        # Rank is used to keep the tree flat
        self.rank = [0] * n

    def find(self, u):
        # Path compression heuristic
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # Union by rank heuristic
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Attach smaller rank tree under root of higher rank tree
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True  # Union was successful
        return False  # Already in the same set

# Function to visualize the MST building process
def visualize_graph(graph, mst_edges, pos):
    plt.clf()
    # Draw all edges in light gray
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(), edge_color='lightgray', style='dashed')
    # Draw nodes
    nx.draw_networkx_nodes(graph, pos, node_color='skyblue', node_size=500)
    # Draw node labels
    nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold')
    # Draw edges in MST in blue
    nx.draw_networkx_edges(graph, pos, edgelist=mst_edges, edge_color='blue', width=2)
    # Draw edge weights
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title("Building the Minimum Spanning Tree")
    plt.axis('off')
    plt.pause(1)

def kruskal_mst(graph):
    # Initialize UnionFind
    uf = UnionFind(len(graph.nodes()))
    # Get all edges sorted by weight
    sorted_edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    mst_edges = []  # List to store edges in MST
    total_weight = 0
    # Position nodes for consistent layout
    pos = nx.spring_layout(graph, seed=42)
    print("Building the MST step-by-step:")
    for u, v, data in sorted_edges:
        u_idx = node_indices[u]
        v_idx = node_indices[v]
        if uf.union(u_idx, v_idx):
            # Edge can be added to MST
            mst_edges.append((u, v))
            total_weight += data['weight']
            print(f"Added edge {u} - {v} with weight {data['weight']}")
            visualize_graph(graph, mst_edges, pos)
    plt.show()
    return mst_edges, total_weight

# Define the graph
graph = nx.Graph()
# Define the nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
graph.add_nodes_from(nodes)
# Map nodes to indices for UnionFind
node_indices = {node: idx for idx, node in enumerate(nodes)}
# Add the edges with weights
edges = [
    ('A', 'B', 2),
    ('A', 'E', 7),
    ('A', 'C', 5),
    ('B', 'E', 1),
    ('B', 'D', 6),
    ('C', 'D', 3),
    ('C', 'F', 8),
    ('D', 'E', 4),
    ('E', 'F', 9)
]
graph.add_weighted_edges_from(edges)

# Run Kruskal's algorithm
mst_edges, total_weight = kruskal_mst(graph)

# Print the MST and its total weight
print("\nMinimum Spanning Tree:")
for u, v in mst_edges:
    weight = graph[u][v]['weight']
    print(f"{u} - {v}: {weight}")
print(f"Total weight of MST: {total_weight}")
