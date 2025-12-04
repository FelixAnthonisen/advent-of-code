p = "input.txt"
ans = 0


def all_eq(arr):
    init = arr[0]
    for a in arr:
        if a != init:
            return 0
    return 1


with open(p, "rt") as f:
    arr = f.read().split(",")

for x in arr:
    a, b = (int(y) for y in x.split("-"))
    for y in range(a, b + 1):
        y = str(y)
        l = len(y)
        for k in range(2, l + 1):
            if l % k:
                continue
            r = l // k
            ars = [y[r * i : r * i + r] for i in range(k)]
            if all_eq(ars):
                ans += int(y)
                break


print(ans)
