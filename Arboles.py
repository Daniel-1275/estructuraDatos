class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.nodoIzq = None
        self.nodoDer = None
    def insertar(self, valorInsertar):
        if (valorInsertar < self.dato):
            if (self.nodoIzq == None):
                self.nodoIzq = NodoArbol(valorInsertar)
            else:
                self.nodoIzq.insertar(valorInsertar)
        elif(valorInsertar > self.dato):
            if (self.nodoDer == None):
                self.nodoDer = NodoArbol(valorInsertar)
            else:
                self.nodoDer.insertar(valorInsertar)


class Arbol:
    def __init__(self):
        self.raiz = None
    def insertarNodo(self, dato):
        if (self.raiz == None):
            self.raiz = NodoArbol(dato)
        else:
            self.raiz.insertar(dato)
    def recorridoPreorden(self):
        self.ayudantePreorden(self.raiz)
    def ayudantePreorden(self, nodo: NodoArbol):
        if (nodo == None):
            return
        print(nodo.dato, end=" ")
        self.ayudantePreorden(nodo.nodoIzq)
        self.ayudantePreorden(nodo.nodoDer)
    def recorridoInorden(self):
        self.ayudanteInorden(self.raiz)
    def ayudanteInorden(self, nodo: NodoArbol):
        if (nodo == None):
            return
        self.ayudanteInorden(nodo.nodoIzq)
        print(nodo.dato, end=" ")
        self.ayudanteInorden(nodo.nodoDer)
    def recorridoPostorden(self):
        self.ayudantePostorden(self.raiz)
    def ayudantePostorden(self, nodo:NodoArbol):
        if (nodo == None):
            return
        self.ayudantePostorden(nodo.nodoIzq)
        self.ayudantePostorden(nodo.nodoDer)
        print(nodo.dato, end=" ")

arbol = Arbol()
arbol.insertarNodo(10)
arbol.insertarNodo(2)
arbol.insertarNodo(40)
arbol.insertarNodo(13)
arbol.insertarNodo(18)

arbol.recorridoPreorden()
print()
arbol.recorridoInorden()
print()
arbol.recorridoPostorden()



