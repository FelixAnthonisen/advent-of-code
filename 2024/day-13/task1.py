import re
from functools import lru_cache

p = "input.txt"
ans = 0

with open(p, "rt") as f:
    a = f.read().splitlines()

arr = []
for i in range(len(a) // 4):
    arr.append(a[4 * i : 4 * i + 3])


@lru_cache(maxsize=None)
def rec(x, y, ax, ay, bx, by, px, py, tot):
    if x > px or y > py or tot > 400:
        return 1000
    if x == px and y == py:
        return tot
    return min(
        rec(x + ax, y + ay, ax, ay, bx, by, px, py, tot + 3),
        rec(x + bx, y + by, ax, ay, bx, by, px, py, tot + 1),
    )


for i, entry in enumerate(arr):
    re1 = re.search(r"X\+(\d+), Y\+(\d+)", entry[0])
    re2 = re.search(r"X\+(\d+), Y\+(\d+)", entry[1])
    re3 = re.search(r"X\=(\d+), Y\=(\d+)", entry[2])

    ax, ay = int(re1.group(1)), int(re1.group(2))
    bx, by = int(re2.group(1)), int(re2.group(2))
    px, py = int(re3.group(1)), int(re3.group(2))

    res = rec(0, 0, ax, ay, bx, by, px, py, 0)
    if res != 1000:
        ans += res
    print(i / len(arr) * 100, "%")

print(ans)
