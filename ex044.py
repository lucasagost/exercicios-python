'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' LOJAS GUANABARA '))
valor = float(input('Preço das Compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
formas = int(input('Qual é opção? '))
if formas == 1:
    total = valor - (valor * 0.10)
    #print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, total))
    #print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, valor - (valor * 10/100)))

elif formas == 2:
    total = valor - (valor * 0.05)

elif formas == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}'.format(parcela))

elif formas == 4:
    total = valor + (valor * 0.20)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = valor
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
    
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, total)) #coloca mais perto da barra para sempre mostrar

