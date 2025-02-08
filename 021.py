#Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).

#entrada de dados
nmr = int(input("Digite um numero entre 1 a 7\n"))

#Condicional
if nmr == 0 or nmr > 7:
    print("Numero digitado nao e valido !")
elif nmr == 1:
    print("Segunda")
elif nmr == 2:
    print("Terca-feira")
elif nmr == 3:
    print("Quarta-feira")
elif nmr == 4:
    print("Quinta-feira")
elif nmr == 5:
    print("Sexta-feira")
elif nmr == 6:
    print("Sabado")
else:
    print("domingo")