'''
Created on 8 de set de 2017

@author: luiz
'''
from datetime import date
from datetime import datetime

Data = date.today()
dia = Data.day
mes = Data.month
ano = Data.year

print("Data: ",Data )#, "----> Tipo de dados: " ,type(Data) )
print("Dia:  ",dia  )#, "----> Tipo de dados: " ,type(dia)   )
print("Mes:  ",mes  )#, "----> Tipo de dados: " ,type(mes)   )
print("Ano:  ",ano  )#, "----> Tipo de dados: " ,type(ano)   )

Horario = datetime.now()
hora     = Horario.hour
minuto   = Horario.minute
segundos = Horario.second
print (hora, "Horas", minuto,"minutos e",segundos ,"segundos.")

horariofinal = str(hora).zfill(2)+":"+str(minuto).zfill(2)+":"+str(segundos).zfill(2)
print("Hora Atual: ", horariofinal)
