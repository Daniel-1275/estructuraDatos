class Nodo(object):
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
    def __str__(self):
        return "\n>>> "+str(self.dato)

class ListaEnlazada(object):
    def __init__(self):
        self.primero = None
        self.len = 0
    def __str__(self):
        nodo = self.primero
        cad = ""
        while (nodo):
            cad += str(nodo)
            nodo = nodo.siguiente
        return cad
    def __len__(self):
        return self.len
    def insertarUltimo(self, dato):
        nuevo = Nodo(dato)
        if (self.estaVacio()):
            self.primero = nuevo
        else:
            nodoActual = self.primero
            while (nodoActual.siguiente):
                nodoActual = nodoActual.siguiente
            nodoActual.siguiente = nuevo
        self.len += 1
    def insertarPrincipio(self, dato):
        nuevo = Nodo(dato)
        if (self.estaVacio()):
            self.primero = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero = nuevo
        self.len += 1
    def insertar(self, dato, i=None):
        if (i == None):
            self.insertarUltimo(dato)
        elif (i == 0):
            self.insertarPrincipio(dato)
        elif (i < 0) or (i >= self.len):
            raise IndexError('Indice fuera de rango')
        else:
            nuevo = Nodo(dato)
            nodoActual = self.primero
            contador = 0
            while (nodoActual.siguiente and contador != i - 1):
                nodoActual = nodoActual.siguiente
                contador += 1
            nuevo.siguiente = nodoActual.siguiente
            nodoActual.siguiente = nuevo
            self.len += 1
    def removerPrincipio(self):
        if (not self.estaVacio()):
            dato = self.primero.dato
            p = self.primero
            self.primero = self.primero.siguiente
            del p
            self.len -= 1
            return dato
        return None
    def removerUltimo(self):
        if (not self.estaVacio()):
            if (self.len == 1):
                return self.removerPrincipio()
            else:
                nodoAnterior = self.primero
                nodoActual = nodoAnterior.siguiente
                while (nodoActual.siguiente):
                    nodoAnterior = nodoActual
                    nodoActual = nodoAnterior.siguiente
                dato = nodoActual.dato
                nodoAnterior.siguiente = None
                del nodoActual
                self.len -= 1
                return dato
        return None
    def remover(self, i=None):
        if (i == None or i == self.len - 1):
            return self.removerUltimo()
        elif (i < 0) or (i >= self.len):
            raise IndexError('Indice fuera de rango')
        elif (i == 0):
            return self.removerPrincipio()
        else:
            nodoActual = self.primero
            contador = 0
            while (nodoActual.siguiente and contador != i - 1):
                nodoActual = nodoActual.siguiente
                contador += 1
            nodoRemover = nodoActual.siguiente
            dato = nodoRemover.dato
            nodoActual.siguiente = nodoRemover.siguiente
            nodoRemover.siguiente = None
            del nodoRemover
            self.len -= 1
            return dato
        return None
    def estaVacio(self):
        return True if (self.len == 0) else False

"""
lista = ListaEnlazada()


lista.insertar(20)
lista.insertar(10, 0)
lista.insertar(30)
lista.insertar(50)
lista.insertar(40, 3)
lista.insertar(70)
lista.insertar(60, 5)
lista.insertar(0, 0)
"""