p = "input.txt"
ans = 0
do = True


def consume(c, i, arr):
    if i >= len(arr):
        return False
    return arr[i] == c


def consume2(s, i, j, arr):
    if j > len(arr):
        return False
    if i >= j:
        return False
    return arr[i:j] == s


with open(p, "rt") as f:
    arr = f.read().splitlines()

for line in arr:
    for i in range(len(line) - 2):
        if consume2("do()", i, i + 4, line):
            do = True
            continue
        if consume2("don't()", i, i + 7, line):
            do = False
            continue
        if line[i : i + 3] == "mul" and do:
            j = i + 3
            if not consume("(", j, line):
                continue
            j += 1
            num = ""
            while True:
                try:
                    int(line[j])
                    num += line[j]
                    j += 1
                except:
                    break
            if not consume(",", j, line):
                continue
            j += 1
            num2 = ""
            while True:
                try:
                    int(line[j])
                    num2 += line[j]
                    j += 1
                except:
                    break
            if not consume(")", j, line):
                continue
            if len(num) == 0 or len(num2) == 0:
                continue
            ans += int(num) * int(num2)

print(ans)
