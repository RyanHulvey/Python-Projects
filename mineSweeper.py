import tkinter
import random

ROWS = 11
COLUMNS = 11
TILE_SIZE = 50
WINDOW_WIDTH = ROWS * TILE_SIZE
WINDOW_HEIGHT = COLUMNS * TILE_SIZE

Window = tkinter.Tk()
Window.title('Mine-Sweeper')
Window.resizable(False, False)

canvas = tkinter.Canvas(Window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, border=0, highlightthickness=0)
canvas.pack()
Window.update()

class Tile:
    def __init__(self, x, y, color, command):
        self.checked = False
        self.x = x
        self.y = y
        self.color = color
        self.command = command
        self.button = tkinter.Button(Window, bg=color, activebackground=color, borderwidth=0, command=lambda: command(number_Grid, tile_Grid, x, y))
        self.button.place(x=(i * TILE_SIZE), y=(j * TILE_SIZE), width=TILE_SIZE, height=TILE_SIZE)
    
    def buttonCheck(self):
        self.button.config(bg='white', activebackground='white')
        self.checked = True

    def updateButton(self, text):
        self.button.config(text=text, font=30)

    def returnChecked(self):
        return self.checked
    
    def disableButton(self):
        self.button.config(state='disabled')

def buttonPress(list, list2, x, y):
    if(list[x][y] == 0):
        list2[x][y].buttonCheck()
        try:
            if(list2[x + 1][y].returnChecked() == False and list[x + 1][y] == 0):
                buttonPress(list, list2, x + 1, y)
            elif(list[x + 1][y] > 0 and list[x + 1][y] < 10):
                list2[x + 1][y].updateButton(list[x + 1][y])
        except IndexError:
            pass
        try:
            if(list2[x][y + 1].returnChecked() == False and list[x][y + 1] == 0):
                buttonPress(list, list2, x, y + 1)
            elif(list[x][y + 1] > 0 and list[x][y + 1] < 10):
                list2[x][y + 1].updateButton(list[x][y + 1])
        except IndexError:
            pass
        try:
            if(list2[x - 1][y].returnChecked() == False and list[x - 1][y] == 0):
                buttonPress(list, list2, x - 1, y)
            elif(list[x - 1][y] > 0 and list[x - 1][y] < 10):
                list2[x - 1][y].updateButton(list[x - 1][y])
        except IndexError:
            pass
        try:
            if(list2[x][y - 1].returnChecked() == False and list[x][y - 1] == 0):
                buttonPress(list, list2, x, y - 1)
            elif(list[x][y - 1] > 0 and list[x][y - 1] < 10):
                list2[x][y - 1].updateButton(list[x][y - 1])
        except IndexError:
            pass
    elif(list[x][y] > 0 and list[x][y] < 10):
        list2[x][y].updateButton(list[x][y])
    elif(list[x][y] > 10):
        for i in range(ROWS):
            for j in range(COLUMNS):
                list2[x][y].disableButton()


    
number_Grid = []
for i in range(ROWS):
    number_Row = []
    for j in range(COLUMNS):
        number_Row.append(0)
    number_Grid.append(number_Row)

bomb_Count = 0
num_Bombs = 15
while bomb_Count < num_Bombs:
    random_X = random.randint(0, 10)
    random_Y = random.randint(0, 10)
    if number_Grid[random_X][random_Y] < 10:
        number_Grid[random_X][random_Y] = 10
        try:
            number_Grid[random_X + 1][random_Y] += 1
        except IndexError:
            pass
        try:
            number_Grid[random_X + 1][random_Y + 1] += 1
        except IndexError:
            pass
        try:
            number_Grid[random_X][random_Y + 1] += 1
        except IndexError:
            pass
        try:
            number_Grid[random_X - 1][random_Y] += 1
        except IndexError:
            pass
        try:
            number_Grid[random_X - 1][random_Y - 1] += 1
        except IndexError:
            pass
        try:
            number_Grid[random_X][random_Y - 1] += 1
        except IndexError:
            pass
        try:
            number_Grid[random_X + 1][random_Y - 1] += 1
        except IndexError:
            pass
        try:
            number_Grid[random_X - 1][random_Y + 1] += 1
        except IndexError:
            pass
        bomb_Count += 1
   
tile_Color_Checker = True
tile_Grid = []
for i in range(ROWS):
    tile_Row = []
    for j in range(COLUMNS):
        if(tile_Color_Checker):
            tile_Color = 'gray'
            tile_Color_Checker = False
        else:
            tile_Color = 'light gray'
            tile_Color_Checker = True
        if(number_Grid[i][j] >= 10):
            tile_Color = 'black'
        tile = Tile(i, j, tile_Color, buttonPress)
        tile_Row.append(tile)
    tile_Grid.append(tile_Row)
        
Window.mainloop()

