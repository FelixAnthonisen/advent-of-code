from functools import cache

p = "input.txt"
ans = 0

with open(p, "rt") as f:
    arr = f.read().splitlines()

n, m = len(arr), len(arr[0])


@cache
def dfs(i, j):
    if i >= n or j >= m:
        return 1

    if arr[i][j] == "^":
        return dfs(i, j + 1) + dfs(i, j - 1)

    return dfs(i + 1, j)


j = arr[0].find("S")
ans = dfs(0, j)

print(ans)
