import networkx as nx

p = "test.txt"
G = nx.Graph()

with open(p, "rt") as f:
    arr = f.read().splitlines()


for line in arr:
    v1, v2 = line.split("-")
    G.add_edge(v1, v2)

largest_clique = max(nx.algorithms.clique.find_cliques(G), key=len)

print(",".join(sorted(largest_clique)))
