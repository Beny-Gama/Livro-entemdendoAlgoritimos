def my():
    t = []
    cont = 0
    for i in range(4):
        num = int(input(f'Escolha o {i + 1} nuemro: '))
        if num % 2 == 0: cont+=1 
        t.append(num)
    t = tuple(t)
    print(f'O valor 9 aparece: {t.count(9)} vezes...')
    print(f"O valor 3 aparece: {t.index(3)} posição...")
    print(f"O valor Par aparece: {cont}ª vezes.")

my()
