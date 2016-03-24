def printBoard(board):
    
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def checkWinner(board, player):    

    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################

    print('Checking if ' + player + ' is a winner...')
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or
            (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or
            (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or
            (board['low-L'] == player and board['mid-L'] == player and board['top-L'] == player) or
            (board['low-M'] == player and board['mid-M'] == player and board['top-M'] == player) or
            (board['low-R'] == player and board['mid-R'] == player and board['top-R'] == player) or
            (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or
            (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player))
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer   # setting the turn variable to the startingPlayer argument
    for i in range(9):      # for in loop iterating through range
        printBoard(board)   # prints the board
        print('Turn for ' + turn + '. Move on which space?')   # prints which players turn it is
        move = input() # setting the move varibale equal to what the user inputs
        board[move] = turn # sets the X or O on the board
        if( checkWinner(board, 'X') ): # checks if X wins and then prints the winner
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ):  # checks O X wins and then prints the winner.
            print('O wins!')
            break
    
        if turn == 'X': # if player X is complete,
            turn = 'O'  # change player to O
        else:
            turn = 'X'  # change it back
        
    printBoard(board) # re-prints the board with the players move added.
    
