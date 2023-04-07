''' Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
from  time import sleep
print('-'*20)
print('CALCULADORA DOIDA')
print('-'*20)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICA
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>>> Qual é a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma é {}.'.format(soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto é {}.'.format(produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor é {}'.format(maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!')