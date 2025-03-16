velocidade = int(input('velocidade atual de um carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Vc ultrasou o limite de velocidade! Sua mulda sera de R$:{multa:.2f}')  
else:
    print(f'Não tera mulda!')