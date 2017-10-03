'''
Created on 7 de set de 2017

@author: luiz
'''
cTexto = input("Informe um texto: ").upper()

if cTexto.startswith("SPED"):
    print("seu texto é inicializado por SPED")
else:
    print("seu texto não é inicializado por SPED")

print("checa se o início da variável contém uma expressão: ", cTexto.startswith("SPED"))

print("-"*50)
cCodigo = "301"
print("Preenche com zeros a esquerda: ", cCodigo.zfill(10))

print("-"*50)

# no for a variável começa em zero
for numero in range(1,6):
    print(numero)