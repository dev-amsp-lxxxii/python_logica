# Exercício 3.12
"""
Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
"""

distancia = float(input("Qual a distância do percurso? "))
velocidade_media = float(input("Qual a velocidade média? "))

tempo = distancia / velocidade_media

print(f"Tempo de viagem será de {tempo}")
