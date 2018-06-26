#coding: utf-8

from bell import bellman_ford
from dijk import dijkstra
from floy import floyd_warshall
from g_utils import *

#===============================================================================
#observem os dados
fonte = 's'

grafo = {'s': [('u', 10), ('x',  5)],
         'u': [('v',  1), ('x',  2)],
         'v': [('y',  4)],
         'x': [('u',  3), ('v',  9), ('y',  2)],
         'y': [('s',  7), ('v',  6)]
        }

print("OBS: 0=S,1=U,2=V,3=X,4=Y")
grafo2 = [[0, 10, 0, 5, 0],
          [0,  0, 1, 2, 0],
          [0,  0, 0, 0, 4],
          [0,  3, 9, 0, 2],
          [7,  0, 6, 0, 0]]

grafoaa  = gd(50)

grafo2aa = gb(50)
#===============================================================================

def dij():
    print("Dijkstra:\n")
    distancias, antecedencias, existeCicloNeg = dijkstra(grafo, fonte)
    if existeCicloNeg:
        print("Existe pelo menos uma aresta com peso negativo, não se pode usar Dijkstra.")
    else:
        print("Distância da fonte", fonte, "para os nós:\t", distancias)
        print("Antecessores dos nós:\t\t\t", antecedencias)

def bel():
    print("Bellman Ford:\n")
    distancias, antecedencias, cicloneg = bellman_ford(grafo, fonte)
    if cicloneg:
        print("Ciclo negativo encontrado.")
    else:
        print("Distância da fonte", fonte, "para os nós:\t", distancias)
        print("Antecessores dos nós:\t\t\t", antecedencias)

def flo():
    print("Floyd Warshall:\n")
    print("Grafo entrada:\n")
    for i in range(len(grafo2)):
        print(grafo2[i])
    grafo, antec = floyd_warshall(grafo2)
    print("\nDistâncias:\n")
    for i in range(len(grafo2)):
        print(grafo[i])
    print("\nAntecedências:\n")
    for i in range(len(grafo2)):
        print(antec[i])
    x = int(input("Para caminhar no grafo informe o nó de partida:"))
    y = int(input("Informe o nó de chegada:"))
    showPathFloy(antec, x, y)

if __name__ == '__main__':
    
    print('\n\n')
    bel()


    print('\n\n')
    nodes = list(grafo.keys())
    #rodando dijkstra de todos para todos
    for node in nodes:
        fonte = node
        dij()


    print('\n\n')
    flo()
    print('\n')

