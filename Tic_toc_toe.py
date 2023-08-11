#Tic Toc Toe
print( "                         welcome                      ")
print ( "                       by   jey                      ")


from pyfiglet import Figlet 
def game(): 
    for row in game_board: 
        for cel in row: 
            print(cel, end="-") 
        print() 
         
def check_game1(): 
    # افقی 
    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X": 
        print("Player 1 Win") 
        quit() 
         
    elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X": 
        print("Player 1 Win") 
        quit() 
         
    elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X": 
        print("Player 1 Win") 
        quit() 
    # عمودی 
    elif game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X": 
        print("Player 1 Win") 
        quit() 
    elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X": 
        print("Player 1 Win") 
        quit() 
    elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X": 
        print("Player 1 Win") 
        quit() 
    # ضربدری 
    elif game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X": 
        print("Player 1 Win") 
        quit() 
    elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X": 
        print("Player 1 Win") 
        quit() 
def check_game2(): 
    # افقی 
    if game_board[0][0] == "0" and game_board[0][1] == "0" and game_board[0][2] == "0": 
        print("Player 2 Win") 
        quit() 
         
 
    elif game_board[1][0] == "0" and game_board[1][1] == "0" and game_board[1][2] == "0": 
        print("Player 2 Win") 
        quit() 
 
    elif game_board[2][0] == "0" and game_board[2][1] == "0" and game_board[2][2] == "0": 
        print("Player 2 Win") 
        quit() 
 
    # عمودی 
    elif game_board[0][0] == "0" and game_board[1][0] == "0" and game_board[2][0] == "0": 
        print("Player 2 Win") 
        quit() 
 
    elif game_board[0][1] == "0" and game_board[1][1] == "0" and game_board[2][1] == "0": 
        print("Player 2 Win") 
        quit() 
 
    elif game_board[0][2] == "0" and game_board[1][2] == "0" and game_board[2][2] == "0": 
        print("Player 2 Win") 
        quit() 
 
    # ضربدری 
    elif game_board[0][0] == "0" and game_board[1][1] == "0" and game_board[2][2] == "0": 
        print("Player 2 Win") 
        quit() 
 
    elif game_board[0][2] == "0" and game_board[1][1] == "0" and game_board[2][0] == "0": 
        print("Player 2 Win") 
        quit() 
def check_draw(): 
    if game_board[0][0]!="-" and game_board[0][1]!="-" and game_board[0][2]!="-" and game_board[1][0]!="-" and game_board[1][1]!="-" and game_board[1][2]!="-" and game_board[2][0]!="-" and game_board[2][1]!="-" and game_board[2][2]!="-": 
        print("Draw") 
        quit() 
f=Figlet(font='bubble') 
print(f.renderText('Welcome To Tic Toc Toe')) 
game_board = [["-", "-", "-"], 
              ["-", "-", "-"], 
              ["-", "-", "-"]] 
game() 
 
# Player 1 
while True: 
    while True: 
        print("Player1") 
        row = int(input("Enter Row: ")) 
        cel = int(input("Enter Cel: ")) 
        if 0 <= row <= 2 and 0 <= cel <= 2: 
            if game_board[row][cel] == "-": 
                game_board[row][cel] = "X" 
                game() 
                check_game1() 
                check_draw() 
                break 
            else: 
                print("Please choose another cell!") 
        else: 
            print("Please choose a number between 0 and 2!") 
     
# Player 2 
    while True: 
        print("Player2") 
        row = int(input("Enter Row: ")) 
        cel = int(input("Enter Cel: ")) 
        if 0 <= row <= 2 and 0 <= cel <= 2: 
            if game_board[row][cel] == "-": 
                game_board[row][cel] = "0" 
                game() 
                check_game2() 
                check_draw() 
                break 
            else: 
                print("Please choose another cell!") 
        else: 
            print("Please choose a number between 0 and 2!")