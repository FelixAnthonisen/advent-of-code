p = "input.txt"

with open(p, "rt") as f:
    arr = f.read().splitlines()

A = int(arr[0][12:])
B = int(arr[1][12:])
C = int(arr[2][12:])

instructions = [int(x) for x in arr[4][9:].split(",")]


def resolveCombo(operand):
    if operand < 4:
        return operand
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    if operand == 7:
        exit("Invalid operand")


i = 0
out = ""
while i < len(instructions):
    opcode, operand = instructions[i], instructions[i + 1]
    match opcode:
        case 0:
            A = A // (2 ** resolveCombo(operand))
        case 1:
            B = B ^ operand
        case 2:
            B = resolveCombo(operand) % 8
        case 3:
            if A != 0:
                i = operand
                continue
        case 4:
            B = B ^ C
        case 5:
            out += str(resolveCombo(operand) % 8) + ","
        case 6:
            B = A // (2 ** resolveCombo(operand))
        case 7:
            C = A // (2 ** resolveCombo(operand))
    i += 2

print(out)
