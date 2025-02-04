'''
print("Aula do guanabara")

print(f'meu onibus passa as {horario} horas') #concatenação entre variavel e print

nome = 'Vitor'
idade = 20

print(f"Seu nome é: {nome}... E sua idade é: {idade}")


sobrename = input(f"Digite seu sobrenome: ")

print(f'seu nome completo é: {nome} {sobrename}')
'''

#tipos de dados

Lanche = int(input("Digite quantos lanches foram comprados: "))
Suco = int(input("Digite a quantidade de sucos tomados: "))

T_Lache = int(input("Qual valor pago no lanche ? "))
T_suco = int(input("Qual valor pago no Suco ?  "))

soma_total = Lanche * T_Lache + Suco * T_suco

print(f"O valor total pago foi R$: {soma_total}")

