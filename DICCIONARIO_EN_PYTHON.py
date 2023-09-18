#Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio con presentación en un print().
# El resultado será esto en la consola: El modelo Corsair K55 RGB cuesta 59,99 $.

teclado1 = {
	'Categoria': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro', #Guardamos informacion teclado 1
	'Precio': '89,99'
}

teclado2 = {
	'Categoria': 'Teclados',
	'Modelo': 'Corsair K55 RGB',     #Guardamos informacion teclado 2
	'Precio': '59,99'
}

consulta1 = teclado2["Modelo"] #Guardamos nombre del modelo en consultar1
consulta2 = teclado2["Precio"] #Guardamos precio en consultar2
print("El modelo " + consulta1 + " cuesta " + consulta2 + " $ .") #Mostramos la informacion que consultamos 
