preco = float(input('Qual é o preço do produto: '))
desconto = int(input('Qual é o desconto (em %): '))

resultado = preco * (1 - desconto / 100)  # Aplica o desconto corretamente

print(f'O preço com desconto é: {resultado:.2f}')  # Exibe o resultado formatado com duas casas decimais
