p = "input.txt"
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
    arr = [[int(x) for x in f.read().splitlines()]]

for _ in range(2000):
    arr.append([one_round(x) for x in arr[len(arr) - 1]])

arr = [[x % 10 for x in row] for row in arr]

mp = dict()

for i in range(len(arr[0])):
    d = dict()
    for j in range(4, len(arr)):
        seq = ",".join([str(arr[j - k][i] - arr[j - k - 1][i]) for k in range(4)])
        if seq not in d.keys():
            d[seq] = arr[j][i]
    for k, v in d.items():
        mp[k] = mp.get(k, 0) + v

best_seq = max(mp, key=mp.get)
print(best_seq)
print(mp[best_seq])
