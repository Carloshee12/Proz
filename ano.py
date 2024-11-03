def obter_nome():
    nome = input("Digite seu nome completo: ")
    return nome

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Erro: O ano deve estar entre 1922 e 2021. Tente novamente.")
        except ValueError:
            print("Erro: Digite um número válido. Tente novamente.")

def calcular_idade(ano_nascimento, ano_atual=2024):
    return ano_atual - ano_nascimento

def main():
    nome = obter_nome()
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)
    print(f"{nome}, você completou ou completará {idade} anos em 2022.")

main()
