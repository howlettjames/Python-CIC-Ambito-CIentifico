import random

def drawBoard(board):
    '''
    Function that draws a board
    '''
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("-" * 12)
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-" * 12)
    print(" " + board[1] + " | " + board[2] + " | " + board[3])

def inputPlayerLetter():
    letter = ''

    while not(letter == 'X' or letter == 'O'):
        print("Do you wish to be X or O?")
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def defineBeginning():
    num = random.randint(0, 1)
    if num == 0:
        return 'The PC'
    else:
        return 'The player'

def playAgain():
    print('Do you wish to play again? (Y/N): ')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    return (( board[7] == letter and board[8] == letter and board[9] == letter ) or
            ( board[4] == letter and board[5] == letter and board[6] == letter ) or
            ( board[1] == letter and board[2] == letter and board[3] == letter ) or

            ( board[7] == letter and board[4] == letter and board[1] == letter ) or
            ( board[8] == letter and board[5] == letter and board[2] == letter ) or
            ( board[9] == letter and board[6] == letter and board[3] == letter ) or

            ( board[7] == letter and board[5] == letter and board[3] == letter ) or
            ( board[9] == letter and board[5] == letter and board[1] == letter )
           )   

def isFreeSpace(board, move):
    return board[move] == ' '

def getBoardDuplicate(board):
    boardDuplicate = []
    
    for element in board:
        boardDuplicate.append(element)
    
    return boardDuplicate

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isFreeSpace(board, int(move)):
        move = input("Which is your next move? (1-9): ")

    return int(move)

def chooseRandomMove(board, listMoves):
    availableMoves = []
    for move in listMoves:
        if isFreeSpace(board, move):
            availableMoves.append(move)
    
    if len(availableMoves) != 0:
        return random.choice(availableMoves)
    else:
        return None

def getPCMove(board, letterPC):
    if letterPC == 'X':
        letterPlayer = 'O'
    else:
        letterPlayer = 'X'    

    # First check if we can win in next move
    for i in range(1, 10):
        copiedBoard = getBoardDuplicate(board)
        if isFreeSpace(copiedBoard, i):
            makeMove(copiedBoard, letterPC, i)
            if isWinner(copiedBoard, letterPC):
                return i
    
    # PC can't win in next move so it makes a blocking move
    for i in range(1, 10):
        copiedBoard = getBoardDuplicate(board)
        if isFreeSpace(copiedBoard, i):
            makeMove(copiedBoard, letterPlayer, i)
            if isWinner(copiedBoard, letterPlayer):
                return i

    # Player can't win in next move so PC will try to occupy a free space in a corner
    move = chooseRandomMove(board, [1, 3, 7, 9])
    if move != None:
        return move

    # PC can't occupy a corner so it will try to occupy the center
    if isFreeSpace(board, 5):
        return 5
    
    # PC can't occupy the center so it will try to occupy any space left
    return chooseRandomMove(board, [2, 4, 5, 8])

def isBoardFullOccupied(board):
    for i in range(1, 10):
        if isFreeSpace(board, i):
            return False
    
    return True

def playCat():
    print("Welcome to the Cat game!")

    while True:
        # Reset the board
        gameBoard = [' '] * 10
        letterPlayer, letterPC = inputPlayerLetter()

        print(f"Player = {letterPlayer}")
        print(f"PC = {letterPC}")

        turn = defineBeginning()
        print(turn + ' moves first')
        gameInProgress = True

        while gameInProgress:
            if turn == 'The player':
                print("\nPlayer's turn")
                drawBoard(gameBoard)
                move = getPlayerMove(gameBoard)
                makeMove(gameBoard, letterPlayer, move)

                if isWinner(gameBoard, letterPlayer):
                    drawBoard(gameBoard)
                    print('Congrats you have won!')
                    gameInProgress = False
                else:
                    if isBoardFullOccupied(gameBoard):
                        drawBoard(gameBoard)
                        print("It's a tie!")
                        gameInProgress = False
                    else:
                        turn = 'The PC'
            else:
                print("\nPC's turn")
                drawBoard(gameBoard)
                move = getPCMove(gameBoard, letterPC)
                makeMove(gameBoard, letterPC, move)

                if isWinner(gameBoard, letterPC):
                    drawBoard(gameBoard)
                    print('The PC has won!')
                    gameInProgress = False
                else:
                    if isBoardFullOccupied(gameBoard):
                        drawBoard(gameBoard)
                        print("It's a tie!")
                        gameInProgress = False
                    else:
                        turn = 'The player'

        if not playAgain():
            break

    print("End of the game")

if __name__=='__main__':
    playCat()