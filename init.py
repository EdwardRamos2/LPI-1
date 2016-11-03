#!/usr/bin/env python3
#Autor: Edward Ramos
questao = ''
resposta1 = ''
resposta = ['1','2','3','4','5']
questao1 = resposta[0:1]
questao2 = resposta[1:2]
questao3 = resposta[2:3]

def questionario(questao = open('q2.txt')):
    for texto in questao:
        imprimir_questao = texto.strip()
        print(imprimir_questao)

def resposta_mult(resposta1,questao1):
    while True:
        resposta1 = input('> ')
        print(resposta1)
        if resposta1 in questao1[0:1]:
            print('(+) Reposta Correta!')
            break
        print('(-) Resposta Errada!')

questionario(questao = open('q2.txt'))
resposta_mult(resposta1,questao1)
questionario(questao = open('q3.txt'))   
resposta_mult(resposta1,questao2)
questionario(questao = open('q4.txt'))
resposta_mult(resposta1,questao3)


