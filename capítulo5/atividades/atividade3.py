def soma(n1, n2):
    return print(f"O valor da soma dos números é: ", n1+n2)

def subtracao(n1, n2):
    return print(f"O valor da subtração dos números é: ", n1-n2)

def divisao(n1, n2):
    return print(f"O valor da divisão dos números é: ", n1/n2)

def multiplicacao(n1, n2):
    return print(f"O valor da multiplicação dos números é: ", n1*n2)


n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

soma(n1, n2)
subtracao(n1, n2)
divisao(n1, n2)
multiplicacao(n1, n2)