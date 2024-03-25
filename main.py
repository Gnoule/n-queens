import time
import random
import matplotlib.pyplot as plt

# The user is asked to select the number of columns in the table
numberOfBoard = int(input("Choisir le nombre de colonne du tableau: "))
if numberOfBoard < 4:
    numberOfBoard = int(input("Choisir un nombre suppérieur à 3: "))

# The user is asked to choose the number of checkers to be randomly placed. 
numberOfQueen = int(input("Choisir le nombre de dame déja présente: "))
if numberOfQueen > numberOfBoard:
    numberOfQueen = int(input("Choisir un nombre inférieur à {}: ".format(numberOfBoard)))

# We create the board
board = [[0 for i in range(numberOfBoard)] for i in range(numberOfBoard)]

# We will create the verification function in column
def CheckColumn(board, colum):
    for i in range(numberOfBoard):
        # we run through each square in the column
        if board[i][colum] == 1:
            return False
    # If no queen is found we return true 
    return True

# We will create the verification function in line
def CheckRow(board, actualRow):
    for i in range(numberOfBoard):
        # we go through each square of the line to check if there is a queen
        if board[actualRow][i] == 1:
            return False
    # If no queen is found we return true 
    return True

# We will create the diagonal verification function
def CheckDiagonal(board, row, colum):
    
    # Checking the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(colum, -1, -1)):
        if board[i][j] == 1:
            return False

    # Checking the lower right diagonal
    for i, j in zip(range(row+1, numberOfBoard), range(colum+1, numberOfBoard)):
        if board[i][j] == 1:
            return False
    
    # Checking the lower left diagonal    
    for i, j in zip(range(row, numberOfBoard), range(colum, -1, -1)):
        if board[i][j] == 1:
            return False

    # Checking the top right diagonal
    for i, j in zip(range(row, -1, -1), range(colum, numberOfBoard)):
         if board[i][j] == 1:
             return False
    # If no queen is found we return true    
    return True

# We will now add queens to the board.
def AddQueen(board, row, numberOfBoard):
    # If the number of rows equals the total number in the array, we're done and the function returns true.
    if row == numberOfBoard:
        return True
    # we will scan the number of cells in the line
    for i in range(numberOfBoard):
        # Check if there is a queen in the line
        if(CheckRow(board, row) == True):
            # Check for queen in column or diagonals
            if(CheckColumn(board, i) == True and CheckDiagonal(board, row, i) == True):
                # If none are found, conditions are good and a queen is placed
                board[row][i] = 1
                # We then call the function recusively to check that adding the queen doesn't block us
                if AddQueen(board, row + 1, numberOfBoard):
                    # In the case of the recusiviter function, true is returned.
                    return True
                # If you are blocked, remove the queen and move on to the next square.        
                board[row][i] = 0
        else:
            # If there's a queen on the line, we know there won't be another, so we move on to the next line
            if(AddQueen(board, row + 1, numberOfBoard)):
                # In the case of the recusiviter function, true is returned.
                return True
    # If no solution is possible, we return false.
    return False

# We will now add random queens to the board.
def AddRandomQueens(board, numberOfQueen):
    # we will scan the number of cells in the line
    for i in range(numberOfQueen):
        # We'll create a number for the rows and one for the square at random
        randomRow = random.randint(0, numberOfBoard - 1)
        randomColum = random.randint(0, numberOfBoard - 1)
        # Check if there is a queen in the line
        if(CheckRow(board, randomRow) == True):
            # Check for queen in column or diagonals
            if(CheckColumn(board, randomColum) == True and CheckDiagonal(board, randomRow, randomColum) == True):
                # If none are found, conditions are good and a queen is placed
                board[randomRow][randomColum] = 1
            else:
                # If you can't place a queen, we'll call up the function, giving the number of queens to place as a parameter.
                numberOfQueenLeft = numberOfQueen - i
                AddRandomQueens(board, numberOfQueenLeft)
        else:
            # If you can't place a queen, we'll call up the function, giving the number of queens to place as a parameter.
            numberOfQueenLeft = numberOfQueen - i
            AddRandomQueens(board, numberOfQueenLeft)
    return True

# We will now create a function for statistics
def Statistic(numberOfQueen):
    # We create a list to store the various stats
    listOfStatistic = []
    # We execute the function for a number of times equal to the number of columns.
    for i in range(numberOfBoard):
        # We create the board
        board = [[0 for i in range(numberOfBoard)] for i in range(numberOfBoard)]
        # Call the function for randomly adding queens
        AddRandomQueens(board, numberOfQueen)
        # We launch a timer
        start = time.time()
        # Call the function to place the queens
        AddQueen(board, 0, numberOfBoard)
        # Stop the timer
        end = time.time()
        # Recover the function execution time
        timeOfExecution = end - start
        # We add it to the list
        listOfStatistic.append(timeOfExecution)
    # Once all the executions have been completed, the average time is calculated.
    averageTime = sum(listOfStatistic) / len(listOfStatistic)
    # We return the list and the average time
    return listOfStatistic, averageTime

# We create the function for displaying and calling functions
def ReturnResult():
    
    # The empty board is displayed
    for row in board:
        print(row)
    print("")
    
    # Randomly add queens and display them
    print(AddRandomQueens(board, numberOfQueen))
    for row in board:
        print(row)
    print("")
    
    # We launch a timer
    start = time.time()
    # Call the function to place the queens
    print(AddQueen(board, 0, numberOfBoard))
    # Stop the timer
    end = time.time()
    # We check whether the execution has found a solution
    if AddQueen(board, 0, numberOfBoard) == True:
        print ("Solution trouvé : ")
        
        # We call the statistc function and retrieve the retrouner values.
        statisticResult, averageTime = Statistic(numberOfQueen)

        # Statistics are displayed
        plt.plot(statisticResult)
        plt.axhline(y=averageTime, color='r', linestyle='--', label='Moyenne')
        plt.legend()
        plt.xlabel('Bleu')
        plt.ylabel('Temps d\'exécution (s)')
        plt.title('Temps d\'exécution de la fonction AddQueen')
        plt.show()
    # If not, we indicate that no solution has been found.
    else:
        print ("Pas de solution trouvé")

    # The completed board is displayed
    for row in board:
        print(row)
    print("Temps de la fonction: ", end - start, "seconde")

    
# Call the function that returns the results
ReturnResult()