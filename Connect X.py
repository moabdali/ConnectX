import PySimpleGUI as sg
from time import sleep

def notAnIntTest(number):
    try:
        number = int(number)
    except:
        print("That is not a valid number")
        return None
    return  number

def checkForWin(gameBoard,playerTurn):
    print(f"It is player {playerTurn}'s turn.")
    for elements in gameBoard:
        print(elements)
        
    #print(len(gameBoard))
    rows = len(gameBoard)
    columns = len(gameBoard)
    lengthOfWin = 4
    count = 0
    maxLen = 0
    #horizontal check

    #for each row
    for i in range(0,rows):
        count = 0
        #for each column
        for j in range(0,columns):
            if gameBoard[i][j] == playerTurn:
                count+=1
        if count >= maxLen:
            maxLen = count
        if count >= lengthOfWin:
            return 1337
        
    count = 0
    maxLen = 0

    
    #vertical check
    for i in range(0,columns):
        count = 0
        for j in range(0,rows):
            if gameBoard[j][i] == playerTurn:
                count+=1
        if count >= maxLen:
            maxLen = count
        if count >= lengthOfWin:
            return 1337

    #diagonal check up right
    count = 0
    maxLen = 0
    
    for i in range(rows-1,lengthOfWin-2,-1):
        
        count = 0
        for j in range (0,columns-lengthOfWin+1):
            count = 0
            for k in range(0,lengthOfWin):
                if gameBoard[i-k][j+k] == playerTurn:
                    count+=1
            
        
        if count >= maxLen:
            maxLen = count
        if count >= lengthOfWin:
            return 1337

    maxLen = 0
    count = 0

    
    #diagonal check up left
    for i in range(rows-1,lengthOfWin-2,-1):
        count = 0

        for j in range (columns-1, lengthOfWin-2,-1):
            count = 0
            for k in range(0, lengthOfWin):
                if gameBoard[i-k][j-k] == playerTurn:
                    count+=1

            if count >= maxLen:
                maxLen = count
            if count >= lengthOfWin:
                return 1337
            
       


        
def makeBoard(size):
    print("made a board")
    image = 'blank.png'
    board = [ [0 for j in range(size)] for i in range (size)] 
    layout = [ [sg.Button( image_filename=image,key = (i,j),pad=(0,0),size=(4,2) ) for j in range (size)] for i in range (size) ]
    playBoard = sg.Window("Connect X",layout,keep_on_top=True)
    gameBoard = [ [0]*size for i in range(size)]
    return playBoard,gameBoard


def getInput(playBoard,gameBoard, playerTurn):
    if playerTurn == 1:
        image = 'p1.png'
    elif playerTurn == 2:
        image = 'p2.png'
    
    while True:
        playBoard.BringToFront()
        event,values = playBoard.read()
        playBoard.BringToFront()
        print("brought to front")
        if event == None:
            quit()
        print (event, values)
        if gameBoard[event[0]][event[1]] != 0:
            playBoard.hide()
            sg.popup_timed("That's occupied, you dolt", no_titlebar = True, auto_close_duration=5,keep_on_top=True)
            playBoard.UnHide()
            continue
        else:
            playBoard[event].update(image_filename=image)
            gameBoard[event[0]][event[1]]=playerTurn

        playBoard.refresh()
        a = checkForWin(gameBoard,playerTurn)
        if a == 1337:
            playBoard.hide()
            sg.popup(f"PLAYER {playerTurn} WINS")
            playBoard.UnHide()
            sleep(2)
            playBoard.close()
            quit()     
        break
        
    
def gameLoop(playBoard, gameBoard, playerTurn):
    while True:
        if playerTurn == 1:
            playerTurn = 2
        elif playerTurn == 2:
            playerTurn = 1
        else:
            print("Error")
            quit()
        getInput(playBoard, gameBoard, playerTurn)
    

while True:
    
    boardSize = input("What's the length of the board?")
    returnValue = notAnIntTest(boardSize)
    if returnValue != None:
        boardSize = returnValue
    else:
        continue
    playBoard,gameBoard = makeBoard(boardSize)
    gameLoop(playBoard, gameBoard, 2)
    
