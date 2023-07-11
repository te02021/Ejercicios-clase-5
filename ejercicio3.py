"""
Escribe un algoritmo que tome una lista de números al azar como parámetro y 
devuelva una nueva lista que contenga solo los números impares.
"""

def impar(lista):
    
    lista1 = []
    
    for elemento in lista:
        if elemento % 2 != 0:
            lista1.append(elemento)
            
    return lista1

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num_impar = impar(numeros)

print(num_impar)