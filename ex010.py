#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input("Quanto dinheiro você te na carteira? R$"))
dolar = real/5.14
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(real, dolar))
