#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)

def toIntList(t):
    for i in range(len(t)):
        if t[i].isnumeric():
            t[i] = int(t[i])
    return t

t = input().split()
t.reverse()
t = tuple(toIntList(t))
print(t)
