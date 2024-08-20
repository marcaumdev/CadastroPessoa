# 1 - Pessoa Física / 2 - Pessoa jurídica / 0 - Sair
# 1 - Cadastrar Pessoa física / 2 - Listar Pessoa física / 0 - Sair
# 1 - Cadastrar Pessoa jurídica / 2 - Listar Pessoa jurídica / 0 - Sair

from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica, PessoaJuridica


def main():
    listaPF = []
    listaPJ = []

    while True:
        opcao = int(input("\n---Escolha uma opção---\n1 - Pessoa Física\n2 - Pessoas Jurídica\n0 - Sair\n> "))

        if opcao == 1:
            while True:
                opcaoPF = int(input("\n---Escolha uma opção---\n1 - Cadastrar Pessoa Física\n2 - Listar Pessoas Físicas\n0 - Retornar ao menu anterior\n> "))
                if opcaoPF == 1:
                    novaPF = PessoaFisica()
                    novoEnderecoPF = Endereco()

                    novaPF.nome = input("Digite o nome da pessoa física\n> ")
                    novaPF.CPF = input("Digite o CPF\n> ")
                    novaPF.telefone = input("Digite o Telefone\n> ")
                    novaPF.rendimento = float(input("Digite o rendimento\n> "))

                    dataNascimento = input("Digite a data de Nascimento (dd/MM/aaaa)\n> ")
                    novaPF.dataNascimento = datetime.strptime(dataNascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novaPF.dataNascimento).days / 365
                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos.\nRetornando ao menu anterior")
                        continue

                    novoEnderecoPF.logradouro = input("Digite o logradouro\n> ")
                    novoEnderecoPF.numero = input("Digite o número\n> ")
                    novoEnderecoPF.CEP = input("Digite o CEP\n> ")
                    endComercial = input("Este endereço é comercial? (S/N)\n> ")

                    novoEnderecoPF.enderecoComercial = endComercial.strip().upper() == "S"

                    novaPF.endereco = novoEnderecoPF

                    listaPF.append(novaPF)
                    print(f"Cadastro de {novaPF.nome} feito com sucesso!")

                elif opcaoPF == 2:
                    if listaPF:
                        for pessoaPF in listaPF:
                            print("---------------------------------")
                            print(f"Nome: {pessoaPF.nome}")
                            print(f"CPF: {pessoaPF.CPF}")
                            print(f"Telefone: {pessoaPF.telefone}")
                            print(f"Endereço: {pessoaPF.endereco.logradouro}, {pessoaPF.endereco.numero} - {pessoaPF.endereco.CEP}")
                            print(f"Data Nascimento: {pessoaPF.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto: {pessoaPF.calcularImposto(pessoaPF.rendimento)}")
                            print("Digite 0 pra sair")
                            input()
                    else:
                        print("Não há pessoa físicas cadastradas! ")
                elif opcaoPF == 0:
                    print("Voltando ao menu anterior...")
                    break
                else:
                    print("\nOpção inválida!")

        elif opcao == 2:
            while True:
                opcaoPJ = int(input("\n---Escolha uma opção---\n1 - Cadastrar Pessoa Jurídica\n2 - Listar Pessoas Jurídicas\n0 - Retornar ao menu anterior\n> "))
                if opcaoPJ == 1:
                    novaPJ = PessoaJuridica()
                    novoEnderecoPJ = Endereco()

                    novaPJ.nome = input("Digite o nome da pessoa jurídica\n> ")
                    novaPJ.CNPJ = input("Digite o CNPJ\n> ")
                    novaPJ.rendimento = float(input("Digite o rendimento\n> "))
                    novaPJ.razaoSocial = input("Digite a Razão Social\n> ")
                    novaPJ.telefone = input("Digite o telefone\n> ")

                    novoEnderecoPJ.logradouro = input("Digite o logradouro\n> ")
                    novoEnderecoPJ.numero = input("Digite o número\n> ")
                    novoEnderecoPJ.CEP = input("Digite o CEP\n> ")

                    endComercial = input("Este endereço é comercial? (S/N)\n> ")

                    novoEnderecoPJ.enderecoComercial = endComercial.strip().upper() == "S"

                    novaPJ.endereco = novoEnderecoPJ

                    listaPJ.append(novaPJ)
                    print(f"Cadastro de {novaPJ.nome} feito com sucesso!\n")

                elif opcaoPJ == 2:
                    if listaPJ:
                        for pessoaPJ in listaPJ:
                            print("---------------------------------")
                            print(f"Nome: {pessoaPJ.nome}")
                            print(f"Razão Sozial: {pessoaPJ.razaoSocial}")
                            print(f"CNPJ: {pessoaPJ.CNPJ}")
                            print(f"Telefone: {pessoaPJ.telefone}")
                            print(f"Endereço: {pessoaPJ.endereco.logradouro}, {pessoaPJ.endereco.numero} - {pessoaPJ.endereco.CEP}")
                            print(f"Imposto: {pessoaPJ.calcularImposto(pessoaPJ.rendimento)}")
                            print("Digite 0 pra sair")
                            input()
                    else:
                        print("Não há pessoa jurídicas cadastradas! ")

                elif opcaoPJ == 0:
                    print("Voltando ao menu anterior...\n")
                    break

                else:
                    print("\nOpção inválida!")
        elif opcao == 0:
            print("\nObrigado por utilizar o nosso sistema!")
            break
        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    main()