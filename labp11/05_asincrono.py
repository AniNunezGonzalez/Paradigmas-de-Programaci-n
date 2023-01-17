''''
Aniela Montserrat Núñez González
2AV1
PARADIGMAS DE PROGRAMACIÓN
Profesor: Julián Tercero Becerra Sagredo
"Laboratorio 11 de Python (Acerelerando Python con NUMBA y NUMBA-CUDA)"
'''
import multiprocessing as mp
import numpy as np
import time

def mi_function(i, param1, param2, param3):
    #Calcula un polinomio
    result = param1**2 + param2 + param3
    #se hace tonta 2 segundos
    time.sleep(2)
    return (i,result)

def get_result(result):
    #Se inscriben en la lista global
    #(Mal estilo de programación)
    global results
    results.append(result)

#=====================
# Programa principal
#=====================
if __name__ == "__main__":

    #Matriz de 10x3 números al azar
    params = np.random.random((10,3))*100.0
    results = []
    ts = time.time()

    #Un grupo de procesos (pool)
    pool = mp.Pool(mp.cpu_count())

    #Loop de primera dimensión del arreglo
    for i in range(0, params.shape[0]):
        #Correr asincrónicamente my_function con argumentos args y cuando termine correr get_result
        pool.apply_async(mi_function, args = (i,params[i,0], params[i,1], params[i,2]), callback=get_result)

    #Cerrar el grupo
    pool.close()
    #Esperar que termine el grupo
    pool.join()

    print("Tiempo en paralelo = ", time.time()-ts)
    print(results)
