from functools import lru_cache


curr = ["A"] * 26
p = "input.txt"
ans = 0

numerical = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]

directional = [
    [None, "^", "A"],
    ["<", "v", ">"],
]

num_indicies = {
    value: (i, j) for i, row in enumerate(numerical) for j, value in enumerate(row)
}

dir_indicies = {
    value: (i, j) for i, row in enumerate(directional) for j, value in enumerate(row)
}


def best_path(s, curr_char, target_char, is_num_pad):
    ci, cj = num_indicies[curr_char] if is_num_pad else dir_indicies[curr_char]
    ti, tj = num_indicies[target_char] if is_num_pad else dir_indicies[target_char]

    a, b = cj - tj, ci - ti
    horisontal = (">" if a < 0 else "<") * abs(a)
    vertical = ("v" if b < 0 else "^") * abs(b)

    s2 = s + horisontal + vertical + "A"
    s3 = s + vertical + horisontal + "A"

    if (ci, tj) == (num_indicies[None] if is_num_pad else dir_indicies[None]):
        return s3
    if (ti, cj) == (num_indicies[None] if is_num_pad else dir_indicies[None]):
        return s2
    if a > 0:
        return s2
    return s3


def calc_numerical(line):
    s = ""
    curr = "A"
    for i in range(len(line)):
        s = best_path(s, curr, line[i], True)
        curr = line[i]
    return s


@lru_cache(maxsize=None)
def num_presses(_, target, robot_num):
    global curr

    if robot_num == 25:
        return 1, tuple(curr[robot_num:])

    s = best_path("", curr[robot_num], target, False)
    ans = 0
    curr[robot_num] = target

    for c in s:
        tup = num_presses("".join(curr[robot_num + 1]), c, robot_num + 1)
        ans += tup[0]
        curr = curr[: robot_num + 1] + list(tup[1])

    return ans, tuple(curr[robot_num:])


def solve(line):
    global curr
    s = calc_numerical(line)
    ans = 0
    for c in s:
        tup = num_presses("".join(curr), c, 0)
        ans += tup[0]
        curr = list(tup[1])
    return ans


with open(p, "rt") as f:
    arr = f.read().splitlines()

for line in arr:
    shortest = solve(line)
    ans += int(line[:3]) * shortest

print(ans)
