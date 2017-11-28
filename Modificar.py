lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modificar(l):
    
    l = list(set(l))  # Borrar los elementos duplicados (recrea la lista a partir de un nuevo diccionario)
    l.sort(reverse=True)  # Ordenar la lista de mayor a menor
    for i,n in enumerate(l):  # Eliminar todos los números impares
        if n%2 != 0:
            del( l[i] )
            
    suma = sum(l)  # Realizar una suma de todos los números que quedan
    l.insert(0, suma)  # Añadir como primer elemento de la lista la suma realizada
    return l  # Devolver la lista modificada
   

nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )