class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, origen, destino):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].append(destino)
            self.vertices[destino].append(origen)

    def obtener_vertices(self):
        return list(self.vertices.keys())

    def obtener_aristas(self):
        aristas = []
        for vertice, adyacentes in self.vertices.items():
            for adyacente in adyacentes:
                aristas.append((vertice, adyacente))
        return aristas

    ddef generar_html(self):
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
        width: 20px;
        height: 20px;
        border: 2px solid black;
        border-radius: 50%;
        background-color: #3498db;
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
            html += f"<svg style='position: absolute;'><line x1='{pos1[0] + 10}px' y1='{pos1[1] + 10}px' x2='{pos2[0] + 10}px' y2='{pos2[1] + 10}px' style='stroke:black;'/></svg>\n"

        html += """</div>

</body>
</html>"""
        return html

grafo = Grafo()

grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")

grafo.agregar_arista("A", "B")
grafo.agregar_arista("B", "C")
grafo.agregar_arista("C", "A")

vertices = grafo.obtener_vertices()
print("Vertices: ", vertices)

aristas = grafo.obtener_aristas()
print("Aristas: ", aristas)
