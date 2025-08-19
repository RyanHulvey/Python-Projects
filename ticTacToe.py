import tkinter

ROWS = 3
COLUMNS = 3
TILE_SIZE = 200
WINDOW_WIDTH = ROWS * TILE_SIZE
WINDOW_HEIGHT = COLUMNS * TILE_SIZE

Window = tkinter.Tk()
Window.title('Tic-Tac-Toe')
Window.resizable(False, False)

canvas = tkinter.Canvas(Window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, border=0, highlightthickness=0)
canvas.pack()
Window.update()

photoX = tkinter.PhotoImage(file='Images/ticTacToeX.png', width=TILE_SIZE, height=TILE_SIZE)
photoO = tkinter.PhotoImage(file='Images/ticTacToeO.png', width=TILE_SIZE, height=TILE_SIZE)

grid = [[0, 0, 0], 
        [0, 0, 0], 
        [0, 0, 0]]

def checkRows(x, list):
    for i in range(ROWS):
        counter = 0
        for j in range(COLUMNS):
            if list[i][j] == x:
                counter += 1
                if(counter >= ROWS):
                    return True
            else:
                break
    return False

def checkColumns(x, list):
    for i in range(ROWS):
        counter = 0
        for j in range(COLUMNS):
            if list[j][i] == x:
                counter += 1
                if(counter >= COLUMNS):
                    return True
            else:
                break
    return False

def checkDiagonals(x, list):
    counter = 0
    for i in range(ROWS):
        if list[i][i] == x:
            counter += 1
            if(counter >= COLUMNS):
                    return True      
    counter = 0
    for i in range(ROWS):
        if list[i][2 - i] == x:
            counter += 1
            if(counter >= COLUMNS):
                    return True
    return False

def checkAll(x, list):
    if(checkRows(x, list) or checkColumns(x, list) or checkDiagonals(x, list)):
        for i in range(ROWS):
            for j in range(COLUMNS):
                button_List[i][j].configure(state='disabled')

    

playerTurn = True
def click(x, y):
    global playerTurn
    if(playerTurn):
        button_List[x][y].configure(image=photoX, state='disabled')
        grid[x][y] = 1
        playerTurn = False
    else:
        button_List[x][y].configure(image=photoO, state='disabled')
        grid[x][y] = 2
        playerTurn = True

    checkAll(1, grid)
    checkAll(2, grid)

button_List = []
checker = False
gridColor = 'gray'
for i in range(ROWS):
    button_Row = []
    for j in range(COLUMNS):
        if(checker):
            gridColor = 'light gray'
            checker = False
        else:
            gridColor = 'gray'
            checker = True

        button = tkinter.Button(Window, bg=gridColor, activebackground=gridColor, borderwidth=0, command=lambda x=i, y=j: click(x, y))
        button.place(x=(i * TILE_SIZE), y=(j * TILE_SIZE), width=TILE_SIZE, height=TILE_SIZE)
        button_Row.append(button)

    button_List.append(button_Row)

Window.mainloop()