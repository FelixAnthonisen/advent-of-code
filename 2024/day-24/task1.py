p = "test.txt"
ans = 0
values = dict()
X, Y = [0 for x in range(100)], [0 for y in range(100)]

with open(p, "rt") as f:
    arr = f.read().splitlines()

queries = []
b = False
for line in arr:
    if line == "":
        b = True
        continue
    if b:
        queries.append((line, False))
    else:
        mem, v = line.split()
        values[mem[: len(mem) - 1]] = int(v)

for k, v in values.items():
    if k[0] == "x":
        X[int(k[1:])] = v
    if k[0] == "y":
        Y[int(k[1:])] = v

X = int("".join([str(x) for x in X[::-1]]), 2)
Y = int("".join([str(y) for y in Y[::-1]]), 2)

print(X, Y)


while True:
    b = False
    for i in range(len(queries)):
        query, processed = queries[i]
        if processed:
            continue
        mem0, op, mem1, _, mem2 = query.split()
        if mem0 in values and mem1 in values:
            match op:
                case "OR":
                    values[mem2] = values[mem0] | values[mem1]
                case "AND":
                    values[mem2] = values[mem0] & values[mem1]
                case "XOR":
                    values[mem2] = values[mem0] ^ values[mem1]
            queries[i] = (query, True)
        else:
            b = True

    if not b:
        break

arr = [0 for _ in range(100)]

for k, v in values.items():
    if k[0] == "z":
        arr[int(k[1:])] = v

print(int("".join([str(x) for x in arr[::-1]]), 2))
