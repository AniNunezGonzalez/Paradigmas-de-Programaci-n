''''
Aniela Montserrat Núñez González
2AV1 
PARADIGMAS DE PROGRAMACIÓN
Profesor: Julián Tercero Becerra Sagredo
"INTERFACES Y MODULOS"
'''
#===========================================================
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo basededatos.py: trae el objeto Basededatos
#===========================================================
from aplicacion.repositorio.basededatos import BaseDeDatos

#======================================================================
# Del directorio aplicacion, el subdirectorio repositorio,
# El archivo s3.py: trae el objeto S3
#======================================================================
from aplicacion.repositorio.s3 import S3

#========================================================================
# Del directorio aplicacion, el subdirectorio repositorio,
# el archivo sistemadearchivos.py: trae el objeto SistemaDeArchivos
#========================================================================
from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos

#=======================================================
# Del directorio aplicacion, el subdirectorio modelos,
# el archivo usuario.py: trae el objeto Usuario
#=======================================================
from aplicacion.modelos.usuario import Usuario

#============================================================================
# Del directorio aplicacion, el subdirectorio negocios,
# el archivo manejodeinscripciones.py: tres el objeto ManejoDeInscripciones
#============================================================================
from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones

#==========================
# Crear el objeto Usuario
#==========================
usuario = Usuario("Ani","Núñez",19)

#=====================
# Crear el objeto s3
#=====================
repositorioS3 = S3("321321321","sdf324223","MiCubeta")

#=============================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#=============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#===================================
# Crear el objeto sistemadearchivos
#===================================
repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

#=============================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#=============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")

#=============================
# Crear el objeto basededatos
#=============================
repositorioBaseDeDatos = BaseDeDatos("localhost","admin","admin123")

#==============================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#==============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")

