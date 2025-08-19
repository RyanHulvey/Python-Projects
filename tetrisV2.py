import tkinter
import random

ROWS = 24
COLUMNS = 10
TILE_SIZE = 30
WINDOW_HEIGHT = ROWS * TILE_SIZE - 120
WINDOW_WIDTH = COLUMNS * TILE_SIZE + 180
current_Block_X = 4
current_Block_Y = 0
time = 225
paused = False
rotate_Num = 7
        
number_Grid = []
for i in range(COLUMNS):
    number_Row = []
    for j in range(ROWS):
        number_Row.append(0)
    number_Grid.append(number_Row)

number_Grid_Duplicate = []
for i in range(COLUMNS):
    number_Row = []
    for j in range(ROWS):
        number_Row.append(10)
    number_Grid_Duplicate.append(number_Row)

next_Block_Grid = []
for i in range(4):
    number_Row = []
    for j in range(4):
        number_Row.append(10)
    next_Block_Grid.append(number_Row)

held_Block_Grid = []
for i in range(4):
    number_Row = []
    for j in range(4):
        number_Row.append(10)
    held_Block_Grid.append(number_Row)

block_List = [[(0,0), (0,1), (0, 2), (0, 3)], 
              [(0,1), (1,1), (0, 2), (1, 2)],
              [(0,1), (-1,2), (0, 2), (1, 2)],
              [(0,1), (0,2), (0, 3), (1, 3)],
              [(1,1), (1,2), (1, 3), (0, 3)],
              [(-1,1), (0,1), (0, 2), (1, 2)],
              [(1,1), (2,1), (1, 2), (0, 2)],
              [(-2, 2), (-1, 2), (0, 2), (1, 2)],
              [(0,1), (1,1), (0, 2), (1, 2)],
              [(0, 1), (0, 2), (0, 3), (1, 2)],
              [(-1, 2), (-1, 3), (0, 2), (1,2)],
              [(0, 1), (0, 2), (1, 2), (2, 2)],
              [(0, 0), (0, 1), (-1, 1), (-1, 2)],
              [(0, 0), (0, 1), (1, 1), (1, 2)],
              [(-1, 0), (-1, 1), (-1, 2), (-1, 3)],
              [(0,1), (1,1), (0, 2), (1, 2)],
              [(-1, 2), (0, 2), (1, 2), (0,3)],
              [(-1, 1), (0, 1), (0, 2), (0, 3)],
              [(2, 1), (1, 1), (1, 2), (1, 3)],
              [(-1, 1), (0, 1), (0, 2), (1, 2)],
              [(0, 1), (1, 1), (1, 0), (2, 0)],
              [(-2, 1), (-1, 1), (0, 1), (1, 1)],
              [(0,1), (1,1), (0, 2), (1, 2)],
              [(-1, 2), (0, 1), (0, 2), (0, 3)],
              [(-1, 2), (0, 2), (1, 2), (1, 1)],
              [(0, 2), (1, 2), (2, 2), (2, 3)],
              [(-1, 1), (0, 1), (-1, 2), (0, 0)],
              [(0, -1), (0, 0), (1, 0), (1, 1)],
              'None']
random_Num = random.randint(0, 6)
next_Random_Num = random.randint(0, 6)
current_Block = block_List[random_Num]
next_Block = block_List[next_Random_Num]
held_Block = block_List[28]
can_Hold_Block = True
held_Num = 10

def key_Pressed(event):
    global current_Block_X, current_Block_Y, number_Grid_Duplicate, next_Block, can_Hold_Block, current_Block, held_Block, next_Random_Num, random_Num, held_Num, held_Block_Grid, paused, rotate_Num

    if(event.keysym == 'p'):
        if(paused):
            paused = False
            move_Block()
        else:
            paused = True
            Canvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill="gray", stipple="gray50")
    if(event.keysym == 'd' or event.keysym == 'Right' and not paused):
        collision = False
        try:
            for i in range(len(current_Block)):
                if(current_Block[i][0] + current_Block_X >= COLUMNS or number_Grid_Duplicate[current_Block[i][0] + current_Block_X + 1][current_Block[i][1] + current_Block_Y] < 10):
                    collision = True
            if(collision == False):
                current_Block_X += 1
        except IndexError:
            pass

    if(event.keysym == 'a' or event.keysym == 'Left' and not paused):
        collision = False
        try:
            for i in range(len(current_Block)):
                if(current_Block[i][0] + current_Block_X <= 0 or number_Grid_Duplicate[current_Block[i][0] + current_Block_X - 1][current_Block[i][1] + current_Block_Y] < 10):
                    collision = True
            if(collision == False):
                current_Block_X -= 1
        except IndexError:
            pass

    if(event.keysym == 's' or event.keysym == 'Down' and not paused):
        collision = False
        try:
            for i in range(len(current_Block)):
                if(current_Block[i][1] + current_Block_Y == (ROWS - 1) or number_Grid_Duplicate[current_Block[i][0] + current_Block_X][current_Block[i][1] + current_Block_Y + 1] < 10):
                    collision = True
            if(collision == False):
                current_Block_Y += 1
        except IndexError:
            pass

    if(event.keysym == 'w' or event.keysym == 'Up' and not paused):
        try:
            collision = False
            while(collision == False):
                for i in range(len(current_Block)):
                    if(number_Grid_Duplicate[current_Block[i][0] + current_Block_X][current_Block[i][1] + current_Block_Y + 1] < 10):
                        collision = True
                        break
                if collision:
                    break
                else:
                    current_Block_Y += 1
        except IndexError:
            pass

    if(event.keysym == 'e' and not paused):
        if(can_Hold_Block):
            if (held_Block == 'None'):
                held_Num = random_Num
                held_Block = current_Block
                current_Block_Y = 0
                current_Block_X = 4
                random_Num = next_Random_Num
                current_Block = block_List[random_Num]
                next_Random_Num = random.randint(0, 6)
                next_Block = block_List[next_Random_Num]
                can_Hold_Block = False
                for i in range(4):
                    for j in range(4):
                        next_Block_Grid[i][j] = 10
            else:
                for i in range(4):
                    for j in range(4):
                        held_Block_Grid[i][j] = 10
                current_Block_Y = 0
                current_Block_X = 4
                temp_Num = random_Num
                random_Num = held_Num
                held_Num = temp_Num
                temp_Block = current_Block
                current_Block = held_Block
                held_Block = temp_Block
                can_Hold_Block = False
    
    if(event.keysym == 'space' and not paused):
        try:
            collision = False
            for i in range(len(current_Block)):
                if(number_Grid_Duplicate[block_List[random_Num + rotate_Num][i][0] + current_Block_X][block_List[random_Num + rotate_Num][i][1] + current_Block_Y + 1] < 10):
                    collision = True
                    break
            if(not collision):
                current_Block = block_List[random_Num + rotate_Num]
                rotate_Num += 7
                if(rotate_Num == 28):
                    rotate_Num = 0
        except IndexError:
            pass

def clear_Lines():
    global number_Grid_Duplicate
    for i in range(ROWS):
        row_Full = True
        for j in range(COLUMNS):
            if number_Grid_Duplicate[j][i] == 10:
                row_Full = False
                break
        if row_Full:
            for shift_row in range(i, 0, -1):
                for j in range(COLUMNS):
                    number_Grid_Duplicate[j][shift_row] = number_Grid_Duplicate[j][shift_row - 1]
            for j in range(COLUMNS):
                number_Grid_Duplicate[j][0] = 10

def move_Block():
    if(not paused):
        global current_Block_Y, current_Block_X, number_Grid, number_Grid_Duplicate, random_Num, current_Block, block_List, random_Num, next_Random_Num, next_Block_Grid, next_Block, can_Hold_Block, rotate_Num
        collision = False
        try:
            for i in range(len(current_Block)):
                if(current_Block[i][1] + current_Block_Y == (ROWS - 1) or number_Grid_Duplicate[current_Block[i][0] + current_Block_X][current_Block[i][1] + current_Block_Y + 1] < 10):
                    collision = True
                    break
        except IndexError:
            pass
        
        if(collision):
            for i in range(len(current_Block)):
                number_Grid_Duplicate[current_Block[i][0] + current_Block_X][current_Block[i][1] + current_Block_Y] = random_Num  
            current_Block_Y = 0
            current_Block_X = 4
            random_Num = next_Random_Num
            current_Block = block_List[random_Num]
            next_Random_Num = random.randint(0, 6)
            next_Block = block_List[next_Random_Num]
            can_Hold_Block = True
            rotate_Num = 7
            clear_Lines()
            for i in range(4):
                for j in range(4):
                    next_Block_Grid[i][j] = 10

        else:
            current_Block_Y += 1
        
        Window.after(time, move_Block)

Window = tkinter.Tk()
Window.title('Tetris')
Window.resizable(False, False)
Window.bind("<Key>", key_Pressed)
Canvas = tkinter.Canvas(Window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, border=0, highlightthickness=0)
Canvas.pack()

def draw():
    for i in range(COLUMNS):
        for j in range(ROWS):
            number_Grid[i][j] = number_Grid_Duplicate[i][j]
    for i in range(len(current_Block)):
        number_Grid[current_Block[i][0] + current_Block_X][current_Block[i][1] + current_Block_Y] = random_Num
    for i in range(len(next_Block)):
        next_Block_Grid[next_Block[i][0] + 1][next_Block[i][1]] = next_Random_Num
    if(held_Block != 'None'):
        for i in range(len(held_Block)):
            held_Block_Grid[held_Block[i][0] + 1][held_Block[i][1]] = held_Num
    Canvas.delete('all')

    for i in range(COLUMNS):
        for j in range(ROWS):
            if(number_Grid[i][j] == 10):
                Canvas.create_rectangle(i * TILE_SIZE, j * TILE_SIZE - 120, (i + 1) * TILE_SIZE, (j + 1) * TILE_SIZE - 120, fill='black', outline='White')
            if(number_Grid[i][j] == 0):
                Canvas.create_rectangle(i * TILE_SIZE, j * TILE_SIZE - 120, (i + 1) * TILE_SIZE, (j + 1) * TILE_SIZE - 120, fill='light blue', outline='White')
            if(number_Grid[i][j] == 1):
                Canvas.create_rectangle(i * TILE_SIZE, j * TILE_SIZE - 120, (i + 1) * TILE_SIZE, (j + 1) * TILE_SIZE - 120, fill='yellow', outline='White')
            if(number_Grid[i][j] == 2):
                Canvas.create_rectangle(i * TILE_SIZE, j * TILE_SIZE - 120, (i + 1) * TILE_SIZE, (j + 1) * TILE_SIZE - 120, fill='purple', outline='White')
            if(number_Grid[i][j] == 3):
                Canvas.create_rectangle(i * TILE_SIZE, j * TILE_SIZE - 120, (i + 1) * TILE_SIZE, (j + 1) * TILE_SIZE - 120, fill='orange', outline='White')
            if(number_Grid[i][j] == 4):
                Canvas.create_rectangle(i * TILE_SIZE, j * TILE_SIZE - 120, (i + 1) * TILE_SIZE, (j + 1) * TILE_SIZE - 120, fill='blue', outline='White')
            if(number_Grid[i][j] == 5):
                Canvas.create_rectangle(i * TILE_SIZE, j * TILE_SIZE - 120, (i + 1) * TILE_SIZE, (j + 1) * TILE_SIZE - 120, fill='lime green', outline='White')
            if(number_Grid[i][j] == 6):
                Canvas.create_rectangle(i * TILE_SIZE, j * TILE_SIZE - 120, (i + 1) * TILE_SIZE, (j + 1) * TILE_SIZE - 120, fill='red', outline='White')
            
    Canvas.create_rectangle(COLUMNS * TILE_SIZE, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill='gray', outline='white')
    for i in range(4):
        for j in range(4):
            if(next_Block_Grid[i][j] == 10):
                Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + (TILE_SIZE * 6), (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + (TILE_SIZE * 6), fill='black', outline='White')
            if(next_Block_Grid[i][j] == 0):
                Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + (TILE_SIZE * 6), (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + (TILE_SIZE * 6), fill='light blue', outline='White')
            if(next_Block_Grid[i][j] == 1):
                Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + (TILE_SIZE * 6), (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + (TILE_SIZE * 6), fill='yellow', outline='White')
            if(next_Block_Grid[i][j] == 2):
                Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + (TILE_SIZE * 6), (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + (TILE_SIZE * 6), fill='purple', outline='White')
            if(next_Block_Grid[i][j] == 3):
                Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + (TILE_SIZE * 6), (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + (TILE_SIZE * 6), fill='orange', outline='White')
            if(next_Block_Grid[i][j] == 4):
                Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + (TILE_SIZE * 6), (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + (TILE_SIZE * 6), fill='blue', outline='White')
            if(next_Block_Grid[i][j] == 5):
                Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + (TILE_SIZE * 6), (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + (TILE_SIZE * 6), fill='lime green', outline='White')
            if(next_Block_Grid[i][j] == 6):
                Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + (TILE_SIZE * 6), (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + (TILE_SIZE * 6), fill='red', outline='White')
            
        for i in range(4):
            for j in range(4):
                if(held_Block_Grid[i][j] == 10):
                    Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + TILE_SIZE, (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + TILE_SIZE, fill='black', outline='White')
                if(held_Block_Grid[i][j] == 0):
                    Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + TILE_SIZE, (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + TILE_SIZE, fill='light blue', outline='White')
                if(held_Block_Grid[i][j] == 1):
                    Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + TILE_SIZE, (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + TILE_SIZE, fill='yellow', outline='White')
                if(held_Block_Grid[i][j] == 2):
                    Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + TILE_SIZE, (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + TILE_SIZE, fill='purple', outline='White')
                if(held_Block_Grid[i][j] == 3):
                    Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + TILE_SIZE, (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + TILE_SIZE, fill='orange', outline='White')
                if(held_Block_Grid[i][j] == 4):
                    Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + TILE_SIZE, (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + TILE_SIZE, fill='blue', outline='White')
                if(held_Block_Grid[i][j] == 5):
                    Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + TILE_SIZE, (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + TILE_SIZE, fill='lime green', outline='White')
                if(held_Block_Grid[i][j] == 6):
                    Canvas.create_rectangle(i * TILE_SIZE + ((COLUMNS + 1) * TILE_SIZE), j * TILE_SIZE + TILE_SIZE, (i + 1) * TILE_SIZE+ ((COLUMNS + 1) * TILE_SIZE), (j + 1) * TILE_SIZE + TILE_SIZE, fill='red', outline='White')
                
                Canvas.create_text((COLUMNS + 3) * TILE_SIZE, 15, text='Held Block:', fill='black', font=14)
                Canvas.create_text((COLUMNS + 3) * TILE_SIZE, (TILE_SIZE * 5) + 15, text='Next Block:', fill='black', font=14)
                if(paused):
                    Canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - TILE_SIZE, text='Paused', fill='white', font=("Arial", 40))
                    Canvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill="gray", stipple="gray50")
                    Canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - TILE_SIZE, text='Paused', fill='white', font=("Arial", 40))
    Window.after(100, draw)

draw()
Window.after(300, move_Block())

Window.mainloop()