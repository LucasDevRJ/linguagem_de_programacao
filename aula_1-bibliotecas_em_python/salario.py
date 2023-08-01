salario_base = 3000
salario_analista = 3500
salario_estagiario = 1500
salario_lider = 9000

#reajuste salarial
reajuste = 0.035

def reajustar_salario(salario, valor_base, valor_reajuste):
    if salario > salario_base:
        salario *= valor_reajuste
        print(f'Novo salário: R$ {salario}')
    return salario

salario_analista = reajustar_salario(salario_analista, salario_base, reajuste)
salario_estagiario = reajustar_salario(salario_estagiario, salario_base, reajuste)
salario_lider = reajustar_salario(salario_lider, salario_base, reajuste)