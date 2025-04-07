# o algoritio de Dijkstra é basicamete deva em conta "pesos" para atingir determinado camonho.
# ps1 ele não finciona com pesos negativos: O algoritno de bellman-Ford é o mais comum para caminhos com pesosas negativos.

grafo = []

grafo['inicio'] = []
grafo['inicio']['a'] = 6
grafo['inicio']['b'] = 1

grafo['a'] = []
grafo['a']['fim'] = 1

grafo['b'] = []
grafo['a']['b'] = 3
grafo['b']['fim'] = 5

grafo['fim'] = []

infinito = float('inf')

custos = [];
custos['a'] = 6;
custos['b'] = 2;
custos['fim'] = infinito;

print(grafo['inicio']['a']);

pais = [];
pais['a'] = 'inicio';
pais['b'] = 'inicio';
pais['fim'] = None

processados = []

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float('inf')
    nó_mais_baixo = None
    for nó in custos:
        if custos[nó] < custo_mais_baixo and nó not in processados:
            custo_mais_baixo = custos[nó]
            nó_mais_baixo = nó
    return nó_mais_baixo

nó = ache_no_custo_mais_baixo(custos)

while nó is not None:
    custo = custos[nó]
    vizinhos = grafo[nó]

    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nó

    processados.append(nó)
    nó = ache_no_custo_mais_baixo(custos)





def dijkstra(arr):
    pass