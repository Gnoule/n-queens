import time
import random
import matplotlib.pyplot as plt

numberOfBoard = int(input("Choisir le nombre de case du tableau: "))
# numberOfQueen = int(input("Choisir le nombre de dame déja présente: "))

board = [[0 for i in range(numberOfBoard)] for i in range(numberOfBoard)]
board[0][1] = 1
    
def CheckColumn(board, row, column):
    for i in range(row, -1, -1):
        if board[i][column] == 1:
            return False
    return True

def CheckRow(board, row):
    for i in range(row):
        if board[row][i] == 1:
            return False
    return True

def CheckDiagonal(board, row, colum):
    for i, j in zip(range(row, -1, -1), range(colum, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(colum, numberOfBoard)):
        if board[i][j] == 1:
            return False
    return True

def AddQueen(board, row, numberOfBoard):
    if row == numberOfBoard:
        return True
    for i in range(numberOfBoard):
        if(CheckColumn(board, row, i) == True and CheckDiagonal(board, row, i) == True and CheckRow(board, row) == True):
            board[row][i] = 1
            # print("Add Queen all condition is true")
            if AddQueen(board, row + 1, numberOfBoard):
                return True
            board[row][i] = 0
    return False

def AddRandomQueens(board):
    return board

def Statistic():
    listOfStatistic = []
    for i in range(numberOfBoard):
        start = time.time()
        AddQueen(board, 0, numberOfBoard)
        end = time.time()
        # print(i)
        timeOfExecution = end - start
        listOfStatistic.append(timeOfExecution)       
    return listOfStatistic

def ReturnResult():
    
    
    for row in board:
        print(row)
    print("")
    
    # AddRandomQueens(board)
    
    start = time.time()
    print(AddQueen(board, 0, numberOfBoard))
    end = time.time()

    for row in board:
        print(row)
    print("Temps de la fonction: ", end - start, "seconde")
    
    # plt.plot(range(1, numberOfBoard + 1), Statistic())
    # plt.show()

ReturnResult()