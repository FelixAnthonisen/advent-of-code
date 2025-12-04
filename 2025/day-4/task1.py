import copy

p = "test.txt"
ans = 0

with open(p, "rt") as f:
    arr = f.read().splitlines()
    arr = [list(line) for line in arr]
n, m = len(arr), len(arr[0])


def ib(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < m


while 1:
    narr = copy.deepcopy(arr)
    nans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != "@":
                continue
            tot = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if ib(i + k, j + l, n, m):
                        tot += arr[i + k][j + l] == "@"
            if tot <= 4:
                narr[i][j] = "."
                nans += tot <= 4
    arr = narr
    if not nans:
        break
    ans += nans
print(ans)
