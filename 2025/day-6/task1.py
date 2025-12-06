p = "input.txt"
ans = 0

with open(p, "rt") as f:
    arr = f.read().splitlines()
    nums = [[int(y) for y in x.split()] for x in arr[:-1]]
    ops = arr[-1].replace(" ", "")

for j in range(len(nums[0])):
    op = ops[j]
    tot = 0 if op == "+" else 1
    for i in range(len(nums)):
        num = nums[i][j]
        if op == "+":
            tot += num
        else:
            tot *= num
    ans += tot

print(ans)
