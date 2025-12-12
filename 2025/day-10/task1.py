from collections import deque

p = "input.txt"
ans = 0

with open(p, "rt") as f:
    arr = [x.split() for x in f.read().splitlines()]

schema = ["".join(["0" if y == "." else "1" for y in x[0][1:-1]]) for x in arr]
buttons = [[[int(k) for k in y[1:-1].split(",")] for y in x[1:-1]] for x in arr]


def bfs(i):
    curr = ""
    for _ in range(len(schema[i])):
        curr += "0"

    q = deque([(curr, 0)])

    vis = set()

    while len(q):
        curr, d = q.popleft()
        if curr == schema[i]:
            return d
        if curr in vis:
            continue
        for b in buttons[i]:
            ncurr = ""
            for j in range(len(curr)):
                if j in b:
                    ncurr += "0" if curr[j] == "1" else "1"
                else:
                    ncurr += curr[j]
            q.append((ncurr, d + 1))


for i in range(len(schema)):
    print(i)
    ans += bfs(i)

print(ans)

print("done")
