p = "input.txt"
ans = 0

with open(p, "rt") as f:
    arr = f.read().splitlines()

ans = 0

for line in arr:
    a = line.split()
    l = int(a[0].split("x")[0])
    r = int(a[0].split("x")[1][:-1])
    tot = 0
    for x in a[1:]:
        x = int(x)
        tot += x
    if tot * 9 <= l * r:
        ans += 1

print(ans)
