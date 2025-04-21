# https://youtu.be/lcooPuujcVM?si=9Z8nn-nM2rvogma-
from collections import deque

grafo={}
grafo["vc"]=["Joanilsda", "Carlendson", "Danisvardo"]
grafo["Joanilsda"]=["Cleonistica", "Marlindston"]
grafo["Carlendson"]=["Anistilgides", "Gabrandeia"]
grafo["Danisvardo"]=["Jocarlisto"]
grafo["Cleonistica"]=[]
grafo ["Marlindston" ]=[]
grafo["Anistilgides"]=[]
grafo["Gabrandeia" ]=[]
grafo["Jocarlisto"]=[]
print (grafo ["vc"])

def pesquisa_largura():
    fila_pesquisa = deque()
    fila_pesquisa += grafo['vc']
    encontrado = False
    verificados = []
    while fila_pesquisa:
        pessoas = fila_pesquisa.popleft()
          