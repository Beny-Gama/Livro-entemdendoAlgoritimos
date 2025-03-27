maior, menor = 0, 0

for i in range(5):
    peso = float(input('Pesso da {}a pessoa: '.format(i + 1)))
    if menor < peso:
        menor = peso
    elif peso > maior:
        maior = peso
    
print(f'A MAIOR pessoa tem: {maior} \n A MENOR pessoa tem: {menor}')
    


    