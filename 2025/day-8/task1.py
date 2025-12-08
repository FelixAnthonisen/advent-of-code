ip = "test.txt"
ans = 1


def eucDist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2


def find(a):
    if p[a] == a:
        return a
    p[a] = find(p[a])
    return p[a]


def size(a):
    a = find(a)
    return sz[a]


def unite(a, b):
    a = find(a)
    b = find(b)
    p[b] = a
    sz[a] += sz[b]


with open(ip, "rt") as f:
    arr = f.read().splitlines()
    arr = [[int(x) for x in y.split(",")] for y in arr]

n = len(arr)
p = [i for i in range(n)]
sz = [1 for _ in range(n)]
dist = []

for i in range(n):
    for j in range(i + 1, n):
        dist.append([eucDist(arr[i], arr[j]), i, j])

dist = sorted(dist)
for _, a, b in dist[:1000]:
    if find(a) == find(b):
        continue
    unite(a, b)

szs = {}

for _, a, b in dist[:1000]:
    x = find(a)
    if x in szs.keys():
        continue
    szs[x] = size(x)

xxx = sorted(szs.values())[::-1][:3]

for x in xxx:
    ans *= x

print(ans)
