import tkinter
import random

ROWS = 25
COLUMNS = 25
TILE_SIZE = 25

WINDOW_HEIGHT = TILE_SIZE * COLUMNS
WINDOW_WIDTH = TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

window = tkinter.Tk()
window.title("Snake") 
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = 'black', width = WINDOW_WIDTH, height = WINDOW_HEIGHT, border = 0, highlightthickness = 0)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_X = int((screen_width / 2) - (window_width / 2))
window_Y = int((screen_height / 2) - (window_height / 2))
window.geometry(f'{window_width}x{window_height}+{window_X}+{window_Y}')

Snake = Tile(5*TILE_SIZE, 5*TILE_SIZE)
Food = Tile(10*TILE_SIZE, 10*TILE_SIZE)
snake_body = []
velocityX = 0
velocityY = 0
gameOver = False
score = 0

def change_direction(e):
    global velocityX, velocityY, gameOver

    if(gameOver):
        return
    
    if(e.keysym == 'Up' and velocityY != 1):
        velocityX = 0
        velocityY = -1

    elif(e.keysym == 'Down' and velocityY != -1):
        velocityX = 0
        velocityY = 1

    elif(e.keysym == 'Right' and velocityX != -1):
        velocityX = 1
        velocityY = 0

    elif(e.keysym == 'Left' and velocityX != 1):
        velocityX = -1
        velocityY = 0

def move():
    global Snake, Food, snake_body, gameOver, score

    if(gameOver):
        return
    
    if(Snake.x < 0 or Snake.x >= WINDOW_WIDTH or Snake.y < 0 or Snake.y >= WINDOW_HEIGHT):
        gameOver = True
        return
    
    for tile in snake_body:
        if(Snake.x == tile.x and Snake.y == tile.y):
            gameOver = True
            return
    
    if(Snake.x == Food.x and Snake.y == Food.y):
        snake_body.append(Tile(Food.x, Food.y))
        Food.x = random.randint(0, COLUMNS-1) * TILE_SIZE
        Food.y = random.randint(0, ROWS-1) * TILE_SIZE
        score += 1

    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if(i == 0):
            tile.x = Snake.x
            tile.y = Snake.y
        else:
            prev_tile= snake_body[i - 1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y


    Snake.x += velocityX * TILE_SIZE
    Snake.y += velocityY * TILE_SIZE



def draw():
    global Snake, Food, snake_body, score
    move()

    canvas.delete('all')

    canvas.create_rectangle(Food.x, Food.y, Food.x + TILE_SIZE, Food.y + TILE_SIZE, fill = "red")

    canvas.create_rectangle(Snake.x, Snake.y, Snake.x + TILE_SIZE, Snake.y + TILE_SIZE, fill = "lime green")

    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill = "lime green")

    if(gameOver):
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font = "Arial 20", text = f'Game Over: {score}', fill = 'white')
    else:
        canvas.create_text(30, 20, font = 'Arial 10', text = f'Score: {score}', fill = 'white')

    window.after(100, draw)

draw()

window.bind('<KeyRelease>', change_direction)
window.mainloop()
