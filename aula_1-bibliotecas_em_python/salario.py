salario_base = 3000
salario_analista = 3500
salario_estagiario = 1500
salario_lider = 9000

#reajuste salarial
reajuste = 0.035

if salario_analista > salario_base:
    salario_analista *= reajuste
    print(f'Novo salário: R$ {salario_analista}')

if salario_estagiario > salario_base:
    salario_estagiario *= reajuste
    print(f'Novo salário: {salario_estagiario}')

if salario_lider > salario_base:
    salario_lider *= reajuste
    print(f'Novo salário: {salario_lider}')