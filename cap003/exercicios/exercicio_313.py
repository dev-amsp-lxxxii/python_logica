# Exercício 3.13
"""
Escreva um programa que converte uma temperatura digitada em 'C em F'.
A fórmula para essa conversão é: 
"""

celsus = int(input("Informe a temperatura em celsius: "))

f = ((9 * celsus) / 5) + 32

print(f"Celsius -> {celsus}°C")
print(f"{celsus}°C para {int(f)}°F")
