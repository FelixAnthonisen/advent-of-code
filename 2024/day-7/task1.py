def rec(target, curr, arr, i):
    if i == len(arr):
        return target == curr
    return rec(target, curr + arr[i], arr, i + 1) or rec(
        target, curr * arr[i], arr, i + 1
    )


p = "input.txt"
ans = 0

with open(p, "rt") as f:
    arr = f.read().splitlines()

for line in arr:
    line = line.split()
    target = int(line[0][: len(line[0]) - 1])
    arr2 = [int(x) for x in line[1:]]
    if rec(target, arr2[0], arr2, 1):
        ans += target

print(ans)
