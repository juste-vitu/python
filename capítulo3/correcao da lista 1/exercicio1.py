def adicao(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2
# main
n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))

ResultadoAdicao = adicao(n1, n2)
ResultadoSubtracao = subtracao(n1, n2)
ResultadoMultiplicacao = multiplicacao(n1, n2)
ResultadoDivisao = divisao(n1, n2)

print("Adição", ResultadoAdicao)
print("Subtração", ResultadoSubtracao)
print("Multiplicação", ResultadoMultiplicacao)
print("Divisão", ResultadoDivisao)