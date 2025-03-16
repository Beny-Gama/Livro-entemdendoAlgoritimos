# recursividade e pilha

# fatiral!
# ex: 5! = 5 * 4 * 3 * 2 = 120
def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)

print(fat(5))


# as veses usar a fucão recursiva ocupa muito estaço na mememora. devemos viltar para loops normais: for, while... ou considerar usar recursão de cauda (tail recursion)

def fat_tail(x, acumulador=1):
    if x == 1:
        return acumulador
    return fat_tail(x - 1, x * acumulador)

print(fat_tail(5))  # Saída: 120

# loop 1: x = 5, acumulador = 1  === 5 * 5 = 25 
# loop 2: x = 4, acumulador = 5  === 4 * 5 = 