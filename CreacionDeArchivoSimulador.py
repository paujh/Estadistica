##Suponemos que 50 personas hicieron compras en una semana, sin limite de productos, y piezas de los mismos, que pueden comprar, y en la Tienda hay un inventario ilimitado
##Lo que haremos ahora será una lista de los 100 clientes con sus respectivas listas de artículos comprados (carritos). Todo sera aleatorio, asi podemos hacer una buena estadistica 
##La estadistica que buscamos es ver el porcentaje que vendio cada marca de acuerdo a las ventas totales en esa semana.

import random as r

##Haremos la lista de los productos de la Tienda, en este caso solo necesitaremos su nombre, mas delante definiremos como sabremos 

##Desde el inicio abriremos un archivo, donde se guardaran los carritos

Productos = ["muneco","triciclo","munecas","camacoche","buz","elsa","vehiculo","figuras","casa","rayo"] 

##Haremos la clase Carrito, para poder guardar los datos en un archivo, de donde sacaremos los datos para la grafica de la estadistica; para esto solo necesitaremos que tenga nombre, y su carrito

carritos = open("Carritos.txt","w")

class Carrito:

  def __init__(self,productos):
    self.productos = productos

  def carritoPseudo(n):
    Productos = ["muneco","triciclo","munecas","camacoche","buz","elsa","vehiculo","figuras","casa","rayo"]
    l = []
    for i in range(n):
      p = r.choice(Productos)
      l.append(p)
    return l


l1 = Carrito.carritoPseudo(2)
l2 = Carrito.carritoPseudo(6)
l3 = Carrito.carritoPseudo(4)
l4 = Carrito.carritoPseudo(13)
l5 = Carrito.carritoPseudo(5)
l6 = Carrito.carritoPseudo(8)
l7 = Carrito.carritoPseudo(13)
l8 = Carrito.carritoPseudo(9)
l9 = Carrito.carritoPseudo(8)
l10 = Carrito.carritoPseudo(10)
l11 = Carrito.carritoPseudo(6)
l12 = Carrito.carritoPseudo(7)
l13 = Carrito.carritoPseudo(14)
l14 = Carrito.carritoPseudo(5)
l15 = Carrito.carritoPseudo(4)
l16 = Carrito.carritoPseudo(1)
l17 = Carrito.carritoPseudo(6)
l18 = Carrito.carritoPseudo(1)
l19 = Carrito.carritoPseudo(3)
l20 = Carrito.carritoPseudo(10)
l21 = Carrito.carritoPseudo(9)
l22 = Carrito.carritoPseudo(11)
l23 = Carrito.carritoPseudo(13)
l24 = Carrito.carritoPseudo(15)
l25 = Carrito.carritoPseudo(8)
l26 = Carrito.carritoPseudo(11)
l27 = Carrito.carritoPseudo(12)
l28 = Carrito.carritoPseudo(2)
l29 = Carrito.carritoPseudo(3)
l30 = Carrito.carritoPseudo(10)
l31 = Carrito.carritoPseudo(1)
l32 = Carrito.carritoPseudo(8)
l33 = Carrito.carritoPseudo(3)
l34 = Carrito.carritoPseudo(5)
l35 = Carrito.carritoPseudo(6)
l36 = Carrito.carritoPseudo(7)
l37 = Carrito.carritoPseudo(8)
l38 = Carrito.carritoPseudo(12)
l39 = Carrito.carritoPseudo(3)
l40 = Carrito.carritoPseudo(10)
l41 = Carrito.carritoPseudo(5)
l42 = Carrito.carritoPseudo(8)
l43 = Carrito.carritoPseudo(4)
l44 = Carrito.carritoPseudo(9)
l45 = Carrito.carritoPseudo(2)
l46 = Carrito.carritoPseudo(5)
l47 = Carrito.carritoPseudo(1)
l48 = Carrito.carritoPseudo(3)
l49 = Carrito.carritoPseudo(1)
l50 = Carrito.carritoPseudo(10)

carritos.write(str(l1) + "\n" + str(l2) + "\n" + str(l3) + "\n" + str(l4) + "\n" + str(l5) + "\n" + str(l6) + "\n" + str(l7) + "\n" + str(l8) + "\n" + str(l9) + "\n" + str(l10) + "\n" + str(l11) + "\n" + str(l12) + "\n" + str(l13) + "\n" + str(l14) + "\n" + str(l15) + "\n" + str(l16) + "\n" + str(l17) + "\n" + str(l18) + "\n" + str(l19) + "\n" + str(l20) + "\n" + str(l21) + "\n" + str(l22) + "\n" + str(l23) + "\n" + str(l24) + "\n" + str(l25) + "\n" + str(l26) + "\n" + str(l27) + "\n" + str(l28) + "\n" + str(l29) + "\n" + str(l30) + "\n" + str(l31) + "\n" + str(l32) + "\n" + str(l33) + "\n" + str(l34) + "\n" + str(l35) + "\n" + str(l36) + "\n" + str(l37) + "\n" + str(l38) + "\n" + str(l39) + "\n" + str(l40) + "\n" + str(l41) + "\n" + str(l42) + "\n" + str(l43) + "\n" + str(l44) + "\n" + str(l45) + "\n" + str(l46) + "\n" + str(l47) + "\n" + str(l48) + "\n" + str(l49) + "\n" + str(l50))
carritos.close()
