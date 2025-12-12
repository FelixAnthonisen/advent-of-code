import gurobipy as gp
from gurobipy import GRB

p = "input.txt"
ans = 0

with open(p, "rt") as f:
    arr = [x.split() for x in f.read().splitlines()]

jolts = [[int(y) for y in x[-1][1:-1].split(",")] for x in arr]
buttons = [[[int(k) for k in y[1:-1].split(",")] for y in x[1:-1]] for x in arr]


def solve_single(b, A):
    model = gp.Model()
    x = model.addVars(len(A[0]), vtype=GRB.INTEGER, name="x")
    model.setObjective(gp.quicksum(x[j] for j in range(len(A[0]))), GRB.MINIMIZE)
    for i in range(len(b)):
        model.addConstr(gp.quicksum(A[i][j] * x[j] for j in range(len(A[0]))) == b[i])
    model.optimize()
    return model.ObjVal


for i in range(len(jolts)):
    n, m = len(jolts[i]), len(buttons[i])
    A = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(m):
        for b in buttons[i][j]:
            A[b][j] = 1
    ans += solve_single(jolts[i], A)

print(ans)
