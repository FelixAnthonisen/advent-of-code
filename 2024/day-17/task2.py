ins = [2, 4, 1, 3, 7, 5, 4, 1, 1, 3, 0, 3, 5, 5, 3, 0]
lo, hi = int(8**6), int(8**8)
pos = []
for i in [6443713, 6443716, 6443848]:
    k = i << 24
    for j in range(lo, hi):
        A = k + j
        out = []
        while A > 0:
            B = A % 8
            B = B ^ 3
            C = A // (2**B)
            B = B ^ C
            B = B ^ 3
            A = A // (2**3)
            out.append(B % 8)
        if out == ins:
            print(out, k + j)
            pos.append(k + j)
        if not (j % 500000):
            print((hi - j) / (hi - lo), out)
print(pos)
