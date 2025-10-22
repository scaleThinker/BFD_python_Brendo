#Produza uma classe Pessoa com 3 atributos.
#Produza 2 classes, Aluno e Professor.
#Elas devem ser filhas de Pessoa.
#Cada uma deve ter no mínimo 2 atributos adicionais e 3 métodos cada.

class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def atualizar_email(self):
        self.email = input("Insira novo email: ")

class Aluno(Pessoa):
    def __init__(self, nome, idade, email, serie, matricula, status="Ativo"):
        super().__init__(nome, idade, email)
        self.serie = serie
        self.matricula = matricula
        self.status = status

    def trancar_matricula(self):
        self.status = "Trancada"
    
    def modificar_matricula(self):
        self.matricula = int(input("Insira a nova matrícula: "))
    
    def exibir_informacoes(self):
        return f"Aluno: {self.nome}, {self.idade} anos, Status: {self.status}, Matrícula: {self.matricula}, Série: {self.serie}, Email: {self.email}"
    
    def verificar_status(self):
        return self.status == "Ativo"

class Professor(Pessoa):
    def __init__(self, nome, idade, email, salario: float, disciplina, turno):
        super().__init__(nome, idade, email)
        self.salario = salario
        self.disciplina = disciplina
        self.turno = turno
    
    def reajustar_salario(self):
        percentual = float(input("Insira o percentual de reajuste: "))
        self.salario *= (1 + percentual/100)
    
    def exibir_informacoes(self):
        return f"Professor: {self.nome}, {self.idade} anos, Disciplina: {self.disciplina}, Turno: {self.turno}, Salário: R${self.salario:.2f}, Email: {self.email}"
    
    def registrar_aprovacao(self):
        print(f"Professor {self.nome} registrou aprovação de aluno")
    
    def registrar_reprovacao(self):
        print(f"Professor {self.nome} registrou reprovação de aluno")
    
    def trocar_disciplina(self):
        self.disciplina = input("Insira a nova disciplina: ")

# Exemplos de teste com dados diferentes
aluno1 = Aluno(
    nome="Ana Beatriz Costa", 
    idade=16, 
    email="ana.beatriz@escola.edu", 
    serie="2º", 
    matricula=20230045,
    status="Ativo"
)

professor1 = Professor(
    nome="Roberto Mendes Silva", 
    idade=42, 
    email="roberto.mendes@escola.edu", 
    salario=6500.00, 
    disciplina="Matemática", 
    turno="Tarde"
)

# Testes das funcionalidades
print("=== Dados Iniciais ===")
print(aluno1.exibir_informacoes())
print(professor1.exibir_informacoes())

print("\n=== Operações com Aluno ===")
print(f"Status atual: {aluno1.verificar_status()}")
aluno1.trancar_matricula()
print(f"Novo status: {aluno1.status}")
aluno1.modificar_matricula()
print(f"Nova matrícula: {aluno1.matricula}")

print("\n=== Operações com Professor ===")
professor1.trocar_disciplina()
print(f"Nova disciplina: {professor1.disciplina}")
professor1.reajustar_salario()
print(f"Salário reajustado: R${professor1.salario:.2f}")
professor1.registrar_aprovacao()

print("\n=== Dados Atualizados ===")
print(aluno1.exibir_informacoes())
print(professor1.exibir_informacoes())

