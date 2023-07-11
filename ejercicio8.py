"""
Escribe un programa que cuente la frecuencia de cada elemento en una lista y 
muestre los resultados. numeros = [10, 20, 30, 20, 40, 10, 50, 30]
"""

def frecuencia_elementos(lista):
    frecuencia = {}
    
    for elemento in lista:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
    return frecuencia


numeros = [10, 20, 30, 20, 40, 10, 50, 30]

frecuencias = frecuencia_elementos(numeros)

for elemento, frecuencia in frecuencias.items():
    print(f"El elemento {elemento} aparece {frecuencia} veces")
    
    