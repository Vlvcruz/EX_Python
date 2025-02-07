#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.

'''

Ter entre 16 e 69 anos
Pesar mais de 50 kg
Estar em boas condições de saúde
Apresentar um documento oficial de identidade com foto
Não consumir bebidas alcoólicas nas horas anteriores à doação


idade = input("Digite sua idade: \n")
peso = float(input("Digite seu Peso: \n"))
saude = input("Voce esta com condições boas de saude ?\n S-sim || N - Não\n").upper()
doc = input("Voce esta com seu documento com foto ?\n S-sim || N - Não\n").upper()
alcool = input("Voce consumiu Alcool nas ultimas 48 horas ?\n S-sim || N - Não\n").upper()

if saude == "S" and doc == "S" and alcool == "N":
    if idade >= '16' or idade <= '69' and peso > 50:
        print("Voce esta legivel para ser doador, obrigado !")
    else:
        print("Voce não esta Legivel para ser um doador, mas obrigado pela atenção")
else:
    print("Voce não esta Legivel para ser um doador, mas obrigado pela atenção")

'''

idade = input("Digite sua idade: \n")

if idade >= '16' or idade <= '69':
    peso = float(input("Digite seu peso"))
    if peso >= 50:
        print("Teste")
    else:
        print("Não Legivel")
else:
    print('Não Legivel')