import PySimpleGUI as sg
from time import sleep



#makes sure you have an integer
def notAnIntTest(number):
    try:
        number = int(number)
    except:
        sg.popup("That is not a valid number")
        return None
    return  number



#checks for win conditions
def checkForWin(gameBoard,playerTurn, winLength):
    

    rows = len(gameBoard)
    columns = len(gameBoard)
    #number of connected pieces needed for a win
    lengthOfWin = int(winLength)
    count = 0
    maxLen = 0

    #
    #horizontal check
    #
    
    #for each row
    for i in range(0,rows):
        count = 0
        #for each column
        for j in range(0,columns):
            if gameBoard[i][j] == playerTurn:
                count+=1
            else:
                count = 0
            if count >= maxLen:
                maxLen = count
            if count >= lengthOfWin:
                return 1337
        
    count = 0
    maxLen = 0

    #
    #vertical check
    #
    
    for i in range(0,columns):
        count = 0
        for j in range(0,rows):
            if gameBoard[j][i] == playerTurn:
                count+=1
            else:
                count = 0
            if count >= maxLen:
                maxLen = count

            if count >= lengthOfWin:
                return 1337
        
    #
    #diagonal check up right
    #
    
    count = 0
    maxLen = 0
    
    for i in range(rows-1,lengthOfWin-2,-1):
        
        count = 0
        for j in range (0,columns-lengthOfWin+1):
            count = 0
            for k in range(0,lengthOfWin):
                if gameBoard[i-k][j+k] == playerTurn:
                    count+=1
                else:
                    count = 0
            
        
            if count >= maxLen:
                maxLen = count
            if count >= lengthOfWin:
                return 1337

    maxLen = 0
    count = 0

    #
    #diagonal check up left
    #
    
    for i in range(rows-1,lengthOfWin-2,-1):
        count = 0

        for j in range (columns-1, lengthOfWin-2,-1):
            count = 0
            for k in range(0, lengthOfWin):
                if gameBoard[i-k][j-k] == playerTurn:
                    count+=1
                else:
                    count = 0

                if count >= maxLen:
                    maxLen = count
                if count >= lengthOfWin:
                    return 1337
                
def findEmptySlot(gameBoard, column):
    for i in range (len(gameBoard)-1,0,-1):
        if gameBoard[i][column] == 0:
            return i
        


# initialize the boardgame        
def makeBoard(size):
    # place a white square for unused squares
    image = 'blank.png'
    # stores what the game outline looks like
    board = [ [0 for j in range(size)] for i in range (size)]
    layout = [ [sg.Button( image_filename=image,key = (i,j),pad=(0,0),size=(4,2) ) for j in range (size)] for i in range (size) ]
    playBoard = sg.Window("Connect X",layout,keep_on_top=True).Finalize()
    # stores what pieces are supposed to be where
    gameBoard = [ [0]*size for i in range(size)]
    return playBoard,gameBoard


def getInputTTT(playBoard,gameBoard, playerTurn, winLength):

    # player's pieces
    if playerTurn == 1:
        image = 'p1.png'
    elif playerTurn == 2:
        image = 'p2.png'
    
    while True:
        playBoard.BringToFront()
        event,values = playBoard.read()
        playBoard.BringToFront()
        #if the player hit the X button, exit the game
        if event == None:
            quit()
        #if you try to place a piece on an occupied spot
        if gameBoard[event[0]][event[1]] != 0:
            playBoard.hide()
            sg.popup_timed("That's occupied, you dolt", no_titlebar = True, auto_close_duration=5,keep_on_top=True)
            playBoard.UnHide()
            continue
        #put the piece in if valid
        else:
            playBoard[event].update(image_filename=image)
            gameBoard[event[0]][event[1]]=playerTurn
        
        playBoard.refresh()
        a = checkForWin(gameBoard,playerTurn, winLength)
        if a == 1337:
            playBoard.hide()
            sg.popup(f"PLAYER {playerTurn} WINS")
            playBoard.UnHide()
            sleep(2)
            playBoard.close()
            quit()     
        break
        
def getInputC4(playBoard,gameBoard, playerTurn, winLength):
    
    # player's pieces
    if playerTurn == 1:
        image = 'p1.png'
    elif playerTurn == 2:
        image = 'p2.png'
    
    while True:
        playBoard.BringToFront()
        event,values = playBoard.read()
        playBoard.BringToFront()
        #if the player hit the X button, exit the game
        if event == None:
            quit()

            
        #check to see if column is empty
        #if you try to place a piece on an occupied spot
        if gameBoard[0][event[1]]!=0:
            playBoard.hide()
            sg.popup("That column is occupied, you dolt!")
            playBoard.UnHide()
            continue

        
        #put the piece in if valid
        else:
            emptySlot = findEmptySlot(gameBoard,event[1])
            #playBoard[(event[emptySlot],event[1])].update(image_filename=image)
            playBoard[(emptySlot,event[1])].update(image_filename=image)
            gameBoard[emptySlot][event[1]]=playerTurn
        
        playBoard.refresh()
        a = checkForWin(gameBoard,playerTurn, winLength)
        if a == 1337:
            playBoard.hide()
            sg.popup(f"PLAYER {playerTurn} WINS")
            playBoard.UnHide()
            sleep(2)
            playBoard.close()
            quit()     
        break


def gameLoop(playBoard, gameBoard, playerTurn, winLength, gameType):
    while True:
        if playerTurn == 1:
            playerTurn = 2
        elif playerTurn == 2:
            playerTurn = 1
        else:
            sg.popup("Error")
            quit()

        
        if gameType == 1:
            getInputC4(playBoard, gameBoard, playerTurn, winLength)
        if gameType == 2:
            getInputTTT(playBoard, gameBoard, playerTurn, winLength)
    



while True:
    gameType = sg.popup_get_text("Do you want to play tic tac toe style or connect 4? \n1. Connect 4\n2. Tic Tac Toe",keep_on_top=True)
    returnValue = notAnIntTest(gameType)
    if returnValue != None:
        gameType = returnValue
    else:
        continue
    
    
    boardSize = sg.popup_get_text("What's the length of the playing field? (minimum 3, maximum 30)",keep_on_top=True)
    returnValue = notAnIntTest(boardSize)
    if returnValue != None:
        if returnValue <3 or returnValue > 30:
            sg.popup("Nope.")
            continue
        boardSize = returnValue
    else:
        continue
    
    winLength = sg.popup_get_text("How long is a winning line?",keep_on_top=True)
    returnValue = notAnIntTest(winLength)
    if returnValue != None:
        if returnValue > boardSize:
            sg.popup("It's impossible to win with that combination of settings.\nLine size must be less than or equal to the board game size.")
            continue
        winLength = returnValue
    else:
        continue
    
    
    playBoard,gameBoard = makeBoard(boardSize)


    gameLoop(playBoard, gameBoard, 2, winLength, gameType)
    
