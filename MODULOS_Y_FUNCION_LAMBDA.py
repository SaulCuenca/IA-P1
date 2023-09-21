
import math

print("Bienvenido a continuacion podras calcula el area total de un cono circula\n\n")

altura = int(input("Cual es la altura..?\n\n")) #Hacemos que nos brinde la altura y la guardamos

radio = int(input("Cual es tu radio..?\n\n")) #Hacemos que nos brinde el y la guardamos

genera = math.sqrt(altura + radio ) #Realizamos la operacion para calcular la generatriz


print("Primero sacaremos la generatriz\n\n" "Tu generatriz es: ", "{0:.5f}".format(genera) ) #Mostramos en pantalla cual sera la generatriz con 5 decimales

arealateral = math.pi * genera * radio #Realizamos la operacion para calcular el area total

print("\n\nAhora calcularemos tu area laterar\n\n " "Tu area lateral es: " , "{0:.5f}".format(arealateral) ) #Mostramos en pantalla cual sera el area total con 5 decimales
areadelabase = (math.pi * (radio**2)) #Realizamos la operacion utilizamos pi y operacion al cuadrado
areatotal = arealateral + areadelabase #Damos todo el valor a esta variable


print("\n\nPor Ultimo calcularemos tu area total \n\n " "Tu area total es: " , "{0:.5f}".format(areatotal) ) #Mostramos en pantalla el area total usando que solo imprima 5 decimalles

a = arealateral #Guardamos el valor en a
b = areadelabase #Guardamos el valor en b
mismo = lambda a,b: a + b #Aqui utilizamos lambda primero unando variables y depues operaciones en lugar de usar un def

print("\n\nMostrando el resultado pero ahora con lambda: \n\n") #Mostramos en panatalla un anuncio de que dara el mismo resultado pero con lambda
print(mismo(a,b)) #Aqui si mostramos el resultado