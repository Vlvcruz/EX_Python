#Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.

#entrada de dado
Sal = float(input("Digite seu salario atual: \n"))

#processamento de dado
Sal_novo = (Sal * 0.6) + Sal

#saida de dados
print(f"O Salário de {Sal}, com o reajuste de 60% será de \n R$ {Sal_novo}")

