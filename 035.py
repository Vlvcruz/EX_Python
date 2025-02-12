'''Escreva um programa que leia o
Nome, idade e sexo de 4 pessoas. No final mostre:

A média de idade do grupo
Qual é o homem mais velho
Quantas mulheres têm menos de 20 anos
'''
import time

media = 0
maior = 0
cont = 0


for x in range(1, 5):
    nome = input("Digite seu nome: ")
    time.sleep(0.5)
    idade = int(input("Digite sua idade: "))
    time.sleep(0.5)
    sexo = input("Digite seu sexo : ").strip().lower()[0]
    time.sleep(0.5)
    print("----------------------------------------------")
    media = media + idade

    if sexo == "f" and idade <= 20:
        cont = cont + 1

    if maior < idade and sexo == 'm':
        maior = idade
        name2 = nome
    else:
        0

media = media / 4
print(f"Media do Grupo: {media}\n"
      f"Homem mais velho: {name2} com {maior} anos\n"
      f"Quantidade de mulheres menores de 20 anos: {cont}")