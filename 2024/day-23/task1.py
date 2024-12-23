import networkx as nx

p = "test.txt"
ans = 0
valid = set()
G = nx.Graph()

with open(p, "rt") as f:
    arr = f.read().splitlines()


for line in arr:
    v1, v2 = line.split("-")
    G.add_edge(v1, v2)

cliques = nx.algorithms.clique.find_cliques(G)
for clique in cliques:
    if len(clique) < 3:
        continue
    for i in range(len(clique)):
        for j in range(i + 1, len(clique)):
            for k in range(j + 1, len(clique)):
                if clique[i][0] == "t" or clique[j][0] == "t" or clique[k][0] == "t":
                    valid.add(",".join(sorted([clique[i], clique[j], clique[k]])))

print(len(valid))
