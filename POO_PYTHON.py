class ceti:
	nombre = ''
	apellidos = ''
	carrera = ''
	grado= ''
	turno = ''

	def mostrar(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos, '\nCarrera:', self.carrera, '\nGrado:', self.grado, '\nTurno:', self.turno)

estudiante = ceti()

estudiante.nombre = 'Saul Armando'
estudiante.apellidos = 'Cuenca Martinez'
estudiante.carrera = 'Mecatronica'
estudiante.grado = 'Sexto'
estudiante.turno = 'Vespertino'

estudiante.mostrar()
