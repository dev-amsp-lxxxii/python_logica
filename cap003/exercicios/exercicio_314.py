# Exercício 3.14
"""
Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado
pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 km rodado.
"""

dias_aluguel = int(input("Quantos dias o carro foi alugado? "))
km_rados = int(input("Quanto quilometros rodados? "))

total_a_pagar = (dias_aluguel * 60) + (km_rados * 0.15)

print(f"Dias alugados: {dias_aluguel} e Km rodados: {km_rados}")
print(f"Total a ser pago -> R$ {total_a_pagar:5.2f}")
