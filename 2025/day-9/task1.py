p = "input.txt"
ans = 0

with open(p, "rt") as f:
    points = f.read().splitlines()
    points = [[int(x) for x in y.split(",")] for y in points]

n = len(points)

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        ans = max(
            ans, (max(x1, x2) - min(x1, x2) + 1) * (max(y1, y2) - min(y1, y2) + 1)
        )

print(ans)
