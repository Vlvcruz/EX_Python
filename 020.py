#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.
'''
Ter entre 16 e 69 anos
Pesar mais de 50 kg
Estar em boas condições de saúde
Apresentar um documento oficial de identidade com foto
Não consumir bebidas alcoólicas nas horas anteriores à doação

'''

#entrada de dados
idade = int(input("Digite sua idade: \n"))

#Condicional validação

if idade > 16 and idade < 69:
    peso = float(input("Digite seu Peso: \n"))
    if peso > 50:
        saude = input("Voce esta com condições boas de saude ?\n [S/N] \n").strip().upper()[0]
        if saude == 'S':
            doc = input("Voce esta com seu documento com foto ?\n [S/N]\n").strip().upper()[0]
            if doc == 'S':
                alcool = input("Voce consumiu Alcool nas ultimas 12 horas ?\n [S/N]\n").strip().upper()[0]
                if alcool == "S":
                    print("Legivel a doação !")
                else:
                    print("Nao legivel, alcool no sangue")
            else:
                print("Necessario uso de documento com foto")
        else:
            print("Precisa estar com saude em dia")
    else:
        print("Necessario peso maior que 50kg")
else:
    print("idade nao permitida")


'''
if saude == "S" and doc == "S" and alcool == "N":
    if idade >= '16' or idade <= '69' and peso > 50:
        print("Voce esta legivel para ser doador, obrigado !")
    else:
        print("Voce não esta Legivel para ser um doador, mas obrigado pela atenção")
else:
    print("Voce não esta Legivel para ser um doador, mas obrigado pela atenção")

'''