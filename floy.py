#coding: utf-8

from g_utils import *

def floyd_warshall(grafo):
    antec = []
    v = len(grafo)
    p = makeZero(grafo)
    for i in range(0,v):
        for j in range(0,v):
            p[i][j] = i
            if (i != j and grafo[i][j] == 0):
                p[i][j] = -float('Inf')
                grafo[i][j] = float('Inf')

    for k in range(0,v):
        for i in range(0,v):
            for j in range(0,v):
                if grafo[i][j] > grafo[i][k] + grafo[k][j]:
                    grafo[i][j] = grafo[i][k] + grafo[k][j]
                    p[i][j] = p[k][j]
    #retorna (distâncias, antecedências)
    return grafo, p
