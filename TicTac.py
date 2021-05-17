from asyncio import windows_events
from typing import Sized


board = ["|   |", "|   |", "|   |",
         "|   |", "|   |", "|   |",
         "|   |", "|   |", "|   |"]

playsCount = 0

##Returns a string which displays the board in a 3 x 3 matrix
def DisplayBoard():
    output = ""
    count = 0

    for x in board:
        output = output + x +" "
        count = count + 1
        
        if count >= 3:
            output = output + "\n"
            count = 0

    return output

##Places the symbol on the board
        ##returns true if spot is empty
        ##returns false if spot is filled
def Place(index, symbol):
    global playsCount

    if (board[index] == "|   |"):
        board[index] = "| " +symbol +" |"
        playsCount = playsCount + 1
        return True
    else:
        return False

##Checks for win conditions
def WinCon():
    condition = False
    
    if (playsCount < 3):
        return False

    

    #Checking for horizontal wins
    for i in range(0, 6, 3):
        for j in range(i, i + 2):
            if (board[j] != board[j + 1]):
                break

            if (j >= i + 1):
                return True

    #Checking for vertical wins
    for i in range(3):
        for j in range(i, i + 6, 3):
            if (board[j] != board[j + 3]):
                break

            if (j >= i + 3):
                return True

    #Checking for diagonal wins
    startingPoint = 0
    endPoint = 8
    count = 4


    for i in range (2):

        if (i >= 1):
            startingPoint = 2
            endPoint = 6
            count = 2

        for j in range(startingPoint, endPoint, count):
            if (board[j] != board[j + count]):
                break

            if (j >= startingPoint + count):
                return True

    return False

def reset():
    global board
    global playsCount

    for x in range(len(board)):
        board[x] = "|   |"
    playsCount = 0

def tieGame():
    if (playsCount >= 9 and WinCon == False):
        return True
    else:
        return False