"""
Escribe un programa que elimine los elementos duplicados de una lista. 
(Busca dos maneras diferentes de resolverlo). numeros = [10, 20, 30, 20, 40, 10, 50, 30]
"""

def eliminar_duplicados1(lista):
    conjunto = set(lista.sort())
    return conjunto

def eliminar_duplicados2(lista):
    lista_nueva = []
    for elemento in lista:
        if elemento not in lista_nueva:
            lista_nueva.append(elemento)
    return lista_nueva

numeros = [10, 20, 30, 20, 40, 10, 50, 30]

print(eliminar_duplicados1(numeros))

print(eliminar_duplicados2(numeros))


