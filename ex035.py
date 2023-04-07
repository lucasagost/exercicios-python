#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = float(input('Informe o primeiro segmento: '))
r2 = float(input('Informe o segundo segmento: '))
r3 = float(input('Informe o terceiro segmento: '))
if r1 < r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR  triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
