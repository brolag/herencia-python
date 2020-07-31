class Grupo:
  listaEstudiantes = []

  def __init__(self, profesor):
    self.profesor = profesor

  def matricularEstudiante(self, estudiante):
    self.listaEstudiantes.append(estudiante)

  def imprimirListaEstudiantes(self):
    for estudiante in self.listaEstudiantes:
      print(estudiante.getNombre()) 

  



