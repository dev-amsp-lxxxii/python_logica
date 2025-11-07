# Exercício 3.6
"""
Escreva uma expressão que será utilizado para decidir se um aluno foi ou não aprovado.
Para ser aprovado, todas as médias do aluno devem ser maiores ou iguais a 7. Considere que o aluno
cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis:
matéria01, matéria02, matéria03.
"""

nome = "Adelmo Menezes"

materia01 = 6.0;  materia02 = 7.5; materia03 = 9.5

resultado = (materia01 + materia02 + materia03) / 3

print(f"O aluno {nome} está aprovado? {resultado >= 7.0} com média: {resultado:.2f}")
