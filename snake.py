import tkinter
import random

TILE_SIZE = 30
COLUMNS = 15
ROWS = 15
WINDOW_WIDTH = COLUMNS * TILE_SIZE
WINDOW_HEIGHT = ROWS * TILE_SIZE
direction_X = 0
direction_Y = 0
apple_Location = (0, 0)
paused = False

number_Grid = []
for i in range(ROWS):
    number_Row = []
    for j in range(COLUMNS):
        number_Row.append(0)
    number_Grid.append(number_Row)

snake_Head = [random.randint(0, COLUMNS - 1), random.randint(0, ROWS - 1)]
snake_Body = []
snake_Body.append(snake_Head) 

def key_Pressed(event):
    global direction_X, direction_Y
    if(event.keysym == 'w' or event.keysym == 'Up'):
        direction_X = 0
        direction_Y = -1
    if(event.keysym == 's' or event.keysym == 'Down'):
        direction_X = 0
        direction_Y = 1
    if(event.keysym == 'a' or event.keysym == 'Left'):
        direction_X = -1
        direction_Y = 0
    if(event.keysym == 'd' or event.keysym == 'Right'):
        direction_X = 1
        direction_Y = 0
    

Window = tkinter.Tk()
Window.resizable(False, False)
Window.title('Snake')
Window.bind("<Key>", key_Pressed)
Canvas = tkinter.Canvas(Window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, border=0, highlightthickness=0)
Canvas.pack()

def create_Apple():
    global apple_Location
    apple_Location = (random.randint(0, COLUMNS - 1), random.randint(0, ROWS - 1))
    invalid_Position = False
    for i in range(len(snake_Body)):
        if(apple_Location[0] == snake_Body[i][0] and apple_Location[1] == snake_Body[i][1]):
            invalid_Position = True
        
    if(invalid_Position):
        create_Apple()
    
def move_Snake():
    global snake_Body
    snake_Head[0] += direction_X
    snake_Head[1] += direction_Y
    last_Position = snake_Head
    for i in range(len(snake_Body)):
        if(i > 0):
            temp_Position = snake_Body[i]
            snake_Body[i] = last_Position
            last_Position = temp_Position

    if(snake_Head[0] == apple_Location[0] and snake_Head[1] == apple_Location[1]):
        snake_Body.append([apple_Location[0], apple_Location[1]])
        create_Apple()

    Window.after(150, move_Snake)

def draw():
    global number_Grid
    for i in range(ROWS):
        for j in range(COLUMNS):
            number_Grid[i][j] = 0

    snake_Color = True
    for i in range(len(snake_Body)):
        if(snake_Color):
            number_Grid[snake_Body[i][0]][snake_Body[i][1]] = 1
        else:
            number_Grid[snake_Body[i][0]][snake_Body[i][1]] = 2
    
    number_Grid[apple_Location[0]][apple_Location[1]] = 3
    
    Canvas.delete('all')

    for i in range(ROWS):
        for j in range(COLUMNS):
            if(number_Grid[i][j] == 0):
                Canvas.create_rectangle((i * TILE_SIZE), (j * TILE_SIZE), ((i + 1) * TILE_SIZE), ((j + 1) * TILE_SIZE), fill='black', outline='white')
            if(number_Grid[i][j] == 1):
                Canvas.create_rectangle((i * TILE_SIZE), (j * TILE_SIZE), ((i + 1) * TILE_SIZE), ((j + 1) * TILE_SIZE), fill='lime green', outline='white')
            if(number_Grid[i][j] == 2):
                Canvas.create_rectangle((i * TILE_SIZE), (j * TILE_SIZE), ((i + 1) * TILE_SIZE), ((j + 1) * TILE_SIZE), fill='green', outline='white')
            if(number_Grid[i][j] == 3):
                Canvas.create_rectangle((i * TILE_SIZE), (j * TILE_SIZE), ((i + 1) * TILE_SIZE), ((j + 1) * TILE_SIZE), fill='red', outline='white')
    
    Window.after(100, draw)

move_Snake()
create_Apple()
draw()
Window.mainloop()