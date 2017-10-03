'''
Created on 7 de set de 2017

@author: luiz
'''
cString = ""
cString += "010|NOTAFISCAL:000001\n"

nItem = 1
while nItem <= 4:
    cString += "020|item:"+str(nItem)+'\n'
    nItem += 1
    
#criação de arquivo txt
arquivo = open("phyton_nota_e_Itens.txt","w")  #r=ler, w=escrever
arquivo.write(cString)
arquivo.close()

#lendo arquivo txt
arquivo = open('phyton_nota_e_Itens.txt', 'r') #r=ler, w=escrever
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
