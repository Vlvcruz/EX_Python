#Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.
import random

#entrada de dados
jo = int(input("Faça sua escolha: \n1- Pedra\n2- Papel\n3- Tesoura\n"))

#escolha do computador
pc = random.randint(1,3)

#processamento
if jo == pc:
    print('\nEmpate!')
elif jo == 1 and pc == 2 or jo == 2 and pc == 3 or jo == 3 and pc == 1:
    print('\nComputador ganha!')
elif jo == 1 and pc == 3 or jo == 2 and pc == 1 or jo == 3 and pc == 2:
    print('\nJogador ganha!')
else:
    print('\nApenas numeros entre 1 a 3 !!')
