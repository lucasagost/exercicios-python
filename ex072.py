'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

Aula Anterior'''

cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'catorze', 'quinze','dezesseis', 'dezessete', 'dezoite',
        'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <=20:
            break
        print('Tente novamente.', end=' ')
    print(f'Você digitou o número {cont[num]}')
    print('')
    resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
print('-'*40)
print('PROGRAMA ENCERRADO')


