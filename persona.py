class Persona:
  ''' Esta es la clase base de objetos de tipo persona '''
  def __init__(self, nombre, cedula):
    self.nombre = nombre
    self.cedula = cedula
  
  def __str__(self): 
    return "Nombre: %s, Cedula: %s" % (self.nombre, self.cedula)

  def getNombre(self):
    ''' Este metodo devuelve el nombre de la persona '''
    return self.nombre
  
  def getCedula(self):
    ''' Este metodo devuelve la cedula de la persona '''
    return self.cedula

