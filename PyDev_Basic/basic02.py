'''
Created on 4 de set de 2017

@author: luiz
'''
cNome = input("Informe o primeiro nome: ")
cSobrenome = input("Informe o primeiro nome: ")
cIdade = input("Qual é sua idade? ")

if cIdade < '30':
    print("Sr(a)", cNome, cSobrenome," ainda não tem 30 anos.")
else:
    print("Sr(a)",cNome,cSobrenome,"já possui idade suficiente para prosseguir!")