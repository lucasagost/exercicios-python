#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input("Digite sua temperatura em graus Celsius: "))
fahrenh = ((celsius*9/5)+32)
print("Sua temperatura em Fahrenheit é: {:.2f}°F!".format(fahrenh))
