''''
Aniela Montserrat Núñez González
PARADIGMAS DE PROGRAMACIÓN
2AV1
Profesor: Julián Tercero Becerra Sagredo
Laboratorio 7 de Python "PROGRAMACIÓN FUNCIONAL"
'''
#===========================================
# Uso de reducciones (colapsar resultados)
#===========================================

#==================================================
# Multiplicación de todos los números en la lista
#==================================================

from functools import reduce

bigdata = [2,3,5,7,11,13,17,19,23,29]

#==============
# Función x*y
#==============
multiplicar = lambda x,y: x*y

print(reduce(multiplicar,bigdata))

#===========================================================
# Reduce le aplica la función por pares a los resultados y
# el siguiente elemento comenzando con los dos primeros
# elementos
#===========================================================
