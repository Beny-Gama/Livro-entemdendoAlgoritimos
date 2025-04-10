# Algoritmo de Dijkstra (sem pesos negativos)

# Estrutura do grafo
grafo = {}
grafo['inicio'] = {}
grafo['inicio']['a'] = 6
grafo['inicio']['b'] = 1

grafo['a'] = {}
grafo['a']['fim'] = 1

grafo['b'] = {}
grafo['b']['a'] = 3
grafo['b']['fim'] = 5

grafo['fim'] = {}

# Custos iniciais
infinito = float('inf')

custos = {}
custos['a'] = 6
custos['b'] = 1
custos['fim'] = infinito

# Pais (ou predecessores)
pais = {}
pais['a'] = 'inicio'
pais['b'] = 'inicio'
pais['fim'] = None

# Nós já processados
processados = []

# Função para encontrar o nó com menor custo
def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float('inf')
    no_mais_baixo = None
    for no in custos:
        if custos[no] < custo_mais_baixo and no not in processados:
            custo_mais_baixo = custos[no]
            no_mais_baixo = no
    return no_mais_baixo

# Loop principal do algoritmo
no = ache_no_custo_mais_baixo(custos)
while no is not None:
    custo = custos[no]
    vizinhos = grafo[no]
    for n in vizinhos:
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = no
    processados.append(no)
    no = ache_no_custo_mais_baixo(custos)

# Resultado final
print("Custos finais:", custos)
print("Caminho até o fim:")
no = 'fim'
caminho = []
while no != 'inicio':
    caminho.append(no)
    no = pais[no]
caminho.append('inicio')
caminho.reverse()
print(" -> ".join(caminho))
