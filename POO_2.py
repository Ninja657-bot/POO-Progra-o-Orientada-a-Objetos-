import os
os.system("cls")

class Funcionario:
    def __init__ (self, nome, cpf ,salario_base=1582.00):
        self.nome = nome
        self.cpf = cpf
        self.salario_base = salario_base
        self.funcao = "Auxiliar"
        
    def salario(self):
        return self.salario_base
    
    def exibir_info(self):
        print("Ficha do funcionario")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Função {self.funcao}")
        print(f"Salário: {self.salario():.2f}")
        
class Professor(Funcionario):
    def __init__(self,nome, cpf, salario_base=None):
        if salario_base is None:
            super().__init__(nome, cpf)
        else:
            super().__init__ (nome, cpf, salario_base)
            
        self.disciplinas = []
        self.funcao = "Professor"
        
    def salario(self):
        quantidade = len(self.disciplinas)
        aumento = quantidade * 10

        return super().salario() * (1 + aumento / 100)
    
class Coordenador(Funcionario):
    def __init__ (self, nome, cpf, salario_base=None):
        if salario_base is None:
            super().__init__(nome, cpf)
        else:
            super().__init__(nome, cpf, salario_base)
        self.funcao = "Coordenador"
        
    def salario(self):
        salario_com_atividade = super().salario() * 1.05
        salario_final_com_dsr = salario_com_atividade * (1 + 1/6)
        return salario_final_com_dsr
    
class Diretor(Funcionario):
    def __init__ (self, nome, cpf, salario_base=None):
        if salario_base is None:
            super().__init__(nome, cpf)
        else:
            super().__init__(nome, cpf, salario_base)
        self.funcao = "Diretor"
        
    def salario(self):
        super().salario()