''''
Aniela Montserrat Núñez González
PARADIGMAS DE PROGRAMACIÓN
Profesor: Julián Tercero Becerra Sagredo
2AV1
Laboratorio 6 de Python "CORRER ATRAPANDO ERRORES (EXCEPCIONES)"
'''
from aplicacion.banco.cliente_bancario import ClienteBancario

#==============================================
# try: intenta (correr las instrucciones)
# except: atrapar el error en una variable e
# e se puede convertir a string
#==============================================

#===========================================
# Error por sacar más dinero del que tiene
#===========================================
try:
    cliente = ClienteBancario("Aniela Montserrat", "Núñez González", 19, 0.0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo())

#===============================================
# Exception es el objeto más general del error
#===============================================
except Exception as e:
    print("Error: " + str(e))

#=====================================
# Error por usar un atributo privado
#=====================================
try:
    print(cliente.__nombres)
except Exception as ex:
    print("Error: " + str(ex))

#=================
# Forma correcta
#=================
print(cliente.nombres)