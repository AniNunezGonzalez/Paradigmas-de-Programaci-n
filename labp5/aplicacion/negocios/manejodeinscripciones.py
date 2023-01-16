''''
Aniela Montserrat Núñez González
2AV1
PARADIGMAS DE PROGRAMACIÓN
Profesor: Julián Tercero Becerra Sagredo
"INTERFACES Y MÓDULOS"
'''

from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#========================
# Clase storemanager
# NO TIENE VARIABLES!!!
#========================
class ManejoDeInscripciones:
    #==================================================================
    # Decorador staticmethod
    # El objeto sólo tiene la función inscribirUsuario
    # ENVUELVE LA FUNCIÓN SIN LLAMAR VARIABLES LOCALES
    # El objeto ManejoDeInscripciones es la interface intercambiable
    #===================================================================
    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("------> Guardando usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()