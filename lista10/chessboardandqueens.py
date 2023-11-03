def copyBoard(board):
    boardCopy = []
    for i in range(len(board)):
        boardCopy.append([])
        for j in range(len(board)):
            boardCopy[i].append(board[i][j])
    return boardCopy

def markRow(i,board):
    for j in range(boardSize):
        if board[i][j] == ".":
            board[i][j] = "*"

def markCol(j,board):
    for i in range(boardSize):
        if board[i][j] == ".":
            board[i][j] = "*"

def markDiagBottomRight(i,j,board):
    if i >= 0 and i < boardSize:
        if j >= 0 and j < boardSize:
            if board[i][j] == ".":
                board[i][j] = "*"
            markDiagBottomRight(i+1,j+1,board)

def markDiagBottomLeft(i,j,board):
    if i >= 0 and i < boardSize:
        if j >= 0 and j < boardSize:
            if board[i][j] == ".":
                board[i][j] = "*"
            markDiagBottomLeft(i+1,j-1,board)  

def markDiagUpperRight(i,j,board):
    if i >= 0 and i < boardSize:
        if j >= 0 and j < boardSize:
            if board[i][j] == ".":
                board[i][j] = "*"
            markDiagUpperRight(i-1,j+1,board)

def markDiagUpperLeft(i,j,board):
    if i >= 0 and i < boardSize:
        if j >= 0 and j < boardSize:
            if board[i][j] == ".":
                board[i][j] = "*"
            markDiagUpperLeft(i-1,j-1,board)

def markDiag(i,j,board):
    markDiagBottomLeft(i,j,board)
    markDiagBottomRight(i,j,board)
    markDiagUpperLeft(i,j,board)
    markDiagUpperRight(i,j,board)    

def addQueen(i,j,board):
    markRow(i,board)
    markCol(j,board)
    markDiag(i,j,board)

def isValid(i,j,board):
    if i < 0 or i >= boardSize: return False
    if j < 0 or j >= boardSize: return False
    return board[i][j] == "."

def solve(row,board):
    if row == boardSize:
        global count
        count += 1
        return True
    thereIsValidMove = False
    for j in range(boardSize):
        if isValid(row,j,board):
            thereIsValidMove = True
            boardCopy = copyBoard(board)
            addQueen(row,j,boardCopy)
            if row < boardSize:
                canSolve = solve(row+1,boardCopy)
                if not canSolve:
                    thereIsValidMove = False
                    continue    
    return thereIsValidMove
           
boardSize = 8
board = []
for i in range(boardSize):
    row = list(input())
    board.append(row)
count = 0
solve(0,board)
print(count)