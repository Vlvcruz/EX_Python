#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

tab = int(input("Digite qual numero deseja a tabuada: "))

for x in range(0, 11):
    soma = tab * x
    print(f"{tab} x {x} = {soma}")