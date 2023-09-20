class ceti:
	def __init__(self, nombre, apellidos, carrera, grado, turno): #Creamos los elementos que tendra nuestra clase
		self.nombre = nombre 
		self.apellidos = apellidos
		self.carrera = carrera            #Les brindamos una variable en la cual se guardaran nuestros datos
		self.grado = grado
		self.turno = turno


	def mostrar(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos, '\nCarrera:', self.carrera, '\nGrado:', self.grado, '\nTurno:', self.turno) #Aqui solo es lo que msotraremos en pantalla usando self
		


estudiante1 = ceti('Saul Armando', 'Cuenca Martinez', 'Mecatronica', 'sexto', 'Vespertino\n\n') #Guardamos cada valor en estudiante 1

estudiante1.mostrar() #Mostramos los datos del estudiante 1


class ceti_nuevo(ceti): #Creamos la nueva clase que viene de nuestra primera clase y que tendra herencia
	def __init__(self, nombre, apellidos, carrera, grado, turno, registro):#Creamos que valores tendra nuestra nueva clase y agragamos un nuevo valor
		ceti.__init__(self, nombre, apellidos, carrera, grado, turno)#De aqui estamos llamando que tendra de la primera clase los valores
		self.registro = registro #Aqui agregamos un nueva self que nos guardara nuestro codigo osea la nueva variable
		

	def mostrar_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos, '\nCarrera:', self.carrera, '\nGrado:', self.grado, '\nTurno:', self.turno, '\nRegistro:', self.registro) #Aqui solo es lo que mostraremos en pantalla usando self y agregamos el nuevo que es registro
		



estudiante2 = ceti_nuevo('Jose Cruz', 'Torres Palomares', 'Mecatronica', 'sexto', 'Vespertino', '21110324') #Guardamos cada valor en estudiante 2

estudiante2.mostrar_datos() #Mostramos los datos del estudiante 2  pero ya utilizando la herencia y nuestro nuevo dato
