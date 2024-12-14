# shameless brute force

p = "input.txt"
ans = 0

with open(p, "rt") as f:
    s = f.read()

arr = []

for i in range(len(s)):
    if i % 2:
        arr += int(s[i]) * ["."]
    else:
        arr += int(s[i]) * [i // 2]

j = len(arr) - 1
while j >= 0:
    if arr[j] == ".":
        j -= 1
        continue
    i = j
    while i > 0 and arr[i - 1] == arr[j]:
        i -= 1
    print(i, j)

    k, l = 0, 0
    y = j - i + 1

    for k in range(len(arr) - y):
        if k > i:
            break
        a = True
        for l in range(y):
            if arr[k + l] != ".":
                a = False
                break
        if not a:
            continue
        for l in range(y):
            arr[k + l] = arr[i + l]
            arr[i + l] = "."
    j = i - 1

ans = 0

for i, e in enumerate(arr):
    if e == ".":
        continue
    ans += i * e

print(ans)
