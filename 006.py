#Escreva um programa que leia 6 notas diferentes e faça a média do aluno

#entradas de dados
nt1 = float(input("Digite a primeira nota do Aluno: \n"))
nt2 = float(input("Digite a segunda nota do Aluno: \n"))
nt3 = float(input("Digite a terceira nota do Aluno: \n"))
nt4 = float(input("Digite a quarta nota do Aluno: \n"))
nt5 = float(input("Digite a quinta nota do Aluno: \n"))
nt6 = float(input("Digite a sexta nota do Aluno: \n"))

#processamento da media
media = (nt1 + nt2 + nt3 + nt4 + nt5 + nt6)/6

#saida de dados
print(f"A sua média final é: {media:.2f}")
