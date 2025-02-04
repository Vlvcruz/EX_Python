#Escreva um programa que leia o nome, e o sobrenome, CONCATENE em uma nova variável nome completo, e retorne para o usuário

name = input("Digite seu nome: \n")
s_name = input("Digite seu sobre nome: \n")

n_completo = name + ' ' + s_name 

print(f"Seu nome completo é: {n_completo}")
