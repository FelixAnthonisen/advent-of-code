p = "input.txt"
ans = 0

with open(p, "rt") as f:
    arr = f.read().splitlines()

s = set()
b = 0
rangs = []
for j, line in enumerate(arr):
    if not line:
        b = 1
        continue
    if not b:
        x, y = (int(z) for z in line.split("-"))
        rangs.append((x, y))
    else:
        x = int(line)
        for l, r in rangs:
            if l <= x <= r:
                ans += 1
                break

print(ans)
