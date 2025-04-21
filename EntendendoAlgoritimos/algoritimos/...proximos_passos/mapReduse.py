# qual frequente sao as palavras em um array de frases

from functools import reduce

# Lista de frases
frases = [
    "o sol nasceu",
    "o sol se pôs",
    "a lua brilhou"
]

# MAP: transformar frases em pares (palavra, 1)
def map_func(frases):
    palavras = []
    for frase in frases:
        for palavra in frase.split():
            palavras.append((palavra, 1))
    return palavras

# REDUCE: somar as contagens por palavra
def reduce_func(pares):
    resultado = {}
    for palavra, contagem in pares:
        if palavra in resultado:
            resultado[palavra] += contagem
        else:
            resultado[palavra] = contagem
    return resultado

# Aplicando o MapReduce
map_result = map_func(frases)
reduce_result = reduce_func(map_result)

print(reduce_result)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-= maneira simplificada -=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=

from functools import reduce

# Map: separa palavras
palavras = list(map(lambda frase: frase.split(), frases))
# Flatten a lista
palavras_flat = [palavra for sublist in palavras for palavra in sublist]
# Map: converte para pares
pares = list(map(lambda palavra: (palavra, 1), palavras_flat))

# Reduce manual:
resultado = reduce(lambda acc, par: {**acc, par[0]: acc.get(par[0], 0) + par[1]}, pares, {})

print(resultado)
