import time
import random
import matplotlib.pyplot as plt

numberOfBoard = int(input("Choisir le nombre de colonne du tableau: "))
if numberOfBoard < 4:
    numberOfBoard = int(input("Choisir un nombre suppérieur à 3: "))
    
numberOfQueen = int(input("Choisir le nombre de dame déja présente: "))
if numberOfQueen > numberOfBoard:
    numberOfQueen = int(input("Choisir un nombre inférieur à {}: ".format(numberOfBoard)))

board = [[0 for i in range(numberOfBoard)] for i in range(numberOfBoard)]
# board[0][4] = 1
# board[2][0] = 1

def CheckColumn(board, colum):
    for i in range(numberOfBoard):
        if board[i][colum] == 1:
            return False
    return True

def CheckRow(board, actualRow):
    for i in range(numberOfBoard):
        if board[actualRow][i] == 1:
            return False
    return True

def CheckDiagonal(board, row, colum):
    
    for i, j in zip(range(row, -1, -1), range(colum, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row+1, numberOfBoard), range(colum+1, numberOfBoard)):
        if board[i][j] == 1:
            return False
        
    for i, j in zip(range(row, numberOfBoard), range(colum, -1, -1)):
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
                numberOfQueenLeft = numberOfQueen - i
                AddRandomQueens(board, numberOfQueenLeft)
        else:
            numberOfQueenLeft = numberOfQueen - i
            AddRandomQueens(board, numberOfQueenLeft)
    return True

def Statistic(numberOfQueen):
    listOfStatistic = []
    for i in range(numberOfQueen):
        board = [[0 for i in range(numberOfBoard)] for i in range(numberOfBoard)]
        AddRandomQueens(board, numberOfQueen)
        start = time.time()
        AddQueen(board, 0, numberOfBoard)
        end = time.time()
        timeOfExecution = end - start
        listOfStatistic.append(timeOfExecution)
    averageTime = sum(listOfStatistic) / len(listOfStatistic)
    return listOfStatistic, averageTime

def ReturnResult():
       
    for row in board:
        print(row)
    print("")
    
    print(AddRandomQueens(board, numberOfQueen))
    for row in board:
        print(row)
    print("")
    
    start = time.time()
    print(AddQueen(board, 0, numberOfBoard))
    end = time.time()
    if AddQueen(board, 0, numberOfBoard) == True:
        print ("Solution trouvé : ")
        
        statisticResult, averageTime = Statistic(numberOfQueen)
    
        plt.plot(statisticResult)
        plt.axhline(y=averageTime, color='r', linestyle='--', label='Moyenne')
        plt.legend()
        plt.xlabel('Bleu')
        plt.ylabel('Temps d\'exécution (s)')
        plt.title('Temps d\'exécution de la fonction AddQueen')
        plt.show()
    else:
        print ("Pas de solution trouvé")

    for row in board:
        print(row)
    print("Temps de la fonction: ", end - start, "seconde")

    

ReturnResult()