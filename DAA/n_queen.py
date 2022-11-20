from copy import deepcopy

def create_board(n):
    board = []
    for i in range(n):
        board += [["_"]*n]
    
    # print(board)
    return board

n = int(input("enter number: "))
col = set()
posDig = set()
negDIg = set()
board = create_board(n)
res = []

def backtrack(r):
    if r==n:
        copy = deepcopy(board)
        res.append(copy)   
        return
    
    for c in range(n):
        if c in col or (r+c) in  posDig or (r-c) in negDIg:
            continue
        
        col.add(c)
        posDig.add(r+c)
        negDIg.add(r-c)
        board[r][c] = "Q"
        
        backtrack(r+1)
        
        col.remove(c)
        posDig.remove(r+c)
        negDIg.remove(r-c)
        board[r][c] = "_"
backtrack(0)


   
for i in range(len(res)):
    print()
    print(i+1,"\n")
    for a in res[i]:
        print(*a)