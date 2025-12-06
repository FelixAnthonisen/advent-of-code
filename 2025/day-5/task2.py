p = "input.txt"
ans = 0

with open(p, "rt") as f:
    arr = f.read().splitlines()

rangs = []
for j, line in enumerate(arr):
    if not line:
        break
    x, y = (int(z) for z in line.split("-"))
    rangs.append([x, y])

rangs = sorted(rangs)
nrangs = [rangs[0]]

for l, r in rangs[1:]:
    if l <= nrangs[-1][1]:
        nrangs[-1][1] = max(r, nrangs[-1][1])
    else:
        nrangs.append([l, r])

for l, r in nrangs:
    ans += r - l + 1

print(ans)
