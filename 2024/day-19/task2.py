from functools import lru_cache

p = "input.txt"
ans = 0

with open(p, "rt") as f:
    arr = f.read().splitlines()

available = arr[0].split(", ")

print(available)


@lru_cache(maxsize=None)
def solve(line):
    if line == "":
        return 1
    res = 0
    for a in available:
        if len(a) > len(line) or a != line[: len(a)]:
            continue
        res += solve(line[len(a) :])
    return res


for line in arr[2:]:
    ans += solve(line)

print(ans)
