from functools import lru_cache

# Same solution for both tasks

test = [125, 17]
test_depth = 6
inp = [0, 89741, 316108, 7641, 756, 9, 7832357, 91]
inp_depth = 75


@lru_cache(maxsize=None)
def rec(num, d):
    if d == inp_depth:
        return 1
    if num == 0:
        return rec(1, d + 1)
    s = str(num)
    if not (len(s) % 2):
        return rec(int(s[: len(s) // 2]), d + 1) + rec(int(s[len(s) // 2 :]), d + 1)
    return rec(num * 2024, d + 1)


ans = 0

for e in inp:
    ans += rec(e, 0)

print(ans)
