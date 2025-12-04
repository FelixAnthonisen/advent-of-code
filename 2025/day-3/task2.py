from functools import cache


@cache
def search(line, i, k):
    if i == len(line) and not k:
        return []
    if k < 0 or i == len(line):
        return None

    a = search(line, i + 1, k)
    b = search(line, i + 1, k - 1)
    if a is None and b is None:
        return None
    if a is None:
        return [line[i]] + b
    if b is None:
        return a
    return max(a, [line[i]] + b)


p = "input.txt"
ans = 0

with open(p, "rt") as f:
    arr = f.read().splitlines()

for line in arr:
    res = search(line, 0, 12)
    ans += int("".join(search(line, 0, 12)))

print(ans)
