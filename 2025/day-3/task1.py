p = "test.txt"
ans = 0

with open(p, "rt") as f:
    arr = f.read().splitlines()

for line in arr:
    a = max(line)
    i = line.index(a)
    if i == len(line) - 1:
        mx = line[0]
        for x in line[:i]:
            mx = max(mx, x)
        num = int(mx + a)
    else:
        mx = line[i + 1]
        for x in line[i + 1 :]:
            mx = max(mx, x)
        num = int(a + mx)
    print(a, mx)
    ans += num

print(ans)
