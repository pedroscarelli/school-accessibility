import networkx as nx
from networkx.algorithms.connectivity import local_node_connectivity

# 1. Adjacency list representing streets
streets = [
    ("A", "B"),
    ("A", "C"),
    ("B", "E"),
    ("B", "F"),
    ("C", "D"),
    ("C", "F"),
    ("D", "I"),
    ("D", "J"),
    ("E", "F"),
    ("F", "L"),
    ("G", "H"),
    ("G", "K"),
    ("H", "W"),
    ("I", "L"),
    ("I", "M"),
    ("J", "O"),
    ("J", "N"),
    ("K", "S"),
    ("K", "W"),
    ("L", "R"),
    ("M", "P"),
    ("N", "O"),
    ("N", "P"),
    ("P", "V"),
    ("Q", "V"),
    ("Q", "U"),
    ("S", "T"),
    ("R", "U"),
    ("R", "W"),
    ("T", "U"),
]

# 2. Building the graph
G = nx.Graph()
G.add_edges_from(streets)

# 3. Initial connectivity
print("Initial connectivity:")
print("Julia -> School:", local_node_connectivity(G, "A", "U"))
print("Rafaela -> School:", local_node_connectivity(G, "O", "U"))
print("Antonio -> School:", local_node_connectivity(G, "G", "U"))

# 4. Simulating floods
blocked_streets = [("R", "U"), ("R", "W"), ("T", "U")]
G.remove_edges_from(blocked_streets)

# 5. Connectivity after blockages
print("Connectivity after blocked streets:")
print("Julia -> School:", local_node_connectivity(G, "A", "U"))
print("Rafaela -> School:", local_node_connectivity(G, "O", "U"))
print("Antonio -> School:", local_node_connectivity(G, "G", "U"))
