p = "test.txt"
MD = 16777216


def mix(secret, x):
    return secret ^ x


def prune(secret):
    return secret % MD


def one_round(secret):
    secret = prune(mix(secret, 64 * secret))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, 2048 * secret))
    return secret


with open(p, "rt") as f:
    arr = [int(x) for x in f.read().splitlines()]

for _ in range(2000):
    arr = [one_round(x) for x in arr]

ans = sum(arr)
print(ans)
