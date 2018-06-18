#coding: utf-8

from g_utils import *

def bellman_ford(grafo, fonte):
    p, a = inicializa(grafo, fonte) #p = distancia, a = antecedencia
    for i in range(len(grafo)-1): # roda para o grafo todo
        for u in grafo:
            for v in grafo[u]: # para toda aresta (u,v)
                relaxa(u, v, grafo, p, a) # faz relaxamento
    # roda mais uma vez (ciclo negativo)
    for u in grafo:
        for v in grafo[u]:
            if p[v] > p[u] + grafo[u][v]:
                return None, None, 1

    return p, a, None
