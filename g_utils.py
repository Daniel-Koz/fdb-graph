#coding: utf-8

import heapq
import random

random.seed(1)

def inicializa(grafo, fonte):
    p = {} # peso
    a = {} # antecessor
    for no in grafo:
        p[no] = float('Inf') # inicializa no com "infinito"
        a[no] = None
    p[fonte] = 0 # peso da fonte
    return p, a

def relaxa(no, vizinho, grafo, p, a):
    # se a distancia do no ao vizinho é menor que a atual
    if p[vizinho] > p[no] + grafo[no][vizinho]:
        # salva a distância menor
        p[vizinho] = p[no] + grafo[no][vizinho]
        a[vizinho] = no

def haveNeg(grafo):
    for i in range(len(grafo)-1): # roda para o grafo todo
        for u in grafo:
            for v in grafo[u]: # para toda aresta (u,v)
                if (v[1] < 0):
                    return 1
    return None

def dijkPrep(grafo):
    keys = list(grafo.keys())
    grafoR = {}
    for i in range(len(keys)):
        grafoR[keys[i]] =  list(grafo.get(keys[i]).items())
    return grafoR

def makeZero(grafo):
    return [[0 for i in range(len(grafo))] for j in range(len(grafo))]

def showPathFloy(p, i, j):
    i,j = int(i), int(j)
    if(i==j):
      print(i,)
    elif(p[i][j] == -float('Inf')):
      print(i,'-',j)
    else:
      showPathFloy(p, i, p[i][j]);
      print(j,)

def gb(tam):
    return [[random.randint(1,100) for i in range(tam)] for j in range(tam)]

def gd(tam):
    grafo = {i:{j:random.randint(1,100) for j in range(tam)}for i in range(tam)}
    return dijkPrep(grafo)
