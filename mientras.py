
#Importar librerias son codigos ya hechos o prefabricados

import math
from optparse import Option

from pip import main


#Declaracion el bucle/ciclo/ intecaccion/repeticion/ la vuelta/ loop

print("Arepas de chocolo Ya")
print("***************")
print("0. Digite un 0 para salir")
print("1. Digite 1 para calcular la raiz cuadrada de un #")
print("2. Digite 2 para calcular la posicion 2 de un #")
print("********")


opcion=1

while(opcion!=20):

    #Variable controladora
    opcion=int(input("Digite una opcion: "))
    #Pregunte por la obcion 
    if(opcion==0):
        break
    elif(opcion==1):
        numero=int(input("Digita un numero: "))
        raiz=math.sqrt(numero)
        print(f"La raiz de {numero} es {raiz}")
    elif(opcion==2):
        numero=int(input("Digita un numero: "))
        potencia=math.pow(numero,2)
        print(f"La ptencia de numeroes {potencia}")
    else:
        print("Digita una operación valida")