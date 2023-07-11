"""
Escribe un algoritmo que tome una lista como parámetro y 
devuelva una nueva lista que elimine los elementos duplicados.
"""

def eliminar_duplicados(lista):
    
    conjunto = set(lista)
    
    return conjunto

elementos = [1, 2, 2, 3, 3, 'hola', 'hola', 'chau']

unicos = eliminar_duplicados(elementos)

print(unicos)
