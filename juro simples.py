# Juro Simples

#Apresentação
print('\n\t\t\t -- Juro Simples --\n')

# Nesta Calculadora você irá fazer o calculo de juros simples usando a formula J: C.I.N/Percentual

# Entradas
n1 = int(input('informe Capital: '))
n2 = int(input('informe Taxa: '))
n3 = int(input('informe Prazo: '))
n4 = int(input('informe Percentual: '))

# Processamento
JUROS = n1*n2*n3/n4

#Saida
print(f'{n1} * {n2} * {n3} / {n4} = {JUROS}')