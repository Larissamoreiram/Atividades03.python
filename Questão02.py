'''
Elabore um programa para solicitar o nome de uma equipe de futebol,
a quantidade de derrotas, empates e vitórias obtidas por ela no campeonato.
No futebol, cada vitória vale três pontos e cada empate vale um ponto.
Calcular e informar: a quantidade de pontos ganhos,
a quantidade de pontos perdidos e o percentual de aproveitamento da equipe
'''

time = str(input('Digite o nome do time: '))
vitorias = int(input('Digite o número de vitórias: '))
derrotas = int(input('Digite o número de derrotas: '))
empates = int(input('Digite o número de empates: '))

pts_ganhos = vitorias * 3 + empates
pts_perdidos = derrotas * 3 + empates * 2
total_pts = pts_ganhos + pts_perdidos
aproveitamento = (pts_ganhos/total_pts) * 100

print(f'{time}:')
print(f'Pontos ganhos: {pts_ganhos}')
print(f'Pontos perdidos: {pts_perdidos}')
print(f'Aproveitamento de {aproveitamento:.2f}%')
