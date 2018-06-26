#coding: utf-8

from g_utils import *

def dijkstrALG(grafo, fonte):
    a = {no:None for no in grafo} #inicia (a)ntecedencia vazia
    d = {no:float('Inf') for no in grafo} #inicia distância infinita
    d[fonte] = 0 #distancia da fonte = 0
    Q = []
    heapq.heappush(Q, [d[fonte], fonte]) #fila de prioridades usa heap
    while(Q):
        u_dist, u_no = heapq.heappop(Q) #pega o nó com menor estimativa
        if u_dist == d[u_no]:
            for vizi_id, vizi_dist in grafo[u_no]: # para cada vizinho do nó
               #faz relaxamento
               if d[u_no] +  vizi_dist < d[vizi_id]:
                   d[vizi_id] = d[u_no] + vizi_dist
                   heapq.heappush(Q, [d[vizi_id], vizi_id])
                   a[vizi_id] = u_no
    #retorna distâncias, atecedências, existência de aresta neg
    return d, a, None

def dijkstra(grafo, fonte):
    if haveNeg(grafo):
        return None, None, 1
    else:
        return dijkstrALG(grafo, fonte)
