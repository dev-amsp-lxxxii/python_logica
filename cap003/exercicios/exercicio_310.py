# Exercício 3.10
"""
Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
"""

valor_salario = float(input("Informe o salário atual: "))
porcentagem_aumento = float(input("Informe o aumento em %: "))

calculo_porcentagem = (porcentagem_aumento / 100) * valor_salario
salario_atualizado = calculo_porcentagem + valor_salario

print(f"O salário defasado para: R$ {valor_salario:5.2f}")
print(f"Valor do aumento é R$ {calculo_porcentagem:5.2f}")
print(f"O salário atualizado para: R$ {salario_atualizado:5.2f}")
