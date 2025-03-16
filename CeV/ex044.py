import os
import sys

print("===== Loja do bgama18 =====")
valor = float(input('Preço da Compra: '))
print('[ 1 ] Á vista dinherio/Cheque')
print('[ 2 ] Á vista no Cartão')
print('[ 3 ] 2x no Cartão')
print('[ 4 ] 3x no Cartão')
option = int(input('Qual a sua Opção: '))

if option == 1:
    valor *= 0.9
    print(f'a vista no dinhero ou cheque tem 10% de desconto: \nvalor a pagar: {valor}')
elif option == 2:
    valor *= 0.95
    print(f'a vista no cartão tem 5% de desconto: \nvalor a pagar: {valor}')
elif option == 3:
    print(f'2x no cartão não tem desconto: \nvalor a pagar: {valor}')
elif option == 4:
    valor *= 1.2
    print(f'3x no cartão o juraos sera de 20% no total: \nvalor a pagar: {valor}')
else:
    print(f'Opção: {option} não existe, tente mais uma fez')
    os.execv(__file__,sys.argv)

