
#Estaciones del año

#Caminos para calsificarl el año

estacion = input ("Digite la estacion del año: ").lower()

if(estacion == "septiembre: " or "octubre: " or estacion == "noviembre: "):
    print("Es Otoño")

elif(estacion == "diciembre: " or estacion == "febrero" or estacion == "marzo"):
    print("Es Invierno")

elif(estacion == "Abril" or estacion == "mayo"):
    print("Es primavera")

elif(estacion == "junio" or estacion == "julio" or estacion == "agosto"):
    print("Es Verano")

else:
    print("Mes ingresado no corresponde: ")

