
lista = [2, 31, 312, 123, -123, 43,1]

# Ordenamiento por selección
# Buscas el mayor 
# Lo pones en el final 
def encontraMayor(lista):
    mayor = lista[0]
    posMayor = 0
    for i in range(0, len(lista)):
        if (lista[i] > mayor):
            mayor = lista[i]
            posMayor = i
    return posMayor
def ordenamientoSeleccion(l):
    lista = l.copy()
    i = len(lista) - 1
    while i != -1:
        posMayor = encontraMayor(lista[:i + 1])
        lista[posMayor], lista[i] = lista[i], lista[posMayor] 
        i -= 1
    return lista

# Ordenamiento por inserción


def ordenamientoInsercion(l):
    lista = l.copy()
    i = 1
    while i != len(lista):
        subLista = lista[:i]
        valor = lista[i]
        band = True
        for j in range(len(subLista) - 1):
            if (valor <= subLista[j] and valor >= subLista[j+1]):
                lista[i], subLista[j] = subLista[j], lista[i]
                band = False
                break
        if (band):
            for j in range(len(subLista) - 1):
                if (valor <= subLista[j]):
                    lista[i], subLista[j] = subLista[j], lista[i]
                    break
        i += 1
    return lista



def quick_sort(lista):
    _quick_sort(lista, 0, len(lista) - 1)
def _quick_sort(lista, inicio, fin):
    if inicio >= fin:
        return
    menores = _partition(lista, inicio, fin)
    _quick_sort(lista, inicio, menores - 1)
    _quick_sort(lista, menores + 1, fin)
def _partition(lista, inicio, fin):
    pivote = lista[inicio]
    menores = inicio
    for i in range(inicio + 1, fin + 1):
        if lista[i] < pivote:
            menores += i
            if i != menores:
                lista[menores], lista[i] = lista[i], lista[menores]
    if inicio != menores:
        lista[menores], lista[inicio] = lista[inicio], lista[menores]
        return menores
    
quick_sort(lista)
print(lista)