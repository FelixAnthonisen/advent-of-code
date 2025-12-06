p = "input.txt"
ans = 0


def transpose(arr):
    narr = []
    for j in range(len(arr[0])):
        narr.append([])
        for i in range(len(arr)):
            narr[-1].append(arr[i][j])
    return narr


with open(p, "rt") as f:
    arr = f.read().splitlines()
    nums = transpose([x for x in arr[:-1]])
    ops = arr[-1].replace(" ", "")

j = 0
for i in range(len(ops)):
    op = ops[i]
    tot = 0 if op == "+" else 1
    while 1:
        if j == len(nums):
            break
        num = "".join(nums[j]).replace(" ", "")
        if not num:
            j += 1
            break

        num = int(num)
        if op == "+":
            tot += num
        else:
            tot *= num
        j += 1
    ans += tot

print(ans)
