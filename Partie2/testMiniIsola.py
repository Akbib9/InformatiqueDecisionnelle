game_board = [
    ["X","1","X","_"],
    ["_","_","_","X"],
    ["_","2","X","_"],
    ["X","X","X","_"]
]

########################################
#   Definitions of Functions
########################################

def GetPosition(nbr_player,game_board):
    for y in range(len(game_board)):
        for x in range(len(game_board[y])):
            if game_board[y][x]== str(nbr_player):
                return y,x

#########################################

'Get all positions player can move on'

def get_adjacent_positions(nbr_player,game_board):
    i,j = GetPosition(nbr_player, game_board)
    adjacent_positions = []  # Liste des positions adjacentes
    
    # Vérification des cases adjacentes et en diagonales
    if i > 0:  # Case au-dessus
        if game_board[i-1][j] == "_":
            adjacent_positions.append((i-1, j))
        if j > 0:  # Case en haut à gauche
            if game_board[i-1][j-1] == "_":
                adjacent_positions.append((i-1, j-1))
        if j < 4:  # Case en haut à droite
            if game_board[i-1][j+1] == "_":
                adjacent_positions.append((i-1, j+1))
    if i < 4:  # Case en-dessous
        if game_board[i+1][j] == "_":
            adjacent_positions.append((i+1, j))
        if j > 0:  # Case en bas à gauche
            if game_board[i+1][j-1] == "_":
                adjacent_positions.append((i+1, j-1))
        if j < 4:  # Case en bas à droite
            if game_board[i+1][j+1] == "_":
                adjacent_positions.append((i+1, j+1))
    if j > 0:  # Case à gauche
        if game_board[i][j-1] == "_":
            adjacent_positions.append((i, j-1))
    if j < 4:  # Case à droite
        if game_board[i][j+1] == "_":
            adjacent_positions.append((i, j+1))
    return adjacent_positions

#############################
'Evaluation'

def EvaluationFunction(game_board):
    evaluation = len(get_adjacent_positions(1,game_board)) - len(get_adjacent_positions(2,game_board)) 
    return evaluation


print(EvaluationFunction(game_board))