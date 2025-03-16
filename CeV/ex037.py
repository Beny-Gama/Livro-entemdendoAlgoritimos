num = int(input('Digite um numero: '))
c = int(input('Escolha uma das bases para conversão: \n[ 1 ] Converter para BINARIO\n[ 2 ] Converter para OCTAL\n[ 3 ] Converter para HEXADECIMAL\nSua opção: '))

if c == 1:
    print(f'{num} em BINARIO é iqual a {bin(num)}')
if c == 2:
    print(f'{num} em ACTAL é iqual a {oct(num)}')
if c == 3:
    print(f'{num} em HEXADECIMAL é iqual a {hex(num)}')