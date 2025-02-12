#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos

import time

peso1 = 0
peso2 = 0

for x in range(1, 4):
    peso = float(input("Digite seu Peso: "))
    time.sleep(0.5)
    print("----------------------------------------------")

    if peso1 == 0 and peso2 == 0:
        peso1 = peso
    else:
        peso2 = peso

    if peso1 > peso:
        peso2 = peso
    else:
        0

print(f"Maior Peso: {peso1}\n"
      f"Menor peso: {peso2}\n")