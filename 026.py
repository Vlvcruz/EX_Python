#Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

peso = float(input("Digite seu peso: \n"))
alt = float(input("Digite sua altura: \n"))

imc = peso / (alt**2)

if imc <= 18.5:
    print("Abaixo do normal")
elif imc >= 18.6 and imc <= 24.9:
    print("Normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade grau I")
elif imc >= 35 and imc <= 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")
