print('-'*40)
print('Loja super Baratão'.center(40))

total, cont_maior, preco_maior, preco_menor, item_menor, continuar = 0, 0, 0, 0, '', ''

while continuar != 'N':
    print('-'*40)
    item = str(input('Nome do Produto: '))
    preco = int(input('Valor do Produto: '))

    if preco > preco_maior:
        cont_maior += 1
        preco_maior = preco
    
    
    if preco < preco_menor or total == 0:
        preco_menor = preco
        item_menor = item

    total += preco

    continuar = str(input('quer continuar? [S/N] ')).upper()[0]
    

print('-'*12, 'Fim do Programa', '-'*11)
print(f'O total da compra foi: R$: {total}')
print(f'Temos {cont_maior} Produtos custanado mais de R$: {preco_maior}')
print(f'O Produto mais barato foi {item_menor} que custou R$: {preco_menor}')