#Escreva um programa que peça ao usuário uma senha e verifique se ela está correta (a senha correta é "python123").

senha = input("Digite a senha para Acessar o Desktop: \n").strip()

if senha == 'python123':
    print("Senha Correta, seja bem vindo magnata")
else:
    print("Senha incorreta ! Tente novamente em 2horas")