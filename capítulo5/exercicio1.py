def validaLogin(nome, senha):
    if(nome == "Juste" and senha == "senha123"):
      return print("seja bem vindo", nome, senha)
    else:
        print("senha ou login invalidos")

print("=== digite seu nome: ===")
nome = input()
print("=== digite sua senha: ===")
senha = input()

validaLogin(nome, senha)