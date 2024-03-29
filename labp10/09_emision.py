''''
Aniela Montserrat Núñez González
PARADIRMAS DE PROGRAMACIÓN
2AV1
Profesor: Julián Tercero Becerra Sagredo
"Laboratorio 10 de Python (MPI avanzado y multiprocesamiento en python)"
'''
#=========================
# Broadcast con MPI
# distribución de datos
#=========================
from mpi4py import MPI

#Objeto comunicador
comm = MPI.COMM_WORLD

#Quién soy
rank = comm.Get_rank()

#==========================================
# El proceso 0 tiene datos y los otros no
#==========================================
if rank == 0:
    data = {'key1' : [7, 2.72, 2+3],
            'key2' : ('abc', 'xyz')}
else:
    data = None

#=====================================================
# Enviar diccionario a todos los procesos desde root
#=====================================================
data = comm.bcast(data, root=0)
print(data)