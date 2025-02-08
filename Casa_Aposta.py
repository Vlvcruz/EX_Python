import random

aposta = int(input("Escolha em quem apostar: \n1- Azul\n2- Vermelho\n"))
valor = float(input("Qual valor da aposta ?\n"))

res = valor * 2

azul = random.randint (0, 10)
vermelho = random.randint(0, 10)

if valor > 0:
    if azul > vermelho and aposta == 1:
        print(f"\nVoce ganhou\n{res:.2f} Reais\n")
    elif vermelho > azul and aposta == 2:
        print(f"\nVoce ganhou\n{res:.2f} Reais\n")
    elif azul == vermelho:
        print("\nEmpate, aposta devolvida !")
    else:
        print(f"\nVoce Perdeu: {valor:.2f} Reais \n")
else:
    print("Valor invalido")

print("\nResultado do jogo:")
print(f"Azul: {azul}\nVermelho: {vermelho}")