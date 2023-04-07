#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co1 = float(input('Comprimento do cateto oposto: '))
ca2 = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(co1, ca2)
print('A hipotenusa vai medir {:.2f}'.format(hip))
#FORMULA DA PROPIO MODULO
print('------------------------------------------------------')

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))


