#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

#entrada de dados
letra = input("Digite uma letra: ").lower()

#Condicional
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("Vogal !")
else:
    print("Consoante !")