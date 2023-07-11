"""
Escribe un algoritmo que tome una lista como parámetro y 
devuelva una nueva lista con los elementos en orden inverso.
"""

def inversa(lista):
    lista.reverse()
    return lista

lista = ['gato', 'perro', 1, 2, 3.5, 'auto']

resultado = inversa(lista)

print(resultado)