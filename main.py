import time
import random
import matplotlib.pyplot as plt

numberOfBoard = int(input("Choisir le nombre de case du tableau: "))
if numberOfBoard < 4:
    numberOfBoard = int(input("Choisir un nombre suppérieur à 3: "))
    
numberOfQueen = int(input("Choisir le nombre de dame déja présente: "))
if numberOfQueen > numberOfBoard:
    numberOfQueen = int(input("Choisir un nombre inférieur à {}: ".format(numberOfBoard)))

board = [[0 for i in range(numberOfBoard)] for i in range(numberOfBoard)]
board[2][3] = 1

def CheckColumn(board, column):
    for i in range(numberOfBoard):
        if board[i][column] == 1:
            return False
    return True

def CheckRow(board, actualRow):
    for i in range(numberOfBoard):
        if board[actualRow][i] == 1:
            return False
    return True

# def CheckDiagonal(board, row, colum):
#     for i, j in zip(range(row, -1, -1), range(colum, -1, -1)):
#         if board[i][j] == 1:
#             return False
#     for i, j in zip(range(row, -1, -1), range(colum, numberOfBoard)):
#         if board[i][j] == 1:
#             return False
#     return True

def CheckDiagonal(board, row, colum):
    
    for i, j in zip(range(row, -1, -1), range(colum, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row+1, numberOfBoard), range(colum+1, numberOfBoard)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(colum+1, numberOfBoard)):
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
        if(CheckRow(board, row) == True):
            if(CheckColumn(board, i) == True and CheckDiagonal(board, row, i) == True):
                board[row][i] = 1
                if AddQueen(board, row + 1, numberOfBoard):
                    return True          
                board[row][i] = 0
        else:
            if(AddQueen(board, row + 1, numberOfBoard)):
                return True
    return False


def AddRandomQueens(board, numberOfQueen):
    for i in range(numberOfQueen):
        randomRow = random.randint(0, numberOfBoard - 1)
        randomColum = random.randint(0, numberOfBoard - 1)
        if(CheckRow(board, randomRow) == True):
            if(CheckColumn(board, randomColum) == True and CheckDiagonal(board, randomRow, randomColum) == True):
                board[randomRow][randomColum] = 1
            else:
                print(i)
                numberOfQueenLeft = numberOfQueen - i
                AddRandomQueens(board, numberOfQueenLeft)
        else:
            print(i)
            numberOfQueenLeft = numberOfQueen - i
            AddRandomQueens(board, numberOfQueenLeft)
    return True

def Statistic():
    listOfStatistic = []
    for i in range(numberOfBoard):
        start = time.time()
        AddQueen(board, 0, numberOfBoard)
        end = time.time()
        print(i)
        timeOfExecution = end - start
        listOfStatistic.append(timeOfExecution)       
    return listOfStatistic

def ReturnResult():
       
    for row in board:
        print(row)
    print("")
    
    # print(AddRandomQueens(board, numberOfQueen))
    # for row in board:
    #     print(row)
    # print("")
    
    start = time.time()
    print(AddQueen(board, 0, numberOfBoard))
    end = time.time()

    for row in board:
        print(row)
    print("Temps de la fonction: ", end - start, "seconde")
    
    # plt.plot(range(1, numberOfBoard + 1), Statistic())
    # plt.show()

ReturnResult()