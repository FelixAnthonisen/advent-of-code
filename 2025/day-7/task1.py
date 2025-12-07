p = "input.txt"
ans = 0

with open(p, "rt") as f:
    arr = f.read().splitlines()

n, m = len(arr), len(arr[0])

vis = set()


def dfs(i, j):
    if i >= n or j >= m or (i, j) in vis:
        return 0

    if arr[i][j] == "^":
        vis.add((i, j))
        return 1 + dfs(i, j + 1) + dfs(i, j - 1)

    return dfs(i + 1, j)


j = arr[0].find("S")
ans = dfs(0, j)

print(ans)
