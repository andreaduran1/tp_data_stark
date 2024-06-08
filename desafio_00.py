from funciones import *
from data_stark import lista_personajes



# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
nombres_heroes = mapear_lista(lambda heroe: (heroe["nombre"]), lista_personajes)
mostrar_campo(nombres_heroes)
print()
# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
# la altura del mismo
mostrar_lista_tuplas(
    mapear_lista(lambda heroe: (heroe["nombre"], heroe["altura"]), lista_personajes)
)
print()

# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)

heroe_mas_alto = reduce_lista(lambda ant, act: act if ant['altura'] < act['altura'] else ant, lista_personajes)
mostrar_heroe(heroe_mas_alto)
print()
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
heroe_mas_bajo = reduce_lista(lambda ant, act: act if ant['altura'] > act['altura'] else ant, lista_personajes)
mostrar_heroe(heroe_mas_bajo)
print()
# F. Recorrer la lista y determinar la altura promedio de los superhéroes
campo = "a"
promedio_campo(lista_personajes, campo)

# G. Informar cual es la identidad del superhéroe asociado a cada uno de los
# indicadores anteriores (MÁXIMO, MÍNIMO)
print(heroe_mas_alto["identidad"])
print(heroe_mas_bajo["identidad"])
# H. Calcular e informar cual es el superhéroe más y menos pesado.
heroe_mas_pesado = reduce_lista(lambda ant, act: act if ant['peso'] < act['peso'] else ant, lista_personajes)
print(f"El heroe más pesado es {heroe_mas_pesado["nombre"]} y pesa {heroe_mas_pesado["peso"]}kg.")
print()
heroe_mas_liviano = reduce_lista(lambda ant, act: act if ant['peso'] > act['peso'] else ant, lista_personajes)
print(f"El heroe más liviano es {heroe_mas_liviano["nombre"]} y pesa {heroe_mas_liviano["peso"]}kg.")
print()

# I. Ordenar el código implementando una función para cada uno de los valores
# informados.
# J. Construir un menú que permita elegir qué dato obtener

