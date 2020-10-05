"""
Faça um programa para solicitar o nome e as duas notas e um aluno.
Calcular sua média e informá-la.
Se ela for inferior a 7, escrever "Reprovado”; caso contrário escrever "Aprovado".
"""

nome = input('Digite o nome do(a) aluno(a): ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media >= 7:
    print(f'{nome} obteve média de {media:.2f} pontos! APROVADO(A)!')

if media < 7:
    print(f'{nome} obteve média de {media:.2f} pontos! Infelizmente está REPROVADO(A)!')
