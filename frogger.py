import tkinter
import random

ROWS = 15
COLUMNS = 15
TILE_SIZE = 30
WINDOW_WIDTH = ROWS * TILE_SIZE
WINDOW_HEIGHT = COLUMNS * TILE_SIZE
frog_X = 7
frog_Y = 14

def key_pressed(event):
    global frog_X, frog_Y
    if(event.keysym == 'w' or event.keysym == 'Up') and (frog_Y > 0):
        try:
            if(number_Grid[frog_X][frog_Y - 1] != 2):
                frog_Y -= 1
        except IndexError:
            pass
    if(event.keysym == 's' or event.keysym == 'Down') and (frog_Y < ROWS - 1):
        try:
            if(number_Grid[frog_X][frog_Y + 1] != 2):
                frog_Y += 1
        except IndexError:
            pass
    if(event.keysym == 'd' or event.keysym == 'Right') and (frog_X < COLUMNS - 1):
        try:
            if(number_Grid[frog_X + 1][frog_Y] != 2):
                frog_X += 1
        except IndexError:
            pass
    if(event.keysym == 'a' or event.keysym == 'Left') and (frog_X > 0):
        try:
            if(number_Grid[frog_X - 1][frog_Y] != 2):
                frog_X -= 1
        except IndexError:
            pass

Window = tkinter.Tk()
Window.title("Frogger")
Window.resizable(False, False)
Window.bind("<Key>", key_pressed)
Canvas = tkinter.Canvas(Window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, border=0)
Canvas.pack()

number_Grid = []
for i in range(ROWS):
    number_Row = []
    for j in range(COLUMNS):
        number_Row.append(0)
    number_Grid.append(number_Row)

river_Count = 0
river_Amount = 3
while river_Count < river_Amount:
    random_River = random.randint(0, 10)
    for i in range(COLUMNS):
        number_Grid[i][random_River] = 2
    river_Count += 1

number_Grid_Duplicate = []
for i in range(ROWS):
    for j in range(COLUMNS):
        number_Row.append(number_Grid[i][j])
    number_Grid_Duplicate.append(number_Row)

def draw():
    global number_Grid, frog_X, frog_Y

    for i in range(ROWS):
        for j in range(COLUMNS):
            number_Grid[i][j] = number_Grid_Duplicate[i][j]
    number_Grid[frog_X][frog_Y] = 1

    Canvas.delete('all')
    for i in range(ROWS):
        for j in range(COLUMNS):
            if(number_Grid[i][j] == 0):
                Canvas.create_rectangle(i * TILE_SIZE, j * TILE_SIZE, (i + 1) * TILE_SIZE, (j + 1) * TILE_SIZE, fill='light green', width=0)
            if(number_Grid[i][j] == 1):
                Canvas.create_rectangle(i * TILE_SIZE, j * TILE_SIZE, (i + 1) * TILE_SIZE, (j + 1) * TILE_SIZE, fill='green', width=0)
            if(number_Grid[i][j] == 2):
                Canvas.create_rectangle(i * TILE_SIZE, j * TILE_SIZE, (i + 1) * TILE_SIZE, (j + 1) * TILE_SIZE, fill='blue', width=0)
    Window.after(100, draw)

draw()
Window.mainloop()