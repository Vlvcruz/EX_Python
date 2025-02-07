#Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.

#entrada de dados
numeros = input('Numeros entre espaco: ').split()

#Condicional
if numeros[0] == numeros[1]:
    print('Numeros Iguais')
else:
    print("Numeros Diferentes")

'''
#entrada de dados
numero_um = float(input("Digite o primeiro numero"))
numero_dois = float(input("Digite o segundo numero"))

#Condicional
if numero_um == numero_dois:
    print("Numeros Iguais")
else:
    print("Numeros Diferentes")

'''