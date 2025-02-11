#Escreva um programa que verifique se uma palavra é um palíndromo.

palavra = input("Digite sua palavra: \n").strip().lower()
pont = 0

for i in range(0, len(palavra)):
    if palavra[i] == palavra[-i -1]:
        pont = pont + 1

if pont == len(palavra):
    print("é Palíndromo")
else:
    print("Não é Palíndromo")
