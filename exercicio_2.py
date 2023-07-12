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

print("-------------------|MENU|-------------------")
print("1 - Soma")
opcao = int(input("Digite a sua operação desejada: "))

if opcao == 1:
    calculadora = Calculadora()
    calculadora.solicitaValores()
    print(calculadora.get_penultimo_numero_ru(), "+", calculadora.get_ultimo_numero_ru(), "=", calculadora.soma())
