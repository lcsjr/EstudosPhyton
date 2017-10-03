'''
Created on 8 de set de 2017

@author: luiz
'''
import os

#print(os.listdir("c:\lixo") ) # mostra o conteúdo de um diretório

cPathOld = os.getcwd() #guardo o path atual
os.chdir("C:\lixo") # set o novo path
print(os.getcwd())

cFileDirs = os.listdir(".") # armazena todos os arquivo e diretórios do path

for cFileDir in cFileDirs:
    # mostra o conteúdo de um diretório
    if os.path.isfile(cFileDir):    # verifica se é arquivo
        print("Arquivo:",cFileDir)
    elif os.path.isdir(cFileDir):   # verifica se é diretório
        print("Diretório:",cFileDir)
    else:
        print("Indefinido:",cFileDir)

print("-"*40)

cCria = input("Criar novo diretório? ").upper().strip() #Retorna em maiusculo e elimina espaços

if cCria == "S":
    cDir = input("Informe o Nome do novo Diretório: ").strip() #retorna eliminando espaços em branco
    if  os.path.isdir(cDir) :
        print("O diretório", cDir, "já existe em",os.getcwd())
    else:
        os.mkdir(cDir) # cria o diretório
        print("Diretório",cDir,"criado com sucesso.")

print("-"*40)

# verifico se determinado arquivo existe no diretório
cFile1 = "luizjr.txt"
if os.path.isfile(cFile1):
    print("Arquivo",cFile1,"existente no diretório atual.")
else:
    print("Arquivo",cFile1,"não existe no direótio atual.")

print("-"*40)
os.chdir(cPathOld) #retorna o path principal
print("Volta para o path anterior: ",os.getcwd())