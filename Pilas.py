from Listas import ListaEnlazada

class Pila:
    def __init__(self):
        self.lista = ListaEnlazada()
    def push(self, dato):
        self.lista.insertarPrincipio(dato)
    def pop(self):
        return self.lista.removerPrincipio()
    def __len__(self):
        return self.lista.len
    def __str__(self):
        return str(self.lista)


pila = Pila()
print("La pila esta vacía")

print("Ingresando Datos")
for x in range(1, 10):
    pila.push(x)
    print("Se ingreso", x)
    print(pila)

print("Eliminando datos")
while len(pila) != 0:
    print("Se elimino", pila.pop())
    print(pila)

print("La pila esta vacía")


