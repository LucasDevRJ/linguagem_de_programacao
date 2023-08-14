#tipos de dados
print(type("olá"))
print(type(1))
print(type(1.5))

#métodos de String
print("olá".upper())

class Jogador:
    def jogar(self):
        print('Método jogar foi inicializado')


j1 = Jogador()
j1.jogar()

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e minha idade {self.idade} anos')

p1 = Pessoa('Lucas', 24)
p1.apresentar()

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cadastro):
        self.nome = nome
        self.idade = idade
        self.cadastro = cadastro

    def apresentar(self):
        print(f'Olá, sou o funcionário(a) {self.nome} e minha idade {self.idade} anos')

f1 = Funcionario('João', 32, 1001)
f1.apresentar()
print(f'cadastro do {f1.nome} é {f1.cadastro}')

class Cliente(Pessoa):
    quantidadeClientes = 0
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        Cliente.quantidadeClientes += 1
        self.cadastro = 1000 + Cliente.quantidadeClientes

    def apresentar(self):
        super().apresentar()
        print(f'Sou o cliente de cadastro {self.cadastro}')

c1 = Cliente('Carlos', 16)
c1.apresentar()

class Aluno:
    totalAlunos = 0
    def __init__(self, nome, nota):
        Aluno.totalAlunos += 1
        self.nome = nome
        self.nota = nota
        self.ru = 1000 + Aluno.totalAlunos

    def info(self):
        print(f'Nome: {self.nome}; RU: {self.ru}; Nota: {self.nota}')

    def getNota(self):
        return self.nota

l1 = Aluno('Fábio', 4.6)
l1.info()
print(l1.getNota())