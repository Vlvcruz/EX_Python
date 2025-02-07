#Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.

#entrada de dados
nmr = float(input("Digite um numero: "))

#Condicional para saber se é maior de idade
if nmr >= 0 and nmr <= 9:
    print("Numero digitado esta entre 0 e 10 !")#Saida de dados
elif nmr >= 11 and nmr <= 20:
    print("Numero digitado esta entre 10 e 20 !")#Saida de dados
elif nmr == 10:
    print("Numero esta entre 0 a 10 e 10 a 20")
else:
    print("Numero maior que 20 !")