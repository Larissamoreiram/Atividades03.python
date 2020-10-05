''' Faça um programa que leia dois números e mostre qual o maior dos dois. O programa deve informar caso sejam iguais. '''

a = int(input('primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
    print('O primeiro valor é maior')
    
    elif b > a:
    print('O segundo valor é maior')
    
elif b == a:
    print('Os dois valores são iguais')
