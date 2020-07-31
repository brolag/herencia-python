from estudiante import Estudiante
from profesor import Profesor
from grupo import Grupo


def main(): 
  profesor = Profesor('Alfredo', '111111', 'Programacion')
  grupoB = Grupo(profesor)

  grupoB.matricularEstudiante(Estudiante('Ana', '111111', '1'))
  grupoB.matricularEstudiante(Estudiante('Pedro', '222222', '1'))
  grupoB.matricularEstudiante(Estudiante('Maria', '333333', '1'))

  print(grupoB.imprimirListaEstudiantes())

main()


