from functools import cache

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


@cache
def dfs(curr, a, b):
    if curr == "out":
        return a and b
    if curr == "fft":
        a = 1
    if curr == "dac":
        b = 1
    res = 0
    for n in adj[curr]:
        res += dfs(n, a, b)
    return res


print(adj)


print(dfs("svr", 0, 0))
