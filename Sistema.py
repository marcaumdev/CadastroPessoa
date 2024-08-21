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
                opcaoPF = int(input("\n---Escolha uma opção---\n1 - Cadastrar Pessoa Física\n2 - Listar Pessoas Físicas\n3 - Remover Pessoa Física\n4 - Atualizar Pessoa Física\n0 - Retornar ao menu anterior\n> "))
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
                        print("Não há pessoas físicas cadastradas! ")
                elif opcaoPF == 3:
                    CPFExcluir = input("Digite o CPF da pessoa a ser excluída\n> ")
                    pessoaPfEncontradaExcluir = False
                    if listaPF:
                        for pessoaPF in listaPF:
                            if pessoaPF.CPF == CPFExcluir:
                                listaPF.remove(pessoaPF)
                                pessoaPfEncontradaExcluir = True
                                print(f"Pessoa com CPF {CPFExcluir} excluida com sucesso! ")
                    elif not pessoaPfEncontradaExcluir:
                        print("Cadastro não encontrado! ")
                    else:
                        print("Cadastro não encontrado! ")
                        input()
                elif opcaoPF == 4:
                    CPFAtualizar = input("Digite o CPF da pessoa a ser atualizada\n> ")
                    pessoaPfEncontradaAtualizar = False
                    if listaPF:
                        for pessoaPF in listaPF:
                            if pessoaPF.CPF == CPFAtualizar:
                                pessoaPfEncontradaAtualizar = True
                                novoEnderecoAtualizadoPF = Endereco()
                                while True:
                                    opcaoAtualizarPF = int(input("\n---Escolha uma opção---\n1 - Nome\n2 - Telefone\n3 - Rendimento\n4 - Data de Nascimento\n5 - Endereço\n0 - Retornar ao menu anterior\n> "))
                                    if opcaoAtualizarPF == 1:
                                        pessoaPF.nome = input("Digite o nome da pessoa física\n> ")
                                    elif opcaoAtualizarPF == 2:
                                        pessoaPF.telefone = input("Digite o Telefone\n> ")
                                    elif opcaoAtualizarPF == 3:
                                        pessoaPF.rendimento = float(input("Digite o rendimento\n> "))
                                    elif opcaoAtualizarPF == 4:
                                        dataNascimento = input("Digite a data de Nascimento (dd/MM/aaaa)\n> ")
                                        pessoaPF.dataNascimento = datetime.strptime(dataNascimento, '%d/%m/%Y').date()
                                        idade = (date.today() - pessoaPF.dataNascimento).days / 365
                                        if idade >= 18:
                                            print("A pessoa tem mais de 18 anos")
                                        else:
                                            print("A pessoa tem menos de 18 anos.\nRetornando ao menu anterior")
                                            continue
                                    elif opcaoAtualizarPF == 5:
                                        novoEnderecoAtualizadoPF.logradouro = input("Digite o logradouro\n> ")
                                        novoEnderecoAtualizadoPF.numero = input("Digite o número\n> ")
                                        novoEnderecoAtualizadoPF.CEP = input("Digite o CEP\n> ")
                                        endComercial = input("Este endereço é comercial? (S/N)\n> ")

                                        novoEnderecoAtualizadoPF.enderecoComercial = endComercial.strip().upper() == "S"

                                        pessoaPF.endereco = novoEnderecoAtualizadoPF
                                    elif opcaoAtualizarPF == 0:
                                        print("Voltando ao menu anterior...")
                                        break
                                    else:
                                        print("\nOpção inválida!")
                    elif not pessoaPfEncontradaAtualizar:
                        print("Cadastro não encontrado! ")
                    else:
                        print("Cadastro não encontrado! ")
                        input()
                elif opcaoPF == 0:
                    print("Voltando ao menu anterior...")
                    break
                else:
                    print("\nOpção inválida!")

        elif opcao == 2:
            while True:
                opcaoPJ = int(input("\n---Escolha uma opção---\n1 - Cadastrar Pessoa Jurídica\n2 - Listar Pessoas Jurídicas\n3 - Remover Pessoa Jurídica\n4 - Atualizar Pessoa Jurídica\n0 - Retornar ao menu anterior\n> "))
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
                        print("Não há pessoas jurídicas cadastradas! ")
                elif opcaoPJ == 3:
                    pessoaPjEncontradaExcluir = False
                    CNPJExcluir = input("Digite o CNPJ da pessoa a ser excluída\n> ")
                    if listaPJ:
                        for pessoaPJ in listaPJ:
                            if pessoaPJ.CNPJ == CNPJExcluir:
                                listaPJ.remove(pessoaPJ)
                                pessoaPjEncontradaExcluir = True
                                print(f"Pessoa com CNPJ {CNPJExcluir} excluida com sucesso! ")

                    elif not pessoaPjEncontradaExcluir:
                        print("Cadastro não encontrado! ")

                    else:
                        print("Cadastro não encontrado! ")
                        input()
                elif opcaoPJ == 4:
                    CNPJAtualizar = input("Digite o CNPJ da pessoa a ser atualizada\n> ")
                    pessoaPjEncontradaAtualizar = False
                    if listaPJ:
                        for pessoaPJ in listaPJ:
                            if pessoaPJ.CPF == CNPJAtualizar:
                                novoEnderecoAtualizadoPJ = Endereco()
                                pessoaPjEncontradaAtualizar = True
                                while True:
                                    opcaoAtualizarPJ = int(input("\n---Escolha uma opção---\n1 - Nome\n2 - rendimento\n3 - Razao Social\n4 - Telefone\n5 - Endereço\n0 - Retornar ao menu anterior\n> "))
                                    if opcaoAtualizarPJ == 1:
                                        pessoaPJ.nome = input("Digite o nome da pessoa jurídica\n> ")
                                    elif opcaoAtualizarPJ == 2:     
                                        pessoaPJ.rendimento = float(input("Digite o rendimento\n> "))
                                    elif opcaoAtualizarPJ == 3:
                                        pessoaPJ.razaoSocial = input("Digite a Razão Social\n> ")
                                    elif opcaoAtualizarPJ == 4:
                                        pessoaPJ.telefone = input("Digite o telefone\n> ")
                                    elif opcaoAtualizarPJ == 5:
                                        novoEnderecoAtualizadoPJ.logradouro = input("Digite o logradouro\n> ")
                                        novoEnderecoAtualizadoPJ.numero = input("Digite o número\n> ")
                                        novoEnderecoAtualizadoPJ.CEP = input("Digite o CEP\n> ")

                                        endComercial = input("Este endereço é comercial? (S/N)\n> ")

                                        novoEnderecoAtualizadoPJ.enderecoComercial = endComercial.strip().upper() == "S"

                                        pessoaPJ.endereco = novoEnderecoAtualizadoPJ
                                    elif opcaoAtualizarPJ == 0:
                                        print("Voltando ao menu anterior...")
                                        break
                                    else:
                                        print("Opção inválida!")
                                    print(f"Pessoa com CNPJ {CNPJAtualizar} atualizada com sucesso! ")
                    elif not pessoaPjEncontradaAtualizar:
                        print("Cadastro não encontrado! ")
                    else:
                        print("Cadastro não encontrado! ")
                        input()
                elif opcaoPJ == 0:
                    print("Voltando ao menu anterior...")
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