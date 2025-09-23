# BOARD & GLOBALS
board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

currentPlayer = "X"
gameRunning = True
winner = None

# PRINT BOARD
def printBoard(board):
    print("\n" + "\n".join(" | ".join(linhas) for linhas in board) + "\n")

# SWITCH PLAYER
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
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

# CHECK WINNER
def checkRows(board):
    global winner
    for i in range(len(board)):
        if len(set(board[i])) == 1 and "-" not in set(board[i]):
            winner = board[i][0]
            return True

def checkColumns(board):
    global winner        
    for col in range(len(board)):
        coluna = [board[linha][col] for linha in range(len(board))]
        if len(set(coluna)) == 1 and "-" not in set(coluna):
            winner = board[0][col]
            return True

def checkDiag(board):
    global winner
    if len(set(board[n][n] for n in range(len(board)))) == 1 and board[0][0] != "-":
        winner = board[0][0]
        return True
    elif len(set(board[i][len(board) - 1 - i] for i in range(len(board)))) == 1 and board[0][2] != "-":
        winner = board[0][2]
        return True

# CHECK RESULT
def checkResult():
    global gameRunning
    if checkRows(board) or checkColumns(board) or checkDiag(board):
        gameRunning = False
        print(f"O jogador '{winner}' ganhou.")
    elif not any("-" in board[i] for i in range(len(board))):
        gameRunning = False
        print("Empate")

printBoard(board)

while gameRunning:
    playerInput(board)
    switchPlayer()
    checkResult()
