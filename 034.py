#Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma
import time


for x in range (1, 11):
    soma = int(input("Digite um numero: \n"))
    if x % 2 == 0:
        print(f"{x} = multiplo de 2")
        time.sleep(0.05)
        conta = conta + x
    else:
        0

print(f"\na conta somemente dos numeros pares é: {conta}")

#nao finalizado