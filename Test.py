import time

numberOfBoard = int(input("Choisir le nombre de case du tableau: "))


board = [[0 for i in range(numberOfBoard)] for i in range(numberOfBoard)]

    
def Column(board, row, column):
    for i in range(row, -1, -1):
        if board[i][column]==1:
            return False
    return True

def Diagonal(board, row, colum):
    for i, j in zip(range(row, -1, -1), range(colum, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(colum, numberOfBoard)):
        if board[i][j] == 1:
            return False
    return True

def AddQueen(board, row):
    if row == numberOfBoard:
        return True
    for i in range(numberOfBoard):
        if(Column(board, row, i) == True and Diagonal(board, row, i) == True):
            board[row][i] = 1
            if AddQueen(board, row + 1):
                return True
            board[row][i] = 0
    return False

def Statistique():
    for i in range(20):
        start = time.time()
        AddQueen(board, 0)
        end = time.time()

        for row in board:
            print(row)
        print("Temps de la fonction: ", end - start, "seconde")
    return True

    
start = time.time()
AddQueen(board, 0)
end = time.time()

for row in board:
    print(row)
print("Temps de la fonction: ", end - start, "seconde")