#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#entrada de dado
nmr = float(input("Digite um numero: \n"))

#processamento de dado
dobro = nmr * 2
triplo = nmr * 3
raiz = nmr ** 0.5

#saide de dado
print(f"numero escolhido foi: {nmr} \nDobro: {dobro} \n"
      f"Triplo: {triplo} \n "
      f"Raiz Quadrada: {raiz}")

'''
#segunda saide de dado ( alternativa )
print(f"numero escolhido foi: {nmr} \nDobro: {nmr * 2} \n"
      f"Triplo: {nmr * 3} \n "
      f"Raiz Quadrada: {nmr ** (0.5)}")
'''