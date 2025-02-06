#Crie um programa que leia o nome completo de uma pessoa e mostre:

#entrada de dados
nome_c = input("Digite seu nome: ").strip() #entrada de dados sem espaco
nome_completo_sem_espaco = nome_c.replace(' ', '') #remocao dos espacos
esp = nome_c.find(" ") + 1 #encontrando primeiro espaco e pegando primeiro nome

print(f'nome tudo maiusculo: {nome_c.upper()}') # texto em maiusculo
print(f'nome tudo minusculo: {nome_c.lower()}') # texto em minusculo
print(f'Quantidade caracter: {len(nome_completo_sem_espaco)}') # quantidade de caracter
print(f"Primeiro nome: {nome_c[0:esp]}") #primeiro nome

