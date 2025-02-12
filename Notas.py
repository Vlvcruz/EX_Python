'''
print("Aula do guanabara")

print(f'meu onibus passa as {horario} horas') #concatenação entre variavel e print

nome = 'Vitor'
idade = 20

print(f"Seu nome é: {nome}... E sua idade é: {idade}")


sobrename = input(f"Digite seu sobrenome: ")

print(f'seu nome completo é: {nome} {sobrename}')



#tipos de dados

Lanche = int(input("Digite quantos lanches foram comprados: "))
Suco = int(input("Digite a quantidade de sucos tomados: "))

T_Lache = int(input("Qual valor pago no lanche ? "))
T_suco = int(input("Qual valor pago no Suco ?  "))

soma_total = Lanche * T_Lache + Suco * T_suco

print(f"O valor total pago foi R$: {soma_total}")

#Strings

nome = 'vitor leon'

#fatiamento
print(nome[0])#pega a primeira caracter
print(nome[1:5])#pega as caracter entre 1 a 5 continuo
print(nome[1:5:2])#pega as caracter entre 1 a 5 continuo, pulando de 2 em 2

#Analise
print(len(nome))#conta todas caracter
print(nome.count('l')) #Retorna a contagem de l no texto
print(nome.find('l')) #Retorna a posição da primeira letra l

#transformação
nome = input('nome: ').strip() #Recebe o dado inserido pelo usuario e tira os espaços

print(nome.upper())#Deixa todas caracter em maiusculo
print(nome.lower())#deixa todas caracter em minusculo
print(nome.replace('L', 'P'))#Faz a troca das caracter L para P

import time

contador = 0

while contador < 100:
    time.sleep(0.5)
    print(contador)
    contador += 1

#Laco de repetição

'''

opcao = 0

while opcao != 5:
    opcao = int(input("Digite o que deseja fazer: \n"
                      "1. mostrar nome \n"
                      "2. somar \n"
                      "5. sair"))

    if opcao == 1:
        nome = input("seu nome")
        print(f"Seu nome é {nome}")

