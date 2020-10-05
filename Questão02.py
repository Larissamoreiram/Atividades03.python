'''Elabore um programa para solicitar o nome de uma equipe de futebol, a
quantidade de derrotas, empates e vitórias obtidas por ela no campeonato.
Calcular e informar: a quantidade de pontos ganhos e a quantidade de pontos
perdidos.'''

time = str(input('Digite o nome do time: '))
vitorias = int(input('Digite o número de vitórias: '))
derrotas = int(input('Digite o número de derrotas: '))
empates = int(input('Digite o número de empates: '))
print('Pontos ganhos: ', (vitorias * 3 + empates))
print('Pontos perdidos: ', (derrotas * 3 % vitorias))
