listagem = (
    'Lapis',
    'Borracha'
    'Caderno', 
    'Estojo',
    'Transferidor',
    'Compasso',
    'Mochila', 
    'Canetas',
    'Livro', 
)


for palavra in listagem:
    print('\nlistagem é iqual {palavra.upper()}', end='')
    for letra in palavra:
        if letra.lower() in 'aáãeéêiou':
            print(letra, end=' ')

        