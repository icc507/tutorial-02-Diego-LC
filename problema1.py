#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)

def toIntList(t):
    for i in range(len(t)):
        if t[i].isnumeric():
            t[i] = int(t[i])
    return t
    

t1 = input().split()
t1 = tuple(toIntList(t1))

t2 = input().split()
t2 = tuple(toIntList(t2))
print(t2 + t1 + t2)