p = "input.txt"
ans = 0
values = dict()


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


def perform_round(qs, vs):
    while True:
        b = False
        for i in range(len(qs)):
            query, processed = qs[i]
            if processed:
                continue
            mem0, op, mem1, _, mem2 = query.split()
            if mem0 in vs and mem1 in vs:
                match op:
                    case "OR":
                        vs[mem2] = vs[mem0] | vs[mem1]
                    case "AND":
                        vs[mem2] = vs[mem0] & vs[mem1]
                    case "XOR":
                        vs[mem2] = vs[mem0] ^ vs[mem1]
                qs[i] = (query, True)
            else:
                b = True
        if not b:
            break

    Z = [0 for _ in range(100)]

    for k, v in vs.items():
        if k[0] == "z":
            Z[int(k[1:])] = v
    Z = int("".join([str(x) for x in Z[::-1]]), 2)

    return Z


for i in range(100000):
    p = str(i % 45)
    k = "x" + ("0" + p if len(p) == 1 else p)
    values[k] = (values[k] + 1) % 2
    Z = perform_round(queries.copy(), values.copy())
    X, Y = [0 for _ in range(100)], [0 for _ in range(100)]
    for k, v in values.items():
        if k[0] == "x":
            X[int(k[1:])] = v
        if k[0] == "y":
            Y[int(k[1:])] = v

    X = int("".join([str(x) for x in X[::-1]]), 2)
    Y = int("".join([str(y) for y in Y[::-1]]), 2)
    res = X + Y
    if Z != res:
        print(res)
        print(Z)
        res_bin = bin(res)[2:][::-1]
        z_bin = bin(Z)[2:][::-1]

        print(bin(res))

        initial_wrong = set()
        wrong = set()

        for j in range(max(len(z_bin), len(res_bin))):
            try:
                if res_bin[j] != z_bin[j]:
                    print(j)
                    initial_wrong.add("z" + str(j))
            except:
                print(j)
                initial_wrong.add("z" + str(j))
