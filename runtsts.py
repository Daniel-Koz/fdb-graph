#coding: utf-8

from bell import bellman_ford
from dijk import dijkstra
from floy import floyd_warshall
from bigGrafo import gb


fonte = 's'
grafo = {'s': {'u': 10, 'x':  5},
         'u': {'v':  1, 'x':  2},
         'v': {'y':  4},
         'x': {'u':  3, 'v':  9, 'y':  2},
         'y': {'s':  7, 'v':  6}
        }
grafo2 = [[0, 10, 0, 5, 0],
          [0,  0, 1, 2, 0],
          [0,  0, 0, 0, 4],
          [0,  3, 9, 0, 2],
          [7,  0, 6, 0, 0]]
grafo2unused =  gb(7)

def dij():
    print("Dijkstra: \n")
    distancias, antecedencias, existeCicloNeg = dijkstra(grafo, fonte)
    if existeCicloNeg:
        print("Existe pelo menos uma aresta com peso negativo, não se pode usar Dijkstra.")
    else:
        print("Distância da fonte ", fonte, " para os nós: \t", distancias)
        print("Antecessores dos nós: \t\t\t", antecedencias)

def bel():
    print("Bellman Ford: \n")
    distancias, antecedencias, cicloneg = bellman_ford(grafo, fonte)
    if cicloneg:
        print("Ciclo negativo encontrado.")
    else:
        print("Distância da fonte ", fonte, " para os nós: \t", distancias)
        print("Antecessores dos nós: \t\t\t", antecedencias)

def flo():
    print("Floyd Warshall: \n")
    print("Grafo entrada:\n s, u, v, x, y")
    for i in range(len(grafo2)):
        print(grafo2[i])
    antec, grafo = floyd_warshall(grafo2)
    print("Grafo saída:\n s, u, v, x, y")
    for i in range(len(grafo2)):
        print(grafo[i])
    print('\n')
    for i in range(len(grafo2)):
        print(antec[i])

if __name__ == '__main__':
    print('\n')
    nodes = list(grafo.keys())
    for node in nodes:
        fonte = node
        dij()
    #print('\n\n')
    #bel()
    print('\n\n')
    flo()
    print('\n')

