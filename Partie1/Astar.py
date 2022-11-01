# Using a Python dictionary to act as an adjacency list
from queue import Empty

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
minotaure = (2,5)

def a_star(goal, start, graph):
    queue = [[start]]
    print("La file est initiée au noeud start :", queue)
    node1 =[0,0]
    while len(queue) != 0 :
        node = list(queue[0][-1]) # coordonnées en mode liste ex : (2.5) -> [2.5]
        infoNode = graph[queue[0][-1]].copy() # dico avec infos sur direction {'W':1, 'N':0, 'E':0, 'S':0}
        save = queue.pop(0)
        kidpath = save.copy()
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
                node2 = node1.copy()
                node2 = tuple(node2)
                if node2 not in kidpath:
                    kidpath.append(node2)
                    queue.insert(0,kidpath)
                    print("File incrémentée d'un noeud enfant ", queue)
                if node2 == goal:
                    print("Ce chemin à atteint le goal", node2)
        queue = sorting(queue) #Tri de la queue entière après insertion des noeuds enfants
        print("Etat de la file après le tri : ", queue, len(queue))
        boole = False
        while boole == False : #Gesion des chemins redondants
            boole, queue = delete_rundondant_paths(queue, graph, boole)
        if goal in queue[0]:
            print("Dernière queue : ",queue, len(queue))
            return queue[0]
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

def accumulated_cost(path):
    cost = len(path)-1
    return cost

def sum_heuristic_accumulated_cost(path, graph):
    sum = accumulated_cost(path) + graph[path[-1]]['H']
    #print(" noeud ", path[-1], " cout accumulé + heuristic: ", accumulated_cost(path), "+ ", graph[path[-1]]['H'], "= ", sum)
    return sum

def delete_rundondant_paths(path, graph, boole):
    for i in range (len(path)):
        for j in range(len(path)):
            #print("dernier noeud du chemin : ", path[i][-1], path[j])
            if i != j and path[i][-1] in path[j] and sum_heuristic_accumulated_cost(path[i], graph) >= sum_heuristic_accumulated_cost(path[j], graph):
                del(path[i])
                boole = False
                return boole, path
    boole = True
    return boole, path
                
def sorting(liste):
    for i in range(len (liste)):
        mini=i
        for j in range(i+1, len (liste)):
            if sum_heuristic_accumulated_cost(liste[j], graph) < sum_heuristic_accumulated_cost(liste[mini], graph) :
                #print(sum_heuristic_accumulated_cost(liste[j], graph), sum_heuristic_accumulated_cost(liste[mini], graph))
                mini = j
        liste[i], liste[mini] = liste[mini], liste[i]
    return liste

heuristic(graph, thesee)
print('le chemin choisi est : ', a_star(thesee, minotaure, graph))