class Veiculo: #criando a classe Veiculo
    #construtor da classe Veiculo para instanciarmos os atributos ao criar o objeto
    def __init__(self, tipo, modelo, fabricante, quantidade_passageiros):
        #settando os atributos com valores passado por parâmetro
        self.tipo = tipo
        self.modelo = modelo
        self.fabricante = fabricante
        self.quantidade_passageiros = quantidade_passageiros

    #método para pegar o valor do tipo de Veículo
    def get_tipo(self):
        return f"{self.tipo}"

    # método para pegar o valor do modelo e fabricante do Veículo
    def get_modelo(self):
        return f"Fabricante: {self.fabricante} - Modelo: {self.modelo}"

    #método para pegar o número de passageiros que caibam no veículo
    def get_quantidade_passageiros(self):
        return f"{self.quantidade_passageiros}"

#criando um objeto Veiculo e armazenando na variável
veiculo_1 = Veiculo("Carro", "Ford Mustang", "Ford Motor Company", 4)

#exibindo respostas do código no console
print(veiculo_1.get_modelo())
print("é um ", veiculo_1.tipo, " que cabem ", veiculo_1.quantidade_passageiros, " passageiros")