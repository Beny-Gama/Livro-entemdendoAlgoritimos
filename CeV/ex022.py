nome = str(input('Digite o seu nome completo: '))

maiusculo = nome.upper()
print(maiusculo)

minusculo = nome.lower()
print(minusculo)

cont = len(nome)
print(cont)

primeroNome = nome.split()
print(f"Primenro nsome: {primeroNome[0]} tem {len(primeroNome[0])} letras")