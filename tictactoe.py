# BOARD & GLOBALS
board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

currentPlayer = "X"
gameRunning = True
winner = None

# PRINT BOARD
def printBoard(board):
    print("\n".join(" | ".join(linhas) for linhas in board))

# SWITCH PLAYER
def switchPlayer(currentPlayer):
    if currentPlayer.upper() == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# PLAYER INPUT
def playerInput(board):
    inp = int(input("Digite a posição da jogada (Ex: 1-9): "))

    linha = (inp - 1)//3

    if inp <= 3:
        coluna = inp-1
    else:
        coluna = (inp-1)%3

    board[linha][coluna] = currentPlayer

printBoard(board)
