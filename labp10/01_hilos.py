''''
Aniela Montserrat Núñez González
PARADIRMAS DE PROGRAMACIÓN
2AV1
Profesor: Julián Tercero Becerra Sagredo
"Laboratorio 10 de Python (MPI avanzado y multiprocesamiento en python)"
'''
from threading import Thread
import os
import math
import time

def calc():
    for i in range(0,4000000):
        math.sqrt(i)

threads = []
cpus = os.cpu_count()
print("Núcleos en tu CPU: ", cpus)
for i in range(cpus):
    print("registrando el hilo %d" % i)
    threads.append(Thread(target=calc))

start = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = time.time()
print("Se tardó: ",end-start)
