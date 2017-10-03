'''
Created on 7 de set de 2017

@author: luiz
'''
cNome = input("Digite seu Nome: ")
cSobrenome = input("Digite seu Sobrenome: ")
nIdade = int(input("Digite sua idade: "))

cNomeCompleto =  cNome+" "+cSobrenome

print("Nome Completo: ",cNomeCompleto)
print("Repetição:", "0"*20)
print("Esquivalente a Substring: ", cNomeCompleto[0:4])
print(cNome, ", você tem",nIdade,"anos.")
print("Retorna a posição de uma string (Uso do UPPER com FIND): ",cNome.upper().find("Z"))

cTeste =""
print("Verifica se cTeste tem espaço: ", cTeste.isspace())
cTeste =" "
print("Verifica se cTeste tem espaço: ", cTeste.isspace())
cTeste =" "
print("Verifica se cTeste tem espaço: ", cTeste.strip().isspace())
cTeste = "    davi luiz gomes     "
print("elimina espaços em branco a esquerda e direita: ",cTeste.strip(),".")

print( "Alinhamento a esquerda com espaçamento", cNome.ljust(15), "|",cSobrenome.ljust(20),"|")
print( "Alinhamento a direita  com espaçamento", cNome.rjust(15), "|",cSobrenome.rjust(20),"|")

cNomes = "luiz davi cinthia hilda cariza lauza sueli helcio gislene felipe"
cNomes = cNomes.split()
print("Criando Lista por espaçamento:", cNomes )

cNomes = "luiz;davi;cinthia;hilda;cariza;lauza;sueli;helcio;gislene;felipe"
cNomes = cNomes.split(";")
print("Criando Lista por ';' (ponto e virgula) :", cNomes )