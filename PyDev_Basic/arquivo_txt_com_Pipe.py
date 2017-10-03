'''
Created on 8 de set de 2017

@author: luiz
'''
#lendo arquivo txt separando variaveis por Pipe
arquivo = open('phyton_nomes.txt', 'r') #r=ler, w=escrever
for linha in arquivo.readlines():
    #print(linha)
    cNomes = linha.split("|")
    
    if cNomes[0] == "01":
        print("Nome do Pai:   ", cNomes[1] )
        print("Nome do Mãe:   ", cNomes[2] )
        print("Nome do Filho: ", cNomes[3] )
        print("Nome do Cão:   ", cNomes[4] )

    if cNomes[0] == "02":
        print("Mãe do Luiz:    ", cNomes[1] )
        print("Mãe do Cinthia: ", cNomes[2] )
   
    if cNomes[0] == "03":
        print("Primos do Davi: ", cNomes[1], cNomes[2], cNomes[3], cNomes[4] )

arquivo.close()
