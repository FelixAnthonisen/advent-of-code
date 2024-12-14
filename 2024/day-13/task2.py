import re

p = "test.txt"
ans = 0

with open(p, "rt") as f:
    a = f.read().splitlines()

arr = []
for i in range(len(a) // 4 + 1):
    arr.append(a[4 * i : 4 * i + 3])


for i, entry in enumerate(arr):
    re1 = re.search(r"X\+(\d+), Y\+(\d+)", entry[0])
    re2 = re.search(r"X\+(\d+), Y\+(\d+)", entry[1])
    re3 = re.search(r"X\=(\d+), Y\=(\d+)", entry[2])

    ax, ay = int(re1.group(1)), int(re1.group(2))
    bx, by = int(re2.group(1)), int(re2.group(2))
    px, py = int(re3.group(1)) + int(1e13), int(re3.group(2)) + int(1e13)

    A = (px * by - py * bx) / (ax * by - ay * bx)
    B = (py - A * ay) / by
    if int(A) == A and int(B) == B:
        ans += 3 * A + B

print(int(ans))
