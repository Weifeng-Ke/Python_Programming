# student name: Weifeng Ke
# student number: 18879288

# A command-line Tic-Tac-Toe game 
import random

board = [' '] * 9 # A list of 9 strings, one for each cell, 
                  # will contain ' ' or 'X' or 'O'
played = set()    # A set to keep track of the played cells 
history=set()     # a that to that keeps track of the player's move
def init() -> None:
    """ prints the banner messages 
        and prints the intial board on the screen
    """
    print("Welcome to Tic-Tac-Toe!")
    print("You play X (first move) and computer plays O.")
    print("Computer plays randomly, not strategically.")
    printBoard()

def printBoard() -> None:
    """ prints the board on the screen based on the values in the board list """
    #Print a line on the top
    print("")
    #There are a total of 5 rows, so range(5) has 0,1,2,3,4
    for row in range(5):
        #the dividing line exists on row 1 and 3
        if row % 2 == 1:
            print("   --+---+--    --+---+--")
        #print actual data
        else:
            if row == 0:
                print(f"   {board[0]} | {board[1]} | {board[2]}    0 | 1 | 2")
            elif row == 2:
                print(f"   {board[3]} | {board[4]} | {board[5]}    3 | 4 | 5")
            elif row == 4: 
                print(f"   {board[6]} | {board[7]} | {board[8]}    6 | 7 | 8")
    #print a line below the table
    print("")
          
def playerNextMove() -> None:
    """ prompts the player for a valid cell number, 
        and prints the info and the updated board;
        error checks that the input is a valid cell number 
    """
    #keep prompting if no valid entry has been made
    while True:
        #prmpting the user for input
        try:
            player=input("> Next move for X (state a valid cell num):")
            # Check if input is a digit and in the valid range
            if player.isdigit():
                #convert the ascii number to actual integer
                player=int(player)
                #check if the int is out of the bound or not
                if 0<= player <= 8:
                    #check if the input has been used before
                    if player not in played:
                        #draw the X
                        board[player] = 'X'
                        #log the position
                        played.add(player)
                        #update the board
                        printBoard()
                        break  # Exit the loop once a valid move is made
                    else:
                        print("That cell has already been played. Choose another.")
                else:
                    raise ValueError("Must enter a valid cell number")
            else:
                raise ValueError("Must be an integer")
        except ValueError as e:
            print(e)

def computerNextMove() -> None:
    """ Computer randomly chooses a valid cell, 
        and prints the info and the updated board 
    """
    #initial the two cases
    corner=[0,2,6,8]
    edge=[1,3,5,7]
    center=4
    # update the history with the played list and extract the last move
    if played != history:
        #get the last placement
        last=list(played.difference(history))[0]
        #updat the history with the newly updated played set
        history.update(played)

    #check first move. Strategy #1 if play pick center then we pick corner. If the player does not pick center we will pick center 
    if len(played) == 1:
        if board[center] == 'X':
            cpt=random.choice(corner)
            update_cpt(cpt)
            return
        else:
            cpt=center
            update_cpt(cpt)
            return
    #check when the player has mad it's 2+ move, try all combination and see if there is an combonation that could make player win if so block it
    else:
        for j in range(9):
            if board[j]== ' ':
                #try all combination see if X is close on winning
                board[j]= 'X'
                #if the we found a case where X is closing in on winning, we can block it by putting O in it's place
                if hasWon('X'):
                    cpt=j
                    update_cpt(cpt)
                    return
                #if player is not close in wining
                else:
                    #retreat the testing step
                    board[j]= ' '
    #if there player is not close in on a win, we will try to take as many corners as possible
    for cor in corner:
        if board[cor]==' ':
            cpt=cor
            update_cpt(cpt)
            return
        #if all the corner case has been occupied
        #we will try to fill all the edge case
        for ed in edge:
            if board[ed] == ' ':
                cpt=ed
                update_cpt(cpt)
                return
        #all edge case has been filled we will fill all the available places. 
        for i in range(9):
            if board[i] == ' ':
                cpt=i
                update_cpt(cpt)
                return
#i need this function so that i don't need to copy and paste the same block of code everywhere. This helper function is here to improve maintainability and readability    
def update_cpt(computer_move:int)->None:             
    # Mark the position with 'O' and add it to the played set    
    board[computer_move]='O'
    #update the played set
    played.add(computer_move)
    #print the result
    print(f"Computer Chose cell {computer_move}") 
    printBoard()


def hasWon(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
    #check the board list there are only 8 different combination of wining scenerio
    # Define the win conditions as indices in the board list
    win_case = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal top-left to bottom-right
        [2, 4, 6]   # Diagonal top-right to bottom-left
    ]
    # Check if any of the win conditions are met
    for cond in win_case:
        #check the winning conditions against 'X' or 'O' three times
        if board[cond[0]] == who and board[cond[1]] == who and board[cond[2]] == who:
            return True
    return False
    
def terminate(who: str) -> bool:
    """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
        it also prints the final messages:
                "You won! Thanks for playing." or 
                "You lost! Thanks for playing." or 
                "A draw! Thanks for playing."  
    """
    #Check if the current player or the computer has won
    if hasWon(who):
        if who == 'X':
            # Check if player X has 
            print("You won! Thanks for playing.")
            return True
        elif who == 'O':
            # Check if player O has won
            print("You lost! Thanks for playing")
            return True
    #if the board is full and there is no winner    
    if len(played)==9:
        print("A Draw! Thanks for playing")
        return True    
    return False

if __name__ == "__main__":
    # Use as is. 
    init()
    while True:
        playerNextMove()            # X starts first
        if(terminate('X')): break   # if X won or a draw, print message and terminate
        computerNextMove()          # computer plays O
        if(terminate('O')): break   # if O won or a draw, print message and terminate