def suma(lista):
    contador = 0
    for i in lista:
        contador += i
    return contador

def resta(lista):
    contador = 0
    for i in lista:
        contador -= i
    return contador

lista = [1,2,3,4]

total = suma( lista )
print(total)

total = resta( lista )
print(total)