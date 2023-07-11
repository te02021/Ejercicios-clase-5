"""
Escribe un algoritmo que tome una lista de números como parámetro y 
devuelva la suma de todos los elementos de la lista.
"""

numeros = [3, 4, 4, 23, 12, 65, 76, 12, 15]

suma = 0

for num in range(0, len(numeros)):
    suma += numeros[num]
    
print(suma)