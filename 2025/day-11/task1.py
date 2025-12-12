p = "input.txt"
ans = 0

adj = {}

with open(p, "rt") as f:
    arr = f.read().splitlines()
    for x in arr:
        x = x.split()
        adj[x[0][:-1]] = set()
        for y in x[1:]:
            adj[x[0][:-1]].add(y)


def dfs(curr):
    if curr == "out":
        return 1
    res = 0
    for n in adj[curr]:
        res += dfs(n)
    return res


print(adj)


print(dfs("you"))
