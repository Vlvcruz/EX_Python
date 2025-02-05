#Escreva um programa que converta real para o Franco Congolês

#entrada de dados
valor_real = float(input("Digite o valor que deseja converter para Franco Congolês: \n"))

#processamento do valor
convert = valor_real * 495.75 #Soma para a conversão

#saide de dados
print(f"R$ {valor_real}, é que valem a {convert:.2f} Francos Congolês")
