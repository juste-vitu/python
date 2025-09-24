def apresentacao(nome, nomeMae, nomePai):
    print(f"Nome: {nome}")
    print(f"Nome da mãe: {nomeMae}")
    print(f"Nome do pai: {nomePai}")

nome = str(input("Digite seu nome completo: "))
nomeMae = str(input("Digite o nome completo da sua mae: "))
nomePai = str(input("Digite o nome completo de seu pai: "))

apresentacao(nome, nomeMae, nomePai)