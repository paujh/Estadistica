##Aqui ya haremos la grafica, con los datos recaudados y guardados en el archivo "DatosEstadistica.txt" 

import matplotlib.pyplot as plt

plt.figure() 
plt.pie([58,25,115,28,30,35],autopct='%1.1f%%',colors=['b','g','c','y','r','m'])
plt.legend(["LEGO","Apache","DISNEYCOLLECTION","CILEK","TOYSTORY","LOL"])
plt.title("Pocentaje que vendio cada marca \nen una semana",fontsize=20)
plt.axis('equal')
plt.savefig("Estadistica.png")
plt.show()
