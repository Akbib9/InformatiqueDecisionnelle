import time
import psutil
import os

graph = {
    (1,1) : {'W':0, 'N':0, 'E':1, 'S':0},
    (1,2) : {'W':1, 'N':0, 'E':1, 'S':1},
    (1,3) : {'W':1, 'N':0, 'E':0, 'S':0},
    (1,4) : {'W':0, 'N':0, 'E':1, 'S':1},
    (1,5) : {'W':1, 'N':0, 'E':1, 'S':0},
    (1,6) : {'W':1, 'N':0, 'E':1, 'S':0},
    (1,7) : {'W':1, 'N':0, 'E':0, 'S':0},
    (2,1) : {'W':0, 'N':0, 'E':0, 'S':1},
    (2,2) : {'W':0, 'N':1, 'E':1, 'S':1},
    (2,3) : {'W':1, 'N':0, 'E':1, 'S':0},
    (2,4) : {'W':1, 'N':1, 'E':1, 'S':1},
    (2,5) : {'W':1, 'N':0, 'E':1, 'S':1},
    (2,6) : {'W':1, 'N':0, 'E':1, 'S':0},
    (2,7) : {'W':1, 'N':0, 'E':0, 'S':1},
    (3,1) : {'W':0, 'N':1, 'E':1, 'S':1},
    (3,2) : {'W':1, 'N':1, 'E':0, 'S':1},
    (3,3) : {'W':0, 'N':0, 'E':1, 'S':1},
    (3,4) : {'W':1, 'N':1, 'E':0, 'S':0},
    (3,5) : {'W':0, 'N':1, 'E':1, 'S':0},
    (3,6) : {'W':1, 'N':0, 'E':0, 'S':0},
    (3,7) : {'W':0, 'N':1, 'E':0, 'S':1},
    (4,1) : {'W':0, 'N':1, 'E':0, 'S':1},
    (4,2) : {'W':0, 'N':1, 'E':0, 'S':0},
    (4,3) : {'W':0, 'N':1, 'E':0, 'S':1},
    (4,4) : {'W':0, 'N':0, 'E':1, 'S':1},
    (4,5) : {'W':1, 'N':0, 'E':1, 'S':0},
    (4,6) : {'W':1, 'N':0, 'E':1, 'S':0},
    (4,7) : {'W':1, 'N':1, 'E':0, 'S':1},
    (5,1) : {'W':0, 'N':1, 'E':1, 'S':1},
    (5,2) : {'W':1, 'N':0, 'E':0, 'S':1},
    (5,3) : {'W':0, 'N':1, 'E':0, 'S':1},
    (5,4) : {'W':0, 'N':1, 'E':0, 'S':1},
    (5,5) : {'W':0, 'N':0, 'E':1, 'S':0},
    (5,6) : {'W':1, 'N':0, 'E':1, 'S':1},
    (5,7) : {'W':1, 'N':1, 'E':0, 'S':1},
    (6,1) : {'W':0, 'N':1, 'E':0, 'S':0},
    (6,2) : {'W':0, 'N':1, 'E':1, 'S':0},
    (6,3) : {'W':1, 'N':1, 'E':1, 'S':0},
    (6,4) : {'W':1, 'N':1, 'E':1, 'S':0},
    (6,5) : {'W':1, 'N':0, 'E':0, 'S':1},
    (6,6) : {'W':0, 'N':1, 'E':0, 'S':1},
    (6,7) : {'W':0, 'N':1, 'E':0, 'S':0},
    (7,1) : {'W':0, 'N':0, 'E':1, 'S':0},
    (7,2) : {'W':1, 'N':0, 'E':1, 'S':0},
    (7,3) : {'W':1, 'N':0, 'E':1, 'S':0},
    (7,4) : {'W':1, 'N':0, 'E':1, 'S':0},
    (7,5) : {'W':1, 'N':1, 'E':1, 'S':0},
    (7,6) : {'W':1, 'N':1, 'E':1, 'S':0},
    (7,7) : {'W':1, 'N':0, 'E':0, 'S':0},
}

thesee = (6,1)
minotaure = (4,7)

def dfs(goal, start, graph):
    #On initialise la file au noeud Start
    queue = [[start]]
    print(queue)
    node1 =[0,0]
    #Tant que la file n'est pas vide
    while len(queue) != 0:
        node = list(queue[0][-1]) # coordonnées en mode liste ex : (2.5) -> [2.5]
        infoNode = graph[queue[0][-1]].copy() # dico avec infos sur direction {'W':1, 'N':0, 'E':0, 'S':0}
        #On retire le premier chemin de la file
        save = queue.pop(0)
        #On créé tous les nouveaux chemins enfants s'ils existent
        for direction in 'WSEN':
            if infoNode[direction] == 1: #S'il est possible d'aller dans la direction traitée
                if direction == 'N':#Si on va vers le Nord,
                    node1[0] = node[0] - 1 # on enregistre un noeud contenant avec la position du noeud qu'on traite -1 sur la ligne car le point 0,0 se trouve en haut à gauche
                    node1[1] = node[1] #On reste sur la même colonne
                elif direction == 'E':
                    node1[1] = node[1] + 1
                    node1[0] = node[0]
                elif direction == 'S':
                    node1[0] = node[0] + 1
                    node1[1] = node[1]
                elif direction == 'W':
                    node1[1] = node[1] - 1
                    node1[0] = node[0]
                kidpath = save.copy() #On enregistre l'état du chemin actuel pour vérifier les loop
                node2 = tuple(node1)
                #On vérifie qu'il n'y a pas de boucle
                if node2 not in kidpath:
                    #Si pas de loop, on ajoute le nouveau chemin enfant à l'avant de la file
                    kidpath.append(node2)
                    queue.insert(0,kidpath)
                    print("File incrémentée d'un noeud enfant au début de la file :", queue)
                if node2 == goal:
                    #print("Dernière queue : ",queue)
                    return kidpath
        infoNode = infoNode.clear()
        print("Nouvelle queue suite à l'ajout des noeuds enfants : ", queue)

#Temps écoulé avant la fonction
start_time = time.perf_counter()
#mémoire consomée avant la fonction
process = psutil.Process(os.getpid())
before = process.memory_info().rss / (1024 ** 2)
#Appel de la fonction DFS
a = dfs(minotaure, thesee, graph)
#Temps écoulé après la fonction
end_time = time.perf_counter()
#Mémoire consommée après la fonction
after = process.memory_info().rss / (1024 ** 2)

print("Le chemin à parcourir pour trouver le Minautore est : ",a)
print(f'Temps d\'écoulé : {end_time - start_time} secondes')
print(f"Le script a utilisé {after - before} Mega bytes de mémoire.")