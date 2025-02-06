#Crie um programa que leia um nome, e mostre o primeiro e o último nome

#entrada de dados
nome = input("Digite seu nome: ")

#processamento de dados
esq_esp = nome.find(' ') #encontrando primeiro nome
esp_dir = nome.rfind(' ') + 1 #encontrando ultimo nome

#saida de dados
print(f"Primeiro nome: {nome[0:esq_esp]}") #saida do primeiro nome
print(f"Ultimo nome: {nome[esp_dir:]}") #saida do ultimo nome