############### ISOLA ##################

########################################
#  Import Packages
########################################

import numpy as np

########################################
#   Definitions of Functions
########################################

'Get all positions player can move on'

def get_adjacent_positions(pos,game_board):
    i, j = pos  # Dépacking de la position du pion
    adjacent_positions = []  # Liste des positions adjacentes
    
    # Vérification des cases adjacentes et en diagonales
    if i > 0:  # Case au-dessus
        if game_board[i-1][j] != "X":
            adjacent_positions.append((i-1, j))
        if j > 0:  # Case en haut à gauche
            if game_board[i-1][j-1] != "X":
                adjacent_positions.append((i-1, j-1))
        if j < 5:  # Case en haut à droite
            if game_board[i-1][j+1] != "X":
                adjacent_positions.append((i-1, j+1))
    if i < 5:  # Case en-dessous
        if game_board[i+1][j] != "X":
            adjacent_positions.append((i+1, j))
        if j > 0:  # Case en bas à gauche
            if game_board[i+1][j-1] != "X":
                adjacent_positions.append((i+1, j-1))
        if j < 5:  # Case en bas à droite
            if game_board[i+1][j+1] != "X":
                adjacent_positions.append((i+1, j+1))
    if j > 0:  # Case à gauche
        if game_board[i][j-1] != "X":
            adjacent_positions.append((i, j-1))
    if j < 5:  # Case à droite
        if game_board[i][j+1] != "X":
            adjacent_positions.append((i, j+1))
    if len(adjacent_positions) == 0:
        return 0
    return adjacent_positions

########################################

'Change Position of Player'

def PlayerMove(player_pos, adv_pos,nbr_player):
    while True:
    # Choisir une case ou avancer
        if get_adjacent_positions(player_pos,game_board) == 0:
            return 0
        print("Positions valides :", get_adjacent_positions(player_pos,game_board))
        game_board[player_pos[0]][player_pos[1]] = " "
        i, j = map(int, input("Entrez les coordonnées de la case (ligne colonne) : ").split())
        if (i, j) in get_adjacent_positions(player_pos,game_board) and (i, j) != adv_pos:
            player_pos = (i, j)
            if nbr_player == 1:
                game_board[player_pos[0]][player_pos[1]] = "1"
            else : 
                game_board[player_pos[0]][player_pos[1]] = "2"
            return player_pos
        else:
            print("Case non valide, veuillez réessayer")
            continue  # Recommencez le tour

########################################

'Blok access of one case of the board'

def BlokCase(game_board, player_pos, adv_pos):
    while True:
    # Sélectionner une case à bloquer
        i, j = map(int, input("Entrez les coordonnées de la case à bloquer (ligne colonne) : ").split())
        if game_board[i][j] != "X" and (i,j) != player_pos and (i,j) != adv_pos:
            game_board[i][j] = "X"
            break
        elif (i,j) == player_pos and (i,j) == adv_pos:
            print("Un pion se trouve sur cette case, veuillez réessayer")
        else:
            print("Case déjà bloquée, veuillez réessayer")
            continue  # Recommencez le tour

########################################
#        MAIN
########################################

# Création du tableau de jeu
game_board = [
    [" "," "," "," "," "," "],
    [" "," "," "," "," "," "],
    [" "," "," "," "," "," "],
    [" "," "," "," "," "," "],
    [" "," "," "," "," "," "],
    [" "," "," "," "," "," "],
]

# Positions initiales des pions
player1_pos = (0,4)  # Coin supérieur gauche
player2_pos = (5,3)  # Coin inférieur droit
game_board[player1_pos[0]][player1_pos[1]] = "1"
game_board[player2_pos[0]][player2_pos[1]] = "2"

while True:  # Boucle de jeu

    # Tour du joueur 1
    print("Au tour du joueur 1")
    print(np.array(game_board))
    nbr_player = 1
    player1_pos = PlayerMove(player1_pos,player2_pos,nbr_player)
    if player1_pos == 0:
        print("Joueur 1, vous avez perdu, il n'y a plus moyen de bouger votre pion")
        break
    BlokCase(game_board, player1_pos, player2_pos)

    # Tour du joueur 2
    print("Au tour du joueur 2")
    print(np.array(game_board))
    nbr_player = 2
    player2_pos = PlayerMove(player2_pos,player1_pos,nbr_player)
    if player2_pos == 0:
        print("Joueur 2, vous avez perdu, il n'y a plus moyen de bouger votre pion")
        break
    BlokCase(game_board, player2_pos, player1_pos)