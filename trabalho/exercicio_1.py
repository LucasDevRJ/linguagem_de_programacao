import math
class Calculadora: #criação da classe Calculadora
    #atributos da Calculadora
    penultimo_numero_ru: int
    ultimo_numero_ru: int

    #método para retonar o penultimo valor da RU
    def get_penultimo_numero_ru(self):
        return f"{self.penultimo_numero_ru}"

    # método para retonar o último valor da RU
    def get_ultimo_numero_ru(self):
        return f"{self.ultimo_numero_ru}"

    #método para armazenar valores digitados pelo usuário
    def solicitaValores(self):
        #input que armazena o valor
        self.penultimo_numero_ru = int(input("Digite o penultimo número da sua RU: "))
        self.ultimo_numero_ru = int(input("Digite o último número da sua RU: "))

        #lógica para trocar 0 por 5
        if (self.penultimo_numero_ru == 0):
            calculadora.penultimo_numero_ru = 5
        elif (self.ultimo_numero_ru == 0):
            calculadora.ultimo_numero_ru = 5

    #método para somar o penultimo com o ultimo número da RU
    def soma(self):
        return self.penultimo_numero_ru + self.ultimo_numero_ru

    # método para subtrair o penultimo com o ultimo número da RU
    def subtrai(self):
        return self.penultimo_numero_ru - self.ultimo_numero_ru

    #método para multiplicar o penultimo com o ultimo número da RU
    def multiplica(self):
        return self.penultimo_numero_ru * self.ultimo_numero_ru

    # método para dividir o penultimo com o ultimo número da RU
    def dividi(self):
        return self.penultimo_numero_ru / self.ultimo_numero_ru

    # método para elevar o penultimo pelo ultimo número da RU
    def eleva(self):
        return self.penultimo_numero_ru ** self.ultimo_numero_ru

    # método para retornar o resto da divisão do penultimo com o ultimo número da RU
    def resto(self):
        return self.penultimo_numero_ru % self.ultimo_numero_ru

    # método para retornar o resto da divisão do penultimo com o ultimo número da RU
    def raiz_quadrada(self):
        return math.sqrt(self.penultimo_numero_ru + self.ultimo_numero_ru)

opcao = 0 #lógica para parar o loop
while (opcao != 8) :
    #menu do sistema
    print("-------------------|MENU|-------------------")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Elevar")
    print("6 - Resto")
    print("7 - Raiz Quadrada")
    print("8 - Sair")
    opcao = int(input("Digite a sua operação desejada: "))

    #condições para a opção escolhida
    if (opcao == 1):
        #instancia do objeto para poder acessar atributos e métodos dele
        calculadora = Calculadora()
        calculadora.solicitaValores()
        print(calculadora.get_penultimo_numero_ru(), "+", calculadora.get_ultimo_numero_ru(), "=", calculadora.soma())
    elif (opcao == 2):
        calculadora = Calculadora()
        calculadora.solicitaValores()
        print(calculadora.get_penultimo_numero_ru(), "-", calculadora.get_ultimo_numero_ru(), "=", calculadora.subtrai())
    elif (opcao == 3):
        calculadora = Calculadora()
        calculadora.solicitaValores()
        print(calculadora.get_penultimo_numero_ru(), "x", calculadora.get_ultimo_numero_ru(), "=", calculadora.multiplica())
    elif (opcao == 4):
        calculadora = Calculadora()
        calculadora.solicitaValores()
        print(calculadora.get_penultimo_numero_ru(), "/", calculadora.get_ultimo_numero_ru(), "=", calculadora.dividi())
    elif (opcao == 5):
        calculadora = Calculadora()
        calculadora.solicitaValores()
        print(calculadora.get_penultimo_numero_ru(), "^", calculadora.get_ultimo_numero_ru(), "=", calculadora.eleva())
    elif (opcao == 6):
        calculadora = Calculadora()
        calculadora.solicitaValores()
        print(calculadora.get_penultimo_numero_ru(), "%", calculadora.get_ultimo_numero_ru(), "=", calculadora.resto())
    elif (opcao == 7):
        calculadora = Calculadora()
        calculadora.solicitaValores()
        print("√", calculadora.get_penultimo_numero_ru(), "+", calculadora.get_ultimo_numero_ru(), "=", calculadora.raiz_quadrada())
    elif (opcao == 8):
        print("Programa finalizado.")
    else :
        print("Valor inválido!")
    print("--------------------------------------------")