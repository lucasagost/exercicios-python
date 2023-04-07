#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valorcasa = float(input('Valor da casa: R$'))
salcomprador = float(input('Salário do comprador: R$'))
anosfina = int(input('Quantos anos de financiamento?'))
parcelas = valorcasa/(anosfina * 12)
print('Para paga um casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valorcasa, anosfina, parcelas))
if parcelas > salcomprador * 0.3:
    print('Emprestimo NEGADO')
else:
    print('Emprestimo APROVADO')
