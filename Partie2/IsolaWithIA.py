############### ISOLA ##################

########################################
#  Import Packages
########################################

import numpy as np
from copy import deepcopy
import re

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


########################################

def Move(nbr_player,destination, board):
    i,j = GetPosition(nbr_player, board)
    board[i][j] = "_"
    board[destination[0]][destination[1]] = str(nbr_player)

########################################
'Blok access of one case of the board'

def BlokSpot(board, spot_to_blok):
    board[spot_to_blok[0]][spot_to_blok[1]] = "X"


#########################################

'Evaluation'

def EvaluationFunction(game_board):
    evaluation = len(get_adjacent_positions(1,game_board)) - len(get_adjacent_positions(2,game_board)) 
    return evaluation


########################################

'Game Over Function'

def game_over(board):
    if len(get_adjacent_positions(1, board)) == 0 or len(get_adjacent_positions(2, board)) == 0:
        return True
    else:
        return False

########################################

def EndGame(board):
    if len(get_adjacent_positions(1, board)) == 0 and len(get_adjacent_positions(2, board)) == 0:
        print("C'est un match nul !")
    elif len(get_adjacent_positions(1, board)) == 0:
        print("Vous avez gagné !")
        return False
    elif len(get_adjacent_positions(2, board)) == 0:
        print("Vous avez perdu !")
        return False
    else:
        return True

########################################

'Minimax Function'

def MiniMaxFunction(board, nbr_player, depth, alpha, beta):
    if game_over(board) or depth == 0:
        return EvaluationFunction(board), None, None

    # Si c'est au tour de l'IA, maximisez les scores
    if nbr_player == 1:
        best_score_int = -float("inf")
        best_score_ext = -float("inf")
        best_next_spot = None
        best_spot_to_Blok = None
        best_spot_to_Blok2 = None
        for move in get_adjacent_positions(nbr_player, board):
            board_test = deepcopy(board)
            Move(nbr_player,move,board_test)
            for i in range(len(board_test)):
                for j in range(len(board_test)):
                    if board_test[i][j] == "_":
                        spot_to_blok = (i,j)
                        board_test2 = deepcopy(board_test)
                        BlokSpot(board_test2,spot_to_blok)
                        score, spot, blok = MiniMaxFunction(board_test2, 2, depth - 1, alpha, beta)
                        #print("Maximise",score)
                        if best_score_int < score:
                            best_score_int = score
                            best_spot_to_Blok = (i,j)
            if best_score_ext < best_score_int:
                best_score_ext = best_score_int
                best_next_spot = move
                best_spot_to_Blok2 = best_spot_to_Blok
            alpha = max(best_score_ext, alpha)
            if beta <= alpha:
                break
        return best_score_ext , best_next_spot, best_spot_to_Blok2

    # Si c'est au tour de l'adversaire, minimisez les scores
    else:
        worst_score_int = float("inf")
        worst_score_ext = float("inf")
        worst_next_spot = None
        worst_spot_to_Blok = None
        worst_spot_to_Blok2 = None
        for move in get_adjacent_positions(nbr_player, board):
            board_test = deepcopy(board)
            Move(nbr_player,move,board_test)
            for i in range(len(board_test)):
                for j in range(len(board_test)):
                    if board_test[i][j] == "_":
                        spot_to_blok = (i,j)
                        board_test2 = deepcopy(board_test)
                        BlokSpot(board_test2,spot_to_blok)
                        score, spot, spotBlok = MiniMaxFunction(board_test2, 1, depth - 1, alpha, beta)
                        #print("Minimise",score)
                        if worst_score_int > score:
                            worst_score_int = score
                            worst_spot_to_Blok = (i,j)
            if worst_score_ext > worst_score_int:
                worst_score_ext = worst_score_int
                worst_next_spot = move
                worst_spot_to_Blok2 = worst_spot_to_Blok
            beta = min(worst_score_ext, beta)
            if beta <= alpha:
                break
        return worst_score_ext, worst_next_spot, worst_spot_to_Blok2


########################################
#        MAIN
########################################

# Création du tableau de jeu

game_board = [
    ["_","_","1","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","2","_","_"]
]

pattern = r"^\d+ \d+$"
alpha = -float('inf')
beta = float('inf')
boucle = True

while boucle:  # Boucle de jeu

    # Tour de l'IA
    print("Au tour de l'IA")
    print(np.array(game_board))
    nbr_player = 1
    depth = 2
    value, destination, spot_to_blok = MiniMaxFunction(game_board, nbr_player, depth, alpha, beta)
    Move(nbr_player,destination, game_board)
    BlokSpot(game_board, spot_to_blok)
    boucle = EndGame(game_board)
    if boucle == False:
        break

    # Tour de l'humain
    print("Au tour du joueur")
    print(np.array(game_board))
    nbr_player = 2
    
    #Deplacement du pion du joueur
    while True:
        print("Positions valides :", get_adjacent_positions(nbr_player,game_board))
        input_string = input("Entrez les coordonnées de la case (ligne colonne) :")
        if re.match(pattern, input_string):
            i, j = map(int, input_string.split())
            destination = (i,j)
            if destination in get_adjacent_positions(nbr_player,game_board):
                Move(nbr_player,destination, game_board)
                break
            else:
                print("Case non valide, veuillez réessayer")
        else:
            print("Entrée non valide, veuillez réessayer")

    #Bloquage d'une case
    while True:
        input_string = input("Entrez les coordonnées de la case à bloquer (ligne colonne) : ")
        if re.match(pattern, input_string):
            i, j = map(int, input_string.split())
            spot_to_blok = (i,j)
            if game_board[i][j] == "_" :
                BlokSpot(game_board, spot_to_blok)
                break
            else:
                print("Case invalide, veuillez réessayer")
        else:
            print("Entrée non valide, veuillez réessayer")
    boucle = EndGame(game_board)