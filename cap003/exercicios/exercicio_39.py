# Exercício 3.9
"""
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
Calcule o total em segundos.
"""
int_dias = int(input("Informe o número de dias: "))
int_horas = int(input("Informe o número de horas: "))
int_min = int(input("Informe o número de minutos: "))
int_seg = int(input("Informe o número de segundos: "))

converte_dias = int_dias * 24 * 60 * 60 
converte_horas = int_horas * 60 * 60
converte_min = int_min * 60

resultado_conversao = converte_dias + converte_horas + converte_dias + int_seg 

print(f"{resultado_conversao} segundos")
