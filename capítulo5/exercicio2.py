def apresentacao(nome, NomeMae, NomePai):
    print(f"Nome: {nome}")
    print(f"Nome da mãe: {NomeMae}")
    print(f"Nome do pai: {NomePai}")

nome = str(input("Digite seu nome completo: "))
NomeMae = str(input("Digite o nome completo da sua mãe: "))
NomePai = str(input("Digite o nome completo do seu pai: "))

apresentacao(nome, NomeMae, NomePai)