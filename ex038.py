'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
if num1 == num2:
    print('Não existem valor maior, os dois são iguais!')
elif num1 > num2:
    print('O primeiro valor é maior')
else:
    print('O segundo valor é maior')