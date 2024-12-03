p = "input.txt"
ans = 0


def consume(c, i, arr):
    if i >= len(arr):
        return False
    return arr[i] == c


with open(p, "rt") as f:
    arr = f.read().splitlines()

for line in arr:
    for i in range(len(line) - 2):
        if line[i : i + 3] == "mul":
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
