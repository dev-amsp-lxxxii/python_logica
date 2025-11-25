# Exercício 4.1
"""
Analise o Programa 4.1. Rsponda o que acontece se o primeiro e o segundo
valor forem iguuais? Explique
"""

ex_a = int(input("Primeiro valor: "))
ex_b = int(input("Segundo valor: "))

if ex_a > ex_b:
    print("O primeiro valor é maior!")

if ex_b > ex_a:
    print("Osegundo valor é o maior!")

# Não acontece nada, pois não tem nenhuma opção para 
# imprimir quando os valores são iguais
