#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = float(input('Digite o valor do produto: R$'))
descont = preco*0.05
valorfinal = preco-descont
print('O produto que custava R${:.2f}, na promoção de 5% vai custar R${:.2f}.'.format(preco, valorfinal))

#forma do curso
pre = float(input('Digite o valor do produto: R$'))
novo = pre - (pre * 5 / 100)
print('O produto que custava R${:.2f}, na promoção e 5% vai custar R${:.2f}'.format(pre, novo))
