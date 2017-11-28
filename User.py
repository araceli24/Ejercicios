class User:
    def __init__(self, nombre, arrayMensajes):
        self.nombre= nombre
        self.arrayMensajes = arrayMensajes


# nos devuelve un usuario si está dentro de la lista
def buscarEnLista(nombre, listaUsers):
    # recorro la lista
    for u in listaUsers:
        #si el nombre está en esa lista lo devuelvo
        if(u.nombre == nombre):
            return u
    #en caso de no encontrar nada, devuelvo None
    return None


#lista vacia de users
listaUsers = []
#leemos el fichero
fichero = open("mensajes.txt", "r")
#leemos todas las lineas del fichero
lineas = fichero.readlines()
#print(lineas)
#recorremos cada una de las lineas del fichero
for linea in lineas:
    #separamos el nombre del mensaje
    #datos será un array con 2 elementos
    dato = linea.split("=")
    nombre = dato[0]
    mensaje = dato[1]
    user = buscarEnLista(nombre, listaUsers)
    if(user == None):   #en esta caso el usuario no está en la lista
        listaMensajes = []
        listaMensajes.append(mensaje)
        nuevoUser = User(nombre, listaMensajes)
        listaUsers.append(nuevoUser)
    else: #en este caso el usuario si esta en la lista
        user.arrayMensajes.append(mensaje)


# Mostramos en pantalla los mensajes de casa usuario
for u in listaUsers:
    print("Mensajes de "+u.nombre)
    for m in u.arrayMensajes:
        print("   "+m)
