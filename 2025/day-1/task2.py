p = "test.txt"
ans = 0
curr = 50
with open(p, "rt") as f:
    arr = f.read().splitlines()

for line in arr:
    sign, num = line[0] == "R", int(line[1:])
    for _ in range(num):
        curr += 1 if sign else -1
        if not (curr % 100):
            ans += 1

print(ans)
