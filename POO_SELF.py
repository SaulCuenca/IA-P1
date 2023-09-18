class ceti:
	def __init__(self, nombre, apellidos, carrera, grado, turno):
		self.nombre = nombre
		self.apellidos = apellidos
		self.carrera = carrera
		self.grado = grado
		self.turno = turno


	def mostrar(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos, '\nCarrera:', self.carrera, '\nGrado:', self.grado, '\nTurno:', self.turno)
		

estudiante1 = ceti('Saul Armando', 'Cuenca Martinez', 'Mecatronica', 'sexto', 'Vespertino\n\n')


estudiante2 = ceti('Jose Cruz', 'Torres Palomares', 'Mecatronica', 'sexto', 'Vespertino')

estudiante1.mostrar()
estudiante2.mostrar()