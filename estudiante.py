from persona import Persona

class Estudiante(Persona):

  def __init__(self, nombre, cedula, nivel):
    Persona.__init__(self, nombre, cedula)
    self.nivel = nivel

  def __str__(self):
     return "Nombre: %s, Cedula: %s, Nivel: %s" % (self.nombre, self.cedula, self.nivel)



