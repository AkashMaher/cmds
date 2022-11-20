from copy import deepcopy

# create initial board
def createBoard(n):
    # board = [["."] * n for i in range(n)]
    board = []
    for i in range(n):
        board.append(["."] * n)
    print(board)
    return board

#board = [["."] * n for i in range(n)]
####################################################################
n = 8
col = set()
posDiag = set()  # (r + c)
negDiag = set()  # (r - c)
board = createBoard(n)
res = []
####################################################################

def backtrack(r):
    #base condition
    if r == n:
        copy = deepcopy(board)
        res.append(copy)
        return

    # try placing in each position in row (r)
    for c in range(n):
        if c in col or (r + c) in posDiag or (r - c) in negDiag:
            continue

        #add        
        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)
        board[r][c] = "Q"

        #try next row
        backtrack(r + 1)

        # adding done, backtrack
        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)
        board[r][c] = "_"
backtrack(0)

print(len(res))
for i in range(len(res)):
    print(i+1, ":")
    for row in res[i]:
        print(*row)
    print()
    print()
