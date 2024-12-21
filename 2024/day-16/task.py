p = "input.txt"

with open(p, "rt") as f:
    arr = f.read().splitlines()

N, M = len(arr), len(arr[0])


def in_bounds(y, x):
    return y >= 0 and x >= 0 and y < N and x < M


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

start, end = None, None
for i in range(N):
    for j in range(M):
        if arr[i][j] == "S":
            start = (i, j)
        elif arr[i][j] == "E":
            end = (i, j)

dp = [[[int(1e9) for _ in range(4)] for _ in range(M)] for _ in range(N)]

dp[start[0]][start[1]][0] = 0

for _ in range(N * M * 4):
    updated = False
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            for d in range(4):
                if arr[i][j] == "#":
                    continue
                ni, nj = i + dirs[d][0], j + dirs[d][1]
                if arr[ni][nj] != "#":
                    new_cost = dp[i][j][d] + 1
                    if new_cost < dp[ni][nj][d]:
                        dp[ni][nj][d] = new_cost
                        updated = True

                if dp[i][j][(d + 1) % 4] > dp[i][j][d] + 1000:
                    dp[i][j][(d + 1) % 4] = dp[i][j][d] + 1000
                    updated = True
                if dp[i][j][(d + 3) % 4] > dp[i][j][d] + 1000:
                    dp[i][j][(d + 3) % 4] = dp[i][j][d] + 1000
                    updated = True
    if not updated:
        break

mn = min(dp[end[0]][end[1]])

print(mn)

vis = [[False for _ in range(M)] for _ in range(N)]


def dfs(i, j, d):
    if vis[i][j]:
        return

    vis[i][j] = True

    for turn in [0, 1, 2, 3]:
        new_d = (d + turn) % 4
        ni, nj = i - dirs[new_d][0], j - dirs[new_d][1]

        if in_bounds(ni, nj) and arr[ni][nj] != "#":
            expected_cost = dp[i][j][d] - (
                2001 if turn == 2 else 1001 if turn != 0 else 1
            )
            if dp[ni][nj][new_d] == expected_cost:
                dfs(ni, nj, new_d)


for d in range(4):
    if dp[end[0]][end[1]][d] == mn:
        dfs(end[0], end[1], d)

count_tiles = sum(sum(row) for row in vis)

print(count_tiles)
