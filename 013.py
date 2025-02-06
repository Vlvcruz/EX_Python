'''Crie um programa que leia uma frase e mostre:
Em que posição ela aparece na última vez
Quantas vezes aparece a letra “a”
Em que posição ela aparece a primeira vez
'''

#Recebimento de dados
nome = input("Digite seu nome: ")
prim = nome.find('a') + 1 #encontrando a posicao do primeiro a
ulti = nome.rfind('a') + 1 # encontrando a posicao do ultima a

#saida de dados
print(f"Quantidade de 'a' tem {nome.count('a')}") #contando a quantidade de caracteristica
print(f" Posicao primeira vez 'a': {prim}")
print(f"Posicao ultima vez 'a': {ulti}")