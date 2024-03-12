class Grafo:
    def __init__(self):
        self.vertices = {} #Elementos individuales del grafo
        self.aristas = [] #Son las conexiones entre los vertices

# Este va agregar un vértice al grafo si no existe previamente
# y se va guardar en un nombre espcial y almacenara en una coordenada
    def agregar_vertice(self, vertice, x, y):
        if vertice not in self.vertices:
            self.vertices[vertice] = (x, y)

# Agregara una arista al grafof entre dos vertices, que se identificaran
#como vertice1 y vertice2. Pero para esto los dos vertices se deben de encontrar en self.vertice
    def agregar_arista(self, vertice1, vertice2): #va pedir el nombre de los dos vertices
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.aristas.append((vertice1, vertice2))

    def generar_matriz_adyacencia(self):
        vertices = list(self.vertices.keys())
        n = len(vertices)
        matriz = [[0] * n for _ in range(n)]

        for v1, v2 in self.aristas:
            i = vertices.index(v1)
            j = vertices.index(v2)
            matriz[i][j] = 1
            matriz[j][i] = 1

        return matriz

    def generar_html(self):
        html = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Grafo</title>
<style>
    #lienzo {
        position: relative;
        width: 500px;
        height: 500px;
        border: 1px solid black;
    }
    .vertice {
        position: absolute;
        width: 30px;
        height: 30px;
        border: 2px solid black;
        border-radius: 50%;
        background-color: #3498db;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
</head>
<body>

<div id="lienzo">"""

        # Agregar los vértices como círculos
        for vertice, (x, y) in self.vertices.items():
            html += f"<div class='vertice' style='left: {x}px; top: {y}px;'></div>\n"

        # Agregar las aristas como líneas
        for arista in self.aristas:
            pos1 = self.vertices[arista[0]]
            pos2 = self.vertices[arista[1]]
            html += f"<svg style='position: absolute; z-index: -1; stroke:black; stroke-width: 2px;'><line x1='{pos1[0] + 20}px' y1='{pos1[1] + 20}px'/></svg>"
            html += f"<svg style='position: absolute; z-index: -1; stroke:black; stroke-width: 2px;'><line x2='{pos2[0] + 10}px' y2='{pos2[1] + 10}px'/></svg>"
        html += """</div>

</body>
</html>"""
        return html

# Ejemplo de uso
grafo = Grafo()
#Para invocar al metodo se le debe asignar un nombre especial y valores a sus coordenadas
grafo.agregar_vertice("A", 100, 100)
grafo.agregar_vertice("B", 200, 200)
grafo.agregar_vertice("C", 300, 300)

#
grafo.agregar_arista("A", "B")
grafo.agregar_arista("B", "C")
grafo.agregar_arista("C", "A")

matriz = grafo.generar_matriz_adyacencia()

# Imprimir matriz de adyacencia
for fila in matriz:
    print(fila)

# Escribir el HTML en un archivo
with open("grafo.html", "w") as file:
    file.write(grafo.generar_html())
