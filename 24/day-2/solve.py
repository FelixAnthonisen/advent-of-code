p = "input.txt"

with open(p, "rt") as f:
    arr = [[int(e) for e in x.split()] for x in f.read().splitlines()]

ans = 0
for l in arr:
    k = 0
    for e in range(len(l)):
        ld = l[:e] + l[e + 1 :]
        add = True
        b = ld[0] < ld[1]
        mn = 1 if b else -3
        mx = 3 if b else -1
        for i in range(len(ld) - 1):
            s = ld[i + 1] - ld[i]
            if s < mn or s > mx:
                add = False
        k = max(k, 1 if add else 0)
    ans += k

print(ans)
