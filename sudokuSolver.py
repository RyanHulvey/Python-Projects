import random
sudoku_List = []
button_Grid = []
GRID_NUM = 9

def hideNumbers():
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

    # unsolved_Number_Grid is used to determine if the puzzle is solvable.
    number_Count = 0
    unsolved_Number_Grid = []
    for i in range(GRID_NUM):
        unsolved_Number_Row = []
        for j in range(GRID_NUM):
            number_Reveal = False
            for z in range(len(given_Numbers_List)):
                if(number_Count == given_Numbers_List[z]):
                    number_Reveal = True
                    
            if(not number_Reveal):
                unsolved_Number_Row.append(0)
            else:
                unsolved_Number_Row.append(sudoku_List[i][j])
            number_Count += 1
        unsolved_Number_Grid.append(unsolved_Number_Row)
    
    if(True):
        return unsolved_Number_Grid
    else:
        return hideNumbers()

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

unsolved_Number_Grid = hideNumbers()

for i in range(GRID_NUM):
    for j in range(GRID_NUM):
        print(sudoku_List[i][j], end=' ')
    print()

print()

for i in range(GRID_NUM):
    for j in range(GRID_NUM):
        print(unsolved_Number_Grid[i][j], end=' ')
    print()
