import PySimpleGUI as sg


def notAnIntTest(number):
    try:
        number = int(number)
    except:
        print("That is not a valid number")
        return None
    return  number



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
    print( gameBoard)
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
    playerTurn = 1
    boardSize = input("What's the length of the board?")
    returnValue = notAnIntTest(boardSize)
    if returnValue != None:
        boardSize = returnValue
    else:
        continue
    playBoard,gameBoard = makeBoard(boardSize)
    gameLoop(playBoard, gameBoard, 1)
    
