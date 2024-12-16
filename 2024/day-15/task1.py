p = "input.txt"
ans = 0

with open(p, "rt") as f:
    arr = f.read().splitlines()

board = []
moves = ""


def move(x, y, dX, dY, board):
    endX, endY = x, y
    while 1:
        endX += dX
        endY += dY
        if board[endY][endX] == "#":
            return x, y
        if board[endY][endX] == ".":
            break
    while 1:
        if endX == x and endY == y:
            board[y][x] = "."
            break
        board[endY][endX] = board[endY - dY][endX - dX]
        endX -= dX
        endY -= dY
    return x + dX, y + dY


for i in range(len(arr)):
    if arr[i] == "":
        moves = "".join(arr[i + 1 :])
        break
    board.append([e for e in arr[i]])

for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == "@":
            y, x = i, j
            break

for mv in moves:
    match mv:
        case "^":
            x, y = move(x, y, 0, -1, board)
        case ">":
            x, y = move(x, y, 1, 0, board)
        case "v":
            x, y = move(x, y, 0, 1, board)
        case "<":
            x, y = move(x, y, -1, 0, board)

s = "\n".join(["".join(x) for x in board])

print(s)

for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == "O":
            ans += 100 * i + j

print(ans)
