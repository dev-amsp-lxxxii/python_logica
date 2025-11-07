# Exercício 3.5
"""
Calcule o resultado da expressão A > B and C or D, utilizando os valores da 
tabela a seguir: 
A-B-C-D
1-2-True-False
10-3-False-False
5-1-True-True
"""

ex1_a = 1; ex1_b = 2; ex1_c = True; ex1_d = False
ex2_a = 10; ex2_b = 3; ex2_c = False; ex2_d = False
ex3_a = 5; ex3_b = 1; ex3_c = True; ex3_d = True

print(ex1_a > ex1_b and ex1_c or ex1_d)
print(ex2_a > ex2_b and ex2_c or ex2_d)
print(ex3_a > ex3_b and ex3_c or ex3_d)
