#Escreva um programa que calcule a soma de todos os números múltiplos de 4 que são encontrados entre 1 até 500
import time

print("Iniciando contagem...")
time.sleep(1.6)
conta = 0

for x in range (1, 500 +1):
    soma = x % 4 == 0
    if soma == True:
        print(f"{x} = é Multiplo de 4")
        time.sleep(0.05)
        conta = conta + x
    else:
        0

print(f"\n{conta}")
