#Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média,
#é insuficiente (menor que 6),
# suficiente (entre 6 e 7),
# bom (entre 7 e 9) ou
# excelente (9 ou maior).

nota = float(input("Digite primeira nota: \n"))
nota2 = float(input("Digite segunda nota: \n"))
nota3 = float(input("Digite terceira nota: \n"))
nota4 = float(input("Digite quarta nota: \n"))
nota5 = float(input("Digite quinta nota: \n"))

media = (nota + nota2 + nota3 + nota4 + nota5)/5

if media >= 9:
    print("Parabens, Excelente nota !")
elif media == 7 and media < 9:
    print("Nota boa !")
elif media == 6:
    print("Nota suficiente !")
else:
    print("Nota Insuficiente !")