#Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma
import time
conta = 0

for x in range (1, 11):
    soma = int(input("Digite um numero: \n"))
    if soma % 2 == 0:
        print(f"é multiplo de 2")
        time.sleep(0.05)
        conta = conta + soma
    else:
        0

print(f"\na conta somemente dos numeros pares é: {conta}")
