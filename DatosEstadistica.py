##En este archivo calcularemos las cifras de donde haremos las graficas

##Primero clasificaremos los productos de acuerdo a su marca
import matplotlib.pyplot as plt

LEGO = ["muneco","vehiculo"]
Apache = ["triciclo"]
DISNEYCOLLECTION = ["munecas","elsa","figuras","rayo"]
CILEK = ["camacoche"]
TOYSTORY = ["buz"]
LOL = ["casa"]

archivo = open("Carritos.txt","r")
archivoA = open("DatosEstadistica.txt","w")
lego = 0 
apache = 0
disney = 0
cilek = 0
toy = 0
lol = 0
for linea in archivo: 
  datos = linea.split (",")
  for i in range(len(datos)):
    if datos[i]=="muneco":
      lego = lego + 1
    elif datos[i]=="vehiculo":
      lego = lego + 1
    elif datos[i]=="triciclo":
      apache = apache + 1
    elif datos[i]=="munecas":
      disney = disney + 1
    elif datos[i]=="elsa":
      disney = disney + 1
    elif datos[i]=="figuras":
      disney = disney + 1
    elif datos[i]=="rayo":
      disney = disney + 1
    elif datos[i]=="camacoche":
      cilek = cilek + 1
    elif datos[i]=="buz":
      toy = toy + 1
    elif datos[i]=="casa":
      lol = lol + 1
archivoA.write ("La marca LEGO vendio un total de piezas: " + str(lego) +"\nLa marca Apache vendio un total de piezas: " + str(apache) + "\nLa marca DISNEYCOLLECTION vendio un total de piezas: " + str(disney) + "\nLa marca CILEK vendio un total de piezas: " + str(cilek) + "\nLa marca TOYSTORY vendio un total de piezas: " + str(toy) + "\nLa marca LOL vendio un total de piezas: " + str(lol))
archivo.close()
archivoA.close()
