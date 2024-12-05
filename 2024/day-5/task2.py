from functools import cmp_to_key


def cmp(x, y):
    if x in m.keys() and y in m[x]:
        return -1
    elif y in m.keys() and x in m[y]:
        return 1
    else:
        return 0


p = "input.txt"
ans = 0
a = True
with open(p, "rt") as f:
    arr = f.read().splitlines()
m = dict()
for line in arr:
    if line == "":
        a = False
        continue
    if a:
        x, y = [int(x) for x in line.split("|")]
        if x not in m.keys():
            m[x] = set()
        m[x].add(y)
    else:
        line = [int(x) for x in line.split(",")]
        valid = True
        for i in range(len(line) - 1):
            if line[i + 1] in m.keys() and line[i] in m[line[i + 1]]:
                valid = False
                break
        if not valid:
            line = sorted(line, key=cmp_to_key(cmp))
            ans += line[len(line) // 2]

print(ans)
