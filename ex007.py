#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1+nota2)/2
print('A média entre {} e {} é igual a {}'.format(nota1,nota2,media))

#para arrendondar o valor
nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1+nota2)/2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1,nota2,media))
