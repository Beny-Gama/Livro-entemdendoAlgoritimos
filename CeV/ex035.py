a = float(input('Primento segumento: '))
b = float(input('Segundo segumento: '))
c = float(input('Terceiro segumento: '))

if a < b + c and b < a + c and c < a + b:
    print('Pode formar um tringulo!')
else:
    print('Os sequiento acime não pode formular um triangulo!')
