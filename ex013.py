#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salatual = float(input('Digite seu salário atual: R$'))
salnovo = salatual + (salatual * 15/100)
print('O valor do seu salário reajustado em 15% de aumento é R${:.2f}'.format(salnovo))
