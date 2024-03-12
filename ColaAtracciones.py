import os
os.system('cls' if os.name == 'nt' else 'clear')

class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            raise IndexError("desencolar de una cola vacía")

    def esta_vacia(self):
        return len(self.elementos) == 0

#Uso de la Cola
cola = Cola()
#cola.encolar('elemento1')
print("Bienvenido al parque de atracciones!!!")
num = int(input("Numero de visitantes: \n"))

for i in range(num):
    nombre = input("Nombre: \n")
    especial = input("¿Eres especial o compraste tu entrada antes?\t")

    if especial== "Si" or especial=="si"or especial=="SI":
        cola.encolar(nombre)
        print("Bienvenido disfrute las atracciones\n")
        print("Elemento desencolado", cola.desencolar())

    elif especial=="No" or especial=="NO" or especial=="no":
            print("Tendras que esperar\n")
            cola.encolar(nombre)
    else:
        print("Tienes que responder si o no\n")

print("Elemento desencolado", cola.desencolar())
