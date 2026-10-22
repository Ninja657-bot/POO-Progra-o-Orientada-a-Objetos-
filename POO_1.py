import os
os.system("cls")

dados = {}

class Aluno:
    def __init__(self, nome, matricula, turma):
        self.nome = nome
        self.matricula = int(matricula)
        self.turma = turma
        self.nota = []
        
    def exibir_boletim(self):
        print(f"Nome do aluno: {self.nome}")
        print(f"Matricula: {self.matricula}")
        print(f"Turma: {self.turma}")
        if not self.nota:
            print("Alunos sem notas")
        for i, nota in enumerate (self.nota, start=1):
            print(f"Nota {i}ª unidade: {nota}")
        print(f"Média: {self.calcular_media():.2f}")
        print(f"Status do aluno: {self.verificar_aprovacao()}")
    
    def calcular_media(self):
        if len(self.nota) == 0:
            return 0
        
        return sum(self.nota) / len(self.nota)
    
    def verificar_aprovacao(self):
        dados = self.calcular_media()
        if dados >= 7:
            return "Aprovado"
        else:
            return "Reprovado"
    
    def mudança_de_turma(self):
        print(f"Aluno da turma {self.turma}")
        self.turma += 1
        print(f"Agora passa a ser da turma {self.turma}")
        
aluno1 = Aluno("Carlos", 101, "A")
aluno1.nota = [8, 6, 9]

aluno1.exibir_boletim()