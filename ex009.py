#Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
m1 = n*1
m2 = n*2
m3 = n*3
m4 = n*4
m5 = n*5
m6 = n*6
m7 = n*7
m8 = n*8
m9 = n*9
m10 = n*10
print('{} x 1 = {}'.format(n, m1))
print('{} x 2 = {}'.format(n, m2))
print('{} x 3 = {}'.format(n, m3))
print('{} x 4 = {}'.format(n, m4))
print('{} x 5 = {}'.format(n, m5))
print('{} x 6 = {}'.format(n, m6))
print('{} x 7 = {}'.format(n, m7))
print('{} x 8 = {}'.format(n, m8))
print('{} x 9 = {}'.format(n, m9))
print('{} x 10 = {}'.format(n, m10))
print('-'*12)

#outra maneira (para não salvar a varivavel)
num = int(input('Digite um número para ver sua tabuada: '))
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))