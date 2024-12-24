p = "input.txt"

with open(p, "rt") as f:
    arr = f.read().splitlines()

queries = []
b = False
for line in arr:
    if line == "":
        b = True
        continue
    if b:
        queries.append(line)

edges = ["strict digraph {"]

for query in queries:
    mem0, op, mem1, _, mem2 = query.split()
    edges.append(f"  {mem0} -> {mem2} [label={op}]")
    edges.append(f"  {mem1} -> {mem2} [label={op}]")

edges.append("}")

print("\n".join(edges))
