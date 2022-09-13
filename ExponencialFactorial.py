'''
Aniela Montserrat Núñez González
Paradigmas de Programación
Algoritmo que aproxima el valor de e
con el uso de la forma 1+x+x^2/2!...
'''
n = 1000
fact = 1.0
e = 1.0
x = 2.0
xx = 1.0
for i in range(1,n):
    xx *= x
    fact *= float(i)
    s = 1.0/fact
    e += s

print("xx= ", str(xx))
print("fact= ",str(fact))
print("s= ",str(s))
print("e= ",str(e))
