import math


class Calculadora:
    penultimo_numero_ru: int
    ultimo_numero_ru: int

    def get_penultimo_numero_ru(self):
        return f"{self.penultimo_numero_ru}"

    def get_ultimo_numero_ru(self):
        return f"{self.ultimo_numero_ru}"

    def solicitaValores(self):
        self.penultimo_numero_ru = int(input("Digite o penultimo número da sua RU: "))
        self.ultimo_numero_ru = int(input("Digite o último número da sua RU: "))

        if (self.penultimo_numero_ru == 0):
            calculadora.penultimo_numero_ru = 5
        elif (self.ultimo_numero_ru == 0):
            calculadora.ultimo_numero_ru = 5

    def soma(self):
        return self.penultimo_numero_ru + self.ultimo_numero_ru

    def multiplica(self):
        return self.penultimo_numero_ru * self.ultimo_numero_ru

    def dividi(self):
        return self.penultimo_numero_ru / self.ultimo_numero_ru

    def eleva(self):
        return self.penultimo_numero_ru ** self.ultimo_numero_ru

    def resto(self):
        return self.penultimo_numero_ru % self.ultimo_numero_ru

    def raiz_quadrada(self):
        return math.sqrt(self.penultimo_numero_ru + self.ultimo_numero_ru)

opcao = 0
while (opcao != 8) :
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

    if (opcao != 8):
        calculadora = Calculadora()
        calculadora.solicitaValores()

    if (opcao == 1):
        print(calculadora.get_penultimo_numero_ru(), "+", calculadora.get_ultimo_numero_ru(), "=", calculadora.soma())
    elif (opcao == 2):
        print(calculadora.get_penultimo_numero_ru(), "-", calculadora.get_ultimo_numero_ru(), "=", calculadora.subtrai())
    elif (opcao == 3):
        print(calculadora.get_penultimo_numero_ru(), "x", calculadora.get_ultimo_numero_ru(), "=", calculadora.multiplica())
    elif (opcao == 4):
        print(calculadora.get_penultimo_numero_ru(), "/", calculadora.get_ultimo_numero_ru(), "=", calculadora.dividi())
    elif (opcao == 5):
        print(calculadora.get_penultimo_numero_ru(), "^", calculadora.get_ultimo_numero_ru(), "=", calculadora.eleva())
    elif (opcao == 6):
        print(calculadora.get_penultimo_numero_ru(), "%", calculadora.get_ultimo_numero_ru(), "=", calculadora.resto())
    elif (opcao == 7):
        print("√", calculadora.get_penultimo_numero_ru(), "+", calculadora.get_ultimo_numero_ru(), "=", calculadora.raiz_quadrada())
    elif (opcao == 8):
        print("Programa finalizado.")
    print("--------------------------------------------")