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


def dfsCheck(x, y, dY, board):
    if board[y + dY][x] == "#":
        return False
    if board[y + dY][x] == ".":
        return True
    if board[y + dY][x] == "[":
        return dfsCheck(x, y + dY, dY, board) and dfsCheck(x + 1, y + dY, dY, board)
    if board[y + dY][x] == "]":
        return dfsCheck(x, y + dY, dY, board) and dfsCheck(x - 1, y + dY, dY, board)


def dfsMove(x, y, dY, board):
    if board[y + dY][x] == "[":
        dfsMove(x, y + dY, dY, board)
        dfsMove(x + 1, y + dY, dY, board)
        board[y + dY][x + 1] = "."
    elif board[y + dY][x] == "]":
        dfsMove(x, y + dY, dY, board)
        dfsMove(x - 1, y + dY, dY, board)
        board[y + dY][x - 1] = "."

    board[y + dY][x] = board[y][x]


for i in range(len(arr)):
    if arr[i] == "":
        moves = "".join(arr[i + 1 :])
        break

    line = []

    for e in arr[i]:
        if e == "#":
            c1, c2 = "#", "#"
        elif e == "O":
            c1, c2 = "[", "]"
        elif e == "@":
            c1, c2 = "@", "."
        else:
            c1, c2 = ".", "."
        line.append(c1)
        line.append(c2)

    board.append(line)


for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == "@":
            y, x = i, j
            break

for mv in moves:
    match mv:
        case "^":
            if dfsCheck(x, y, -1, board):
                dfsMove(x, y, -1, board)
                board[y][x] = "."
                y -= 1
        case ">":
            x, y = move(x, y, 1, 0, board)
        case "v":
            if dfsCheck(x, y, 1, board):
                dfsMove(x, y, 1, board)
                board[y][x] = "."
                y += 1
        case "<":
            x, y = move(x, y, -1, 0, board)

s = "\n".join(["".join(x) for x in board])
print(s)

for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == "[":
            ans += 100 * i + j

print(ans)
