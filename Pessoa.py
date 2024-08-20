from datetime import date

# CLASSE ENDERECO
class Endereco:
    def __init__(self, logradouro = "", numero = "", CEP = "", enderecoComercial = False):
        self.logradouro = logradouro
        self.numero = numero
        self.CEP = CEP
        self.enderecoComercial = enderecoComercial

# CLASSE PESSOA
class Pessoa:
    def __init__(self, nome = "", endereco = None, rendimento = 0.0, telefone = ""):
        self.nome = nome
        self.endereco = endereco
        self.rendimento = rendimento
        self.telefone = telefone

    def calcularImposto(self, rendimento):
        pass

# CLASSE PESSOA FÍSICA
class PessoaFisica(Pessoa):
    def __init__(self, nome = "", rendimento = 0.0, endereco = None, telefone = "", CPF = "", rg = "", dataNascimento = None):

        if endereco is None:
            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()

        super().__init__(nome, rendimento, endereco, telefone)

        self.CPF = CPF
        self.rg = rg
        self.dataNascimento = dataNascimento
    
    def calcularImposto(self, rendimento: float) -> float:
        if rendimento <= 1500:
            return 0
        elif 1500 < rendimento <= 3500:
            return rendimento * 0.02
        elif 3500 < rendimento <= 6000:
            return rendimento * 0.035
        else:
            return rendimento * 0.05

# CLASSE PESSOA JURÍDICA
class PessoaJuridica(Pessoa):
    def __init__(self, nome = "", rendimento = 0.0, endereco = None, telefone = "", CNPJ = "", razaoSocial = ""):

        if endereco is None:
            endereco = Endereco()

        super().__init__(nome, rendimento, endereco, telefone)

        self.CNPJ = CNPJ
        self.razaoSocial = razaoSocial

    def calcularImposto(self, rendimento: float) -> float:
        if rendimento <= 1500:
            return rendimento * 0.02
        elif 1500 < rendimento <= 3500:
            return rendimento * 0.035
        elif 3500 < rendimento <= 6000:
            return rendimento * 0.05
        else:
            return rendimento * 0.08

        