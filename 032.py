#Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.

num = int(input("Digite um numero: \n"))
num2 = int(input("Digite um numero: \n"))

for x in range(num, num2 +1):
    soma = x % 2 == 0
    if soma == False:
        print(f"{x} = Impar")
    else:
        print(f"{x} = Par")