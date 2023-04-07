#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Uma distância em metro: '))
km = m/1000
hm = m/100
dam = m/10
dm = m/0.1
cm = m/0.01
mm =m/0.001
print('{} km'.format(km))
print('{} hm'.format(hm))
print('{} dam'.format(dam))
print('{} dm'.format(dm))
print('{} cm'.format(cm))
print('{} mm'.format(mm))
