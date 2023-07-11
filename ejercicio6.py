"""
Escribe un programa que encuentre el número más grande 
en una lista de números. numeros = [10, 5, 25, 30, 15]
"""

def mayor(lista):
    
    lista.sort()
    
    mayor = lista[len(lista)-1]
    
    return mayor

numeros = [10, 5, 25, 30, 15]

mayor = mayor(numeros)

print(mayor)