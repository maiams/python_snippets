from pessoa import Pessoa


def check_cpf(cpf):
    result = False
    if cpf != '0':
        result = True

    return result


class PessoaFisica(Pessoa):
    cpf: str

    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)
        self.cpf = cpf

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        if check_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF invalido")

