n, soma, cont = 0, 0, 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um numero: [999 para parar] '))
print(f'Voce digitou {cont} numeros e a soma entre eles foi {soma}')