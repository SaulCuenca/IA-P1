def Gael(): #Creamos la primera Funcion
    edad = 22 #Le damos valor a la variable
    print('Gael Tiene ', edad , 'A\xf1os de Edad\n\n')  #La frase que mostraremos en pantalla con nuestro valor edad
    print('Gabriela Tiene ', edad1 , 'A\xf1os de Edad\n\n')  #La frase que mostraremos en pantalla con nuestro valor global retornado de Gabriela
    print('Saul va a cumplir ', edad2 , 'A\xf1os de Edad\n')  #La frase que mostraremos en pantalla con nuestro valor global retornado de Saul

def Gabriela():  #Creamos la segunda Funcion
    global edad1  #Hacemos que nuestra variable pase a ser global
    edad1 = 45  #Le damos valor a la variable
    
def Saul(): #Creamos la tercera Funcion
    global edad2  #Hacemos que nuestra variable pase a ser global
    edad2 = 23  #Le damos valor a la variable
    
#Algo que hay que tener en cuenta es la´posicion por  que si empezamos por la funcion Gabriel no estara guardado los valores de Saul y Gabriel
Gabriela() #Mostramos en pantalla La Fuencion Gabriela
Saul()  #Mostramos en pantalla La Fuencion Saul
Gael()  #Mostramos en pantalla La Fuencion Gaul