from persona import Persona

class Profesor(Persona):
  def __init__(self, nombre, cedula, especialidad):
    Persona.__init__(self, nombre, cedula)
    self.especialidad = especialidad

  def __str__(self):
    return "Nombre: %s, Cedula: %s, Especialidad: %s" % (self.nombre, self.cedula, self.especialidad)