#Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.

#Entrada de dados
frase = input("Digite sua frase :").strip().lower()[0]

#Condição
if frase in 'aeiou': #in -> valida se esta dentro de um bloco de caracter
    print("Sua frase comeca com uma Vogal")
else:
    print("Sua frase comeca com uma Consoante")