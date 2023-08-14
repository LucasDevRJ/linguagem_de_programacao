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
    pass

f1 = Funcionario('João', 32)
f1.apresentar()