n = int(input('digite o nomero para fazer uma tabiada: '))
ate = int(input('ate onde vc quer fazer sua tabuada: '))

for nn in range(ate + 1):
    print(f"{n} X {nn} = {n * nn}")
