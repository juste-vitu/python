def validaLogin(nome, senha):
    if(nome == "Juste" and senha == "1234"):
      return print("seja bem vindo")
    else:
        print("senha ou login invalidos")

print("digite seu nome: ")
nome = input()
print("digite sua senha: ")
senha = input()

validaLogin(nome, senha)