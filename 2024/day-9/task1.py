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

i = 0
j = len(arr) - 1

while i < j:
    while arr[i] != "." and i < j:
        i += 1
    if i >= j:
        break
    arr[i] = arr[j]
    arr[j] = "."
    j -= 1

ans = 0

for i, e in enumerate(arr):
    if e == ".":
        break
    ans += i * e

print(ans)
