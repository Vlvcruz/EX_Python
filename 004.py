#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

#leitura
raio = float(input("Digite o raio da esfera: "))

#soma da esfera
vol = (4/3) + 3.1415 * raio**3
area = 4 * 3.1415 * raio**2

#saida de dados
print(f"\n O volume da esfera é: {vol:.2f}")
print(f"\n A Area da esfera é: {area:.2f}")