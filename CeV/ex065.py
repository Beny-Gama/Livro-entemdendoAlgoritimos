cont, maior, menor, soma, resposta = 0, 0, 0, 0, 's'

while resposta != 'n':
    num = int(input('Digite um numero: '))
    soma += num
    cont += 1
    if num > maior:
        maior = num
    elif num < menor: 
        menor = num
    resposta = str(input('Quer continuar: [S/N] ')).lower()[0]
media = soma / cont

print(f'Voce digitou: {cont} números, com a média: {media}')
print(f'O maior valor: {maior} e menor valor: {menor}')