#¿Cuántos argumentos se utilizan en cada una de estas llamadas?

def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marron', 'naranja')

#Los resultados son:
#Línea 4: cuatro argumentos
#Línea 5: tres argumentos
#Línea 6: un argumento
#Línea 7: dos argumentos

#Completa el siguiente fragmento de código:
#def colores(*args):
#	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

#colores()

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco est mal.')

colores("rojo","azul") #Agregamos los parametros que guardar args 


#Crea una función que realice la suma de cinco números utilizando solo *args. 
#Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().

def suma(*args): #Usamos args con el fin de que tengamos varios numeros
	total = 0#El valor total nos guardara el valor y lo igualamos a cero para que de ahi empiece a sumar 
	for x in args: #Los ciclos empezaran hasta llegar a un cierto numero
		total = total + x #Aqui se guardara lo sumado y seguire aumentando
	print("La suma de los numeros es: ",total) #Para este punto ya terminara el FOR Y nos mostrara en pantalla el resultado

suma(3,4,10,13,15) #Mandamos llamar a la fucion y retornara los numeros que usara args