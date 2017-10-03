'''
Created on 7 de set de 2017

@author: luiz
'''
#criação de arquivo txt
arquivo = open("curso_phyton.txt","w")  #r=ler, w=escrever
arquivo.write("Curso Phyton\n\n")
arquivo.write("Controle de variáveis\n")
arquivo.write("Manipulação de Dados\n")
arquivo.write("Lógica de Programação\n")
arquivo.close()

#lendo arquivo txt
arquivo = open('curso_phyton.txt', 'r') #r=ler, w=escrever
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

print("Luiz\nSantos\nJunior")