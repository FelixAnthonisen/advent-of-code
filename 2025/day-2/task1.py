p = "input.txt"
ans = 0

with open(p, "rt") as f:
    arr = f.read().split(",")

for x in arr:
    a, b = (int(y) for y in x.split("-"))
    for y in range(a, b + 1):
        y = str(y)
        l = len(y)
        if l % 2:
            continue
        ans += int(y) if y[: l // 2] == y[l // 2 :] else 0


print(ans)
