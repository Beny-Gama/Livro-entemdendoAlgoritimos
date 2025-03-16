a = float(input('Primento segumento: '))
b = float(input('Segundo segumento: '))
c = float(input('Terceiro segumento: '))

if a < b + c and b < a + c and c < a + b:
    print('Pode formar um tringulo!')
    if a == b == c:
        print('O trinagulo é Reantgulo')
    elif a != b != c != a:
        print('É um triangulo Escaleno')
    else:
        print('É triangulo Esóteles')  
else:
    print('Os sequiento acime não pode formular um triangulo!')
