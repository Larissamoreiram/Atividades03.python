''' Crie um programa que leia a altura de 10 pessoas. Ao final o programa deve informar o total de pessoas cadastradas, a quantidade de pessoas com altura inferior a 1,60 metros;
a quantidade de pessoas com altura entre 1,60 metros e 1,80 metros e a quantidade de pessoas com altura superior a 1,80 metros.'''

inferior = entre = superior = 0

for c in range(10):
    altura = float(input('altura: '))
    while altura > 0:
        if altura < 1.6:
            inferior += 1

        elif altura > 1.8:
            superior += 1

        else:
            entre += 1
        break

cadastros = superior + inferior + entre

print(f'Foram cadastradas {cadastros} pessoas.')
print(f'Pessoas com altura < 1,60 metros: {inferior}')
print(f'Pessoas com altura entre 1,60 e 1,80: {entre}')
print(f'Pessoas com altura superior a 1,80 metros: {superior}')
