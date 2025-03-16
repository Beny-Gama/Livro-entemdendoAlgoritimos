distance = float(input('Qual é a Distacia em KM: '))
price = distance * 0.5 if distance <= 200 else distance * 0.45
print(f'a Viagem vai custar: R$:{price:.2f}')

# if distance < 200:
#     calc = distance * 0.5
#     print(f'a Viagem vai custar: R$:{calc:.2f}')
# else:
#     calc = distance * 0.45
#     print(f'a Viagem vai custar: R$:{calc:.2f}')