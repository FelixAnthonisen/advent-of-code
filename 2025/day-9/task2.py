p = "input.txt"
ans = 0

with open(p, "rt") as f:
    points = f.read().splitlines()
    points = [[int(x) for x in y.split(",")] for y in points]
n = len(points)


n = len(points)

edges = []
for i in range(n):
    p1 = points[i]
    p2 = points[(i + 1) % n]
    edges.append((p1, p2))

for i in range(n):
    for j in range(i + 1, n):
        p1 = points[i]
        p2 = points[j]

        l, r = min(p1[0], p2[0]), max(p1[0], p2[0])
        b, t = min(p1[1], p2[1]), max(p1[1], p2[1])

        e = 0
        for e1, e2 in edges:
            ex1, ex2 = min(e1[0], e2[0]), max(e1[0], e2[0])
            ey1, ey2 = min(e1[1], e2[1]), max(e1[1], e2[1])

            if ex1 == ex2:
                if l < ex1 < r and max(b, ey1) < min(t, ey2):
                    e = 1
                    break
            else:
                if b < ey1 < t and max(l, ex1) < min(r, ex2):
                    e = 1
                    break

        if e:
            continue

        ans = max(ans, (r - l + 1) * (t - b + 1))

print(ans)
