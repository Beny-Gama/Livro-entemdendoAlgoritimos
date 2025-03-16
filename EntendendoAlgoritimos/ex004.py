# pilha

def sauda(nome):
    print('Olá, ' + nome + '!')
    sauda2(nome)
    print('preprarando para duzer tchau...')
    tchau()

def sauda2(nome):
    print('como vai ' + nome + '?')
def tchau():
    print('Ok. thau!')

sauda('Bernardo')