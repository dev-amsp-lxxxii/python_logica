# Exercício 3.11
"""
Faça um programa que solicite o preço de uma mercadoria e o
percentual de desconto. Exiba o valor de desconto e o preço a pagar.
"""

valor_mercadoria = float(input("Informe o valor do produto: "))
percentual_desconto = float(input("Informe o percentual do desconto: "))

calcular_percentual = (percentual_desconto / 100) * valor_mercadoria
valor_final = valor_mercadoria - calcular_percentual

print(f"Valor do produto R$ {valor_mercadoria:5.2f}")
print(f"Valor a ser descontado R$ {calcular_percentual:5.2f}")
print(f"Valor final a ser pago R$ {valor_final:5.2f}")
