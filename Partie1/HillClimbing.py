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
    queue = [[start]]
    print(queue)
    node1 =[0,0]
    while len(queue) != 0:
        node = list(queue[0][-1]) # coordonnées en mode liste ex : (2.5) -> [2.5]
        infoNode = graph[queue[0][-1]].copy() # dico avec infos sur direction {'W':1, 'N':0, 'E':0, 'S':0}
        save = queue.pop(0)
        kidpath = save.copy()
        kidspath = []
        for direction in 'WSEN':
            if infoNode[direction] == 1:
                if direction == 'N':
                    node1[0] = node[0] - 1
                    node1[1] = node[1]
                elif direction == 'E':
                    node1[1] = node[1] + 1
                    node1[0] = node[0]
                elif direction == 'S':
                    node1[0] = node[0] + 1
                    node1[1] = node[1]
                elif direction == 'W':
                    node1[1] = node[1] - 1
                    node1[0] = node[0]
                kidpath = save.copy()
                node2 = tuple(node1)
                if node2 not in kidpath:
                    kidpath.append(node2)
                    kidspath.append(kidpath)
                    #print(kidspath)
                if node2 == goal:
                    #print("Dernière queue : ",queue)
                    return kidpath
        print("Voici les chemins enfants non triés : ",kidspath)
        kidspath = sorting(kidspath, graph) #Tri des noeuds enfants (ordre coirssant) avant de les inserer dans la queue
        print("Voici les chemins enfants triés avant d'être ajoutés : ",kidspath)
        for path in kidspath[::-1]:
            queue.insert(0,path)
        infoNode = infoNode.clear()
        print("Nouvelle queue : ", queue)


def heuristic(graph, goal):
    for cle in graph.keys():
        xgoal = goal[0]
        ygoal = goal[1]
        #print(xgoal, ygoal)
        xcle = cle[0]
        ycle = cle[1]
        #print(xcle, ycle)
        diffx = abs(xgoal-xcle)
        diffy = abs(ygoal-ycle)
        #print(diffx, diffy)
        heurinode = diffx+diffy
        #print(heurinode)
        graph[cle]['H'] = heurinode
        #print(graph[cle])

def sorting(liste, graph):
    for i in range(len (liste)):
        mini=i
        for j in range(i+1, len (liste)):
            if graph[liste[j][-1]]['H']<graph[liste[mini][-1]]['H'] :
                #print(graph[liste[j][-1]]['H'], graph[liste[mini][-1]]['H'])
                print("Changement de place !")
                mini = j
        liste[i], liste[mini] = liste[mini], liste[i]
    return liste

heuristic(graph, minotaure)

#Temps écoulé avant la fonction
start_time = time.perf_counter()
#mémoire consomée avant la fonction
process = psutil.Process(os.getpid())
before = process.memory_info().rss / (1024 ** 2)
#Appel de la fonction iterative Deepening
print('le chemin choisi est : ', dfs(minotaure, thesee, graph))
#Temps écoulé après la fonction
end_time = time.perf_counter()
#Mémoire consommée après la fonction
after = process.memory_info().rss / (1024 ** 2)

print(f'Temps d\'écoulé : {end_time - start_time} secondes')
print(f"Le script a utilisé {after - before} bytes de mémoire.")