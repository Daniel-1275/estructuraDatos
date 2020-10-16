from Listas import ListaEnlazada
class Cola:
    def __init__(self):
        self.lista = ListaEnlazada()
    def encolar(self, dato):
        self.lista.insertarUltimo(dato)
    def encolarEnOrden(self, dato):
        if (self.lista.estaVacio()):
            self.encolar(dato)
        else:
            actual = self.lista.primero
            while actual:
                datoActual = actual.dato
                if (dato >= datoActual):
                    self.lista.insertar(dato, self.find(datoActual))
                    break
                actual = actual.siguiente
            if (not actual):
                self.encolar(dato)

    def desencolar(self):
        return self.lista.removerPrincipio()
    def find(self, dato):
        actual = self.lista.primero
        c = 0
        while actual:
            if (dato == actual.dato):
                return c
            c += 1
            actual = actual.siguiente

        return - 1
    def datos(self):
        actual = self.lista.primero
        listaDatos = []
        while actual:
            listaDatos.append(actual.dato)
            actual = actual.siguiente
        return listaDatos
    def set(self, pos, dato):
        if (pos < 0 or pos >= self.lista.len):
            raise IndexError('Fuera de rango')
        else:
            actual = self.lista.primero
            i = 0
            while i != pos:
                actual = actual.siguiente
                i += 1
            actual.dato = dato
    def __str__(self):
        return str(self.lista)
    def __len__(self):
        return self.lista.len
    
cola = Cola()
n = int(input())
for x in range(n):
    r = int(input())
    cola.encolarEnOrden(r)
print(cola)

print(cola.datos())

"""
print("La cola esta vacía")

print("Ingresando")
for x in range(1, 10):
    cola.encolar(x)
    print("Enqueue", x)
    print(cola)


print("Removiendo")
while len(cola) != 0:
    print("Dequeue", cola.desencolar())
    print(cola)

print("La cola esta vacía")
"""