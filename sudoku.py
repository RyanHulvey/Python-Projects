'''
 Hello anyone currently reading this, thank you for taking interest in this project. This is a basic creation of a Sudoku puzzle which
 consists of a 9x9 grid with numbers appearing in some of the squares. The goal of the puzzle is to fill the remaining squares. This has
 been created using Tkinter buttons. 30 numbers are given, so the puzzle is quite simple to solve.
 
 Once again, thank you for exploring this project - Ryan Hulvey
'''

import tkinter
import random

# Defining permanent variables.
TILE_SIZE = 40
GRID_NUM = 9
WINDOW_HEIGHT = (TILE_SIZE * GRID_NUM) + (TILE_SIZE * 4)
WINDOW_WIDTH = (TILE_SIZE * GRID_NUM) + (TILE_SIZE * 4)

# Defining variables which will be changed.
sudoku_List = []
button_Grid = []
selection_Button_Row = []
pressed = False
current_X = -1
current_Y = -1
time = 0.0
amount_Solved = 0
mistakes_Made = 0
game_Ended = False

# Creating Window and Canvas.
Window = tkinter.Tk()
Window.title('Sudoku')
Window.resizable(False, False)
Canvas = tkinter.Canvas(Window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, highlightthickness=0, border=0, background='gray80')
Canvas.pack()

'''
 Button Class, used for creating the grid of buttons. The given command activates another row of buttons 
 numbered one through nine for user input.
'''
class Button:
    def __init__(self, sudoku_Number, command, location_X, location_Y):
        self.sudoku_Number = sudoku_Number
        self.command = command
        self.location_X = location_X
        self.location_Y = location_Y
        self.is_Revealed = False
        self.button = tkinter.Button(Window, background='white', activebackground='white', borderwidth=0, text=sudoku_Number, command=lambda: command(location_X, location_Y))
        self.button.place(x=(TILE_SIZE * location_X) + (TILE_SIZE * 2) + 3, y=(TILE_SIZE * location_Y) + TILE_SIZE + 3, width=TILE_SIZE - 6, height=TILE_SIZE - 6)

    def updateButtonState(self, state):
        self.button.config(state=state)

    def updateButtonColor(self, color):
        self.button.config(bg=color, activebackground=color)
    
    def updateButtonNumber(self, text):
        self.button.config(text=text)

    def returnButtonNumber(self):
        return self.sudoku_Number

    def getIsRevealed(self):
        return self.is_Revealed
    
    def updateIsRevealed(self, revealed):
        self.is_Revealed = revealed

    def placeButton(self, x):
        if(x==-1):
            self.button.place_forget()
        else:
            self.button.place(x=(TILE_SIZE * x) + (TILE_SIZE * 2), y=(TILE_SIZE * 11), width=TILE_SIZE, height=TILE_SIZE) 

'''
 Previously mentioned command, deactivates most grid buttons, places selection button on screen if button has not been pressed.
 If button has been pressed, pressing again reactivates grid buttons and places selection button off screen.
'''
def button_Press(x, y):
    global pressed, selection_Button_Row, button_Grid, current_X, current_Y
    if(not pressed):
        for i in range(len(selection_Button_Row)):
            selection_Button_Row[i].placeButton(i)
        
        for i in range(GRID_NUM):
            for j in range(GRID_NUM):
                if(x == i and y == j):
                    pass
                else:
                    button_Grid[i][j].updateButtonState('disabled')
        button_Grid[x][y].updateButtonColor('light gray')
        pressed = True
        current_X = x
        current_Y = y
    else:
        for i in range(len(selection_Button_Row)):
            selection_Button_Row[i].placeButton(1000)
        
        for i in range(GRID_NUM):
            for j in range(GRID_NUM):
                    if(not button_Grid[i][j].getIsRevealed()):
                        button_Grid[i][j].updateButtonState('active')
        button_Grid[x][y].updateButtonColor('white')
        pressed = False 

# Selection Buttons, the aforementioned row of buttons for user input.
class SelectionButton:
    def __init__(self, number, command):
        self.number = number
        self.command = command
        self.button = tkinter.Button(Window, background='white', activebackground='white', borderwidth=0, text=number, command=lambda: command(number))

    def placeButton(self, x):
        self.button.place(x=(TILE_SIZE * x) + (TILE_SIZE * 2) + 3, y=(TILE_SIZE * 11) + 3, width=TILE_SIZE - 6, height=TILE_SIZE - 6)

# Determines whether the selected number is correct and disables the button if so.
def selection_Button_Press(i):
    global button_Grid, current_X, current_Y, amount_Solved, mistakes_Made, game_Ended
    button_Grid[current_X][current_Y].updateButtonNumber(i)
    button_Press(current_X, current_Y)
    if(i == sudoku_List[current_X][current_Y]):
        button_Grid[current_X][current_Y].updateButtonColor('green3')
        button_Grid[current_X][current_Y].updateButtonState('disabled')
        button_Grid[current_X][current_Y].updateIsRevealed(True)
        amount_Solved += 1
        Canvas.itemconfig(solved_Text, text=f'Tiles Solved: {amount_Solved}/51')

        # If all tiles are correctly guessed, everything will be cleared, and time, mistakes, and the play again button are displayed.
        if(amount_Solved == 51):
            game_Ended = True
            Canvas.delete('all')
            Canvas.create_rectangle((TILE_SIZE * 3.5) - 5, (TILE_SIZE * 3), (TILE_SIZE * 9.5) + 5, (TILE_SIZE * 5), fill='gray70', width=0)
            Canvas.create_text((WINDOW_WIDTH / 2), (TILE_SIZE * 4), text='Solved!', font=('Arial', 50))
            Canvas.create_text((TILE_SIZE * 5), (TILE_SIZE * 5.5), text=f'Time: {time:.1f}', font=('Arial', 16))
            Canvas.create_text((TILE_SIZE * 8), (TILE_SIZE * 5.5), text=f'Mistakes: {mistakes_Made}', font=('Arial', 16))
            play_Again_Button.place(x=(WINDOW_WIDTH / 2), y=(TILE_SIZE * 7), width=(TILE_SIZE * 4), height=(TILE_SIZE), anchor='c')       
            for i in range(GRID_NUM):
                for j in range(GRID_NUM):
                    button_Grid[i][j].placeButton(-1)
                
    else:
        button_Grid[current_X][current_Y].updateButtonColor('orange red')
        mistakes_Made += 1
        Canvas.itemconfig(mistakes_Text, text=f'Mistakes Made: {mistakes_Made}')

# Creates a simple timer which progresses by deciseconds.
def progressTime():
    global time 
    Canvas.itemconfig(time_Text, text=f'Time: {time:.1f}')
    time += 0.1
    if(not game_Ended):
        Window.after(100, progressTime)

# Resets all variables and creates a new Sudoku grid to be solved.
def playAgain():
    global sudoku_List, button_Grid, selection_Button_Row, pressed, current_X, current_Y, time, amount_Solved, mistakes_Made, game_Ended
    sudoku_List = []
    button_Grid = []
    selection_Button_Row = []
    pressed = False
    current_X = -1
    current_Y = -1
    time = 0.0
    amount_Solved = 0
    mistakes_Made = 0
    game_Ended = False
    generateSudoku()

# Generates the suduko pattern, ensures it's correct by using various shifts. Then creates the buttons and visible interface.
def generateSudoku():
    global time_Text, solved_Text, mistakes_Text

    # Before the Sudoku Grid is generated and shown, the title screen is deleted and time_Text and solved_Text are created.
    Canvas.delete('all')
    generate_Button.place_forget()
    play_Again_Button.place_forget()
    time_Text = Canvas.create_text(5, (TILE_SIZE / 2.5), text=f'', fill='Black', font=("Arial", 16), anchor='w')
    solved_Text = Canvas.create_text((TILE_SIZE * 3) + 5, (TILE_SIZE / 2.5), text=f'Tiles Solved: {amount_Solved}/51', fill='Black', font=("Arial", 16), anchor='w')
    mistakes_Text = Canvas.create_text((TILE_SIZE * 8) + 5, (TILE_SIZE / 2.5), text=f'Mistakes Made: {mistakes_Made}', fill='Black', font=("Arial", 16), anchor='w')
    global sudoku_List, given_Numbers_List, button_Grid, selection_Button_Row, number_Grid_Comparison

    for i in range(GRID_NUM):
        sudoku_Row = []
        for j in range(GRID_NUM):
            sudoku_Row.append(0)
        sudoku_List.append(sudoku_Row)

    selection_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(GRID_NUM):
        search_Number = random.randint(0, len(selection_List) - 1)
        selected_Number = selection_List[search_Number]    
        selection_List.pop(search_Number)
        sudoku_List[0][i] = selected_Number

    row_Count = 0
    for i in range(GRID_NUM):
            if(row_Count != 2 and i != 0):
                sudoku_List[i] = sudoku_List[i - 1][3:9] + sudoku_List[i - 1][0:3]
                row_Count += 1
            elif(row_Count == 2 and i != 0):
                sudoku_List[i] = sudoku_List[i - 1][1:9] + sudoku_List[i - 1][0:1]
                row_Count = 0

    # Creates grid of buttons.
    for i in range(GRID_NUM):
        button_Row = []
        for j in range(GRID_NUM):
            button = Button(sudoku_List[i][j], button_Press, i, j)
            button_Row.append(button)
        button_Grid.append(button_Row)

    # Selects an amount of numbers which will be revealed.
    given_Number_Count = 0
    given_Numbers_List = []
    while(given_Number_Count < 30):
        random_Given_Number = random.randint(0, 80)
        given_Useable = True
        for i in range(len(given_Numbers_List)):
            if(given_Numbers_List[i] == random_Given_Number):
                given_Useable = False

        if(given_Useable):
            given_Numbers_List.append(random_Given_Number)
            given_Number_Count += 1

    # Hides the majority of numbers, keeps thirty visible.
    number_Count = 0
    for i in range(GRID_NUM):
        for j in range(GRID_NUM):
            number_Reveal = False
            for z in range(len(given_Numbers_List)):
                if(number_Count == given_Numbers_List[z]):
                    number_Reveal = True
            if(not number_Reveal):
                button_Grid[i][j].updateButtonNumber('')
            else:
                button_Grid[i][j].updateButtonState('disabled')
                button_Grid[i][j].updateIsRevealed(True)
                button_Grid[i][j].updateButtonColor('gray80')
            number_Count += 1

    # Creates row of number selection buttons.
    for i in range(9):
        selection_Button = SelectionButton((i + 1), selection_Button_Press)
        selection_Button_Row.append(selection_Button)

    # Creates visible lines to divide the grid into nine segments.
    Canvas.create_rectangle((TILE_SIZE * 2), TILE_SIZE, (TILE_SIZE * 11), (TILE_SIZE * 10), fill='gray60', width=0)
    Canvas.create_rectangle((TILE_SIZE * 2) - 3, TILE_SIZE, (TILE_SIZE * 2) + 3, (TILE_SIZE * 10), fill='gray35', width=0)
    Canvas.create_rectangle((TILE_SIZE * 5) - 3, TILE_SIZE, (TILE_SIZE * 5) + 3, (TILE_SIZE * 10), fill='gray35', width=0)
    Canvas.create_rectangle((TILE_SIZE * 8) - 3, TILE_SIZE, (TILE_SIZE * 8) + 3, (TILE_SIZE * 10), fill='gray35', width=0)
    Canvas.create_rectangle((TILE_SIZE * 11) - 3, TILE_SIZE, (TILE_SIZE * 11) + 3, (TILE_SIZE * 10), fill='gray35', width=0)
    Canvas.create_rectangle((TILE_SIZE * 2) - 3, (TILE_SIZE * 1) - 3, (TILE_SIZE * 11) + 3, (TILE_SIZE * 1) + 3, fill='gray35', width=0)
    Canvas.create_rectangle((TILE_SIZE * 2), (TILE_SIZE * 4) - 3, (TILE_SIZE * 11), (TILE_SIZE * 4) + 3, fill='gray35', width=0)
    Canvas.create_rectangle((TILE_SIZE * 2), (TILE_SIZE * 7) - 3, (TILE_SIZE * 11), (TILE_SIZE * 7) + 3, fill='gray35', width=0)
    Canvas.create_rectangle((TILE_SIZE * 2) - 3, (TILE_SIZE * 10) - 3, (TILE_SIZE * 11) + 3, (TILE_SIZE * 10) + 3, fill='gray35', width=0)

    Window.after(100, progressTime)

# This is the title screen, allows the user to decide when to start.
Canvas.create_rectangle((TILE_SIZE * 3) - 5, (TILE_SIZE * 3), (TILE_SIZE * 10) + 5, (TILE_SIZE * 5), fill='gray70', width=0)
Canvas.create_text((WINDOW_WIDTH / 2), (TILE_SIZE * 4), text='SUDOKU', font=('Arial', 50))
Canvas.create_text((WINDOW_WIDTH / 2), (TILE_SIZE * 5.5), text='Created By: Ryan Hulvey', font=('Arial', 16))
generate_Button = tkinter.Button(Window, background='white', activebackground='white', borderwidth=0, text='Generate Puzzle', font=('Arial', 15), command=generateSudoku)
generate_Button.place(x=(WINDOW_WIDTH / 2), y=(TILE_SIZE * 7), width=(TILE_SIZE * 4), height=(TILE_SIZE), anchor='c')

# This button will appear once the Sudoku puzzle has been solved.
play_Again_Button = tkinter.Button(Window, background='white', activebackground='white', borderwidth=0, text='Play Again', font=('Arial', 15), command=playAgain)
play_Again_Button.place(x=(WINDOW_WIDTH * 2), y=(WINDOW_HEIGHT * 2))      

Window.mainloop()