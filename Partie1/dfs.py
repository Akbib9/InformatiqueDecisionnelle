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
    (3,7) : {'W':1, 'N':0, 'E':0, 'S':1},
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

def dfs(goal, start, graph):
    queue = [[start]]
    print(queue)
    node1 =[0,0]
    while len(queue) != 0:
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
                node2 = tuple(node1)
                if node2 not in kidpath:
                    kidpath.append(node2)
                    queue.insert(0,kidpath)
                if node2 == goal:
                    print("Dernière queue : ",queue)
                    return kidpath
        infoNode = infoNode.clear()
        print("Nouvelle queue : ", queue)

a = dfs(thesee, minotaure, graph)
print("Le chemin enfant est : ",a)