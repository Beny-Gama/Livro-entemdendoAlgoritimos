altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = peso / altura

if imc < 18.5:
    situação = 'Abaixo do Peso'
    calc = (18.5 + (imc - 18.5))
elif 18.5 <= imc < 25:
    situação = 'Pesso Ideal'
elif 25 < imc < 30:
    situação = 'Sobrepeso'
elif 30 < imc < 40:
    situação = 'Obesidade'
elif imc > 40:
    situação = 'Obesidade Morbida'

print(f'Seu IMC é: {imc} \nlogo vc está com: {situação} \n Voce deve ')