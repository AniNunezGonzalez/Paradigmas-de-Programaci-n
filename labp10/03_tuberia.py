''''
Aniela Montserrat Núñez González
PARADIRMAS DE PROGRAMACIÓN
2AV1
Profesor: Julián Tercero Becerra Sagredo
"Laboratorio 10 de Python (MPI avanzado y multiprocesamiento en python)"
'''
from multiprocessing import Process, Pipe

def f(extremo):
    extremo.send([0,1,2,3,4])
    extremo.close()

def g(extremo):
    a = extremo.recv()
    for i in a:
        a[i] += 100
    print(a)

if __name__ == "__main__":
    extremo1, extremo2 = Pipe()
    proceso1 = Process(target=f, args=(extremo1,))
    proceso2 = Process(target=g, args=(extremo2,))
    proceso2.start()
    proceso1.start()
    proceso1.join()
    proceso2.join()