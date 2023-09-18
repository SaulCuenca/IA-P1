#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. 
#Muestra la última clave ('Modelo') que queda en la consola.

teclado1 = {
	'Categoria': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',   #Generamos nuestro primer diccionario con sus especificaciones
	'Precio': '89,99'
}

teclado2 = {
	'Categoria': 'Teclados',
	'Modelo': 'Corsair K55 RGB',        #Generamos nuestro segundo diccionario con sus especificaciones
	'Precio': '59,99'
}

del teclado1 #Al utilizar el del borrara el teclado 1

del teclado2["Categoria"] #Aqui igual usamos el del pero solo elimina la categoria
teclado2.pop("Precio")    #Eliminamos el precio con la funcion POP
print(teclado2) #Mostramos en pantalla lo que nos quedo del diccionario2 


for x, y in teclado2.items():
	print(x, ": ", y) #De igual forma como lo pide mostramos que nos quedo de ese diccionariopero usando for
