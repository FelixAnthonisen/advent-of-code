p = "input.txt"
ans = 0
curr = 50
with open(p, "rt") as f:
    arr = f.read().splitlines()

for line in arr:
    sign, num = line[0] == "R", int(line[1:])
    if sign:
        curr = (curr + num) % 100
    else:
        curr -= num
        while curr < 0:
            curr += 100
    ans += 0 if curr else 1

print(ans)
