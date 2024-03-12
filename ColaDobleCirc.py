#La actividad es colas doblemente circular hacer el programa donde se inserte y
# eliminé un elemento, además de mostrar cada movimiento ya sea inserción o
# eliminación.
import os
os.system('cls' if os.name == 'nt' else 'clear')

class ColaDoble:
    def __init__(self):
        self.elementos = []

    def encolarFrente(self, item):
        self.elementos.append(item)

    def encolarFinal(self, item):
        self.elementos.insert(0, item)

    def desencolarFrente(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            raise IndexError("desencolar de una cola vacía.")

    def desencolarFinal(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
            print('Primer elemento eliminado.')
        else:
            raise IndexError("desencolar de una cola vacía.")

    def esta_vacia(self):
        return len(self.elementos) == 0

cola = ColaDoble()
cola.encolarFrente('elemento1')
cola.encolarFrente('elemento2')
cola.encolarFinal('elemento3')
cola.encolarFinal('elemento4')
#eliminara
print("Elemento desencolado", cola.desencolarFrente())
print("Elemento desencolado", cola.desencolarFinal())
