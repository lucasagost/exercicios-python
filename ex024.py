#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cid = str(input('Em que cidade você nasceu?: ')).strip()  #geralmente elimina os espaços sempre
print(cid[:5].upper() == 'SANTO')   #vai jogar tudo para maisculo caso o usuario escreva errado e manda a mensagem correta

