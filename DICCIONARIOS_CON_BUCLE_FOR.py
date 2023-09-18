#Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola:
#Categoría = Teclados.
#Modelo = HyperX Alloy FPS Pro.
#Precio = 89,99.

teclado1 = {
	'Categoria': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',     #Generamos nuestro primer diccionario con sus especificaciones
	'Precio': '89,99'
}

teclado2 = {
	'Categoria': 'Teclados',
	'Modelo': 'Corsair K55 RGB',         #Generamos nuestro segundo diccionario con sus especificaciones
	'Precio': '59,99'
}

for x, y in teclado1.items():#Utilizamos la funcion 'items()'la cual nos ayuda a obtiene los elementos del diccionario 
	print(x, ": ", y , ".") #Mostramos en pantalla todo sobre el teclado y agregando las obserbaciones de la practica
