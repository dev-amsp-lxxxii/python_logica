# Exercício 3.15
"""
Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 min de vida a cada cigarro, e calcule quantos dias
de vida um fumante perderá.
Exiba o total em dias.
"""

cigarros_diarios = int(input("Quantos cigarros por dia: "))
anos_fumando = int(input("Quantos anos fumou: "))

qtd_cigarros = (anos_fumando * 365) * cigarros_diarios
tempo_min = qtd_cigarros * 10
dias_vida_perdida = float(tempo_min / 60 / 24)

print(f"dias perdidos de sua vida: {dias_vida_perdida:5.2f}")
