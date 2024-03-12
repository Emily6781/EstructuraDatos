#arboles binarios mostrados en html
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
#este metodo va serivir para detectara que si no hay un valor ponerlo
#debajo del que esta si lo hay es cuando va invocar el metodo insertar recusivo
    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar_recursivo(dato, self.raiz)
#cuadno apuntamos al nodo o asi moismo se debe de usar una letra minuscula
#aquí cuando detecta que un numero si es menor o myor y dependeindo de eso
#se va ir a la izquierda o la derecha, basica caracteristica de los arboles
    def _insertar_recursivo(self, dato, nodo):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._insertar_recursivo(dato, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._insertar_recursivo(dato, nodo.derecha)
#esto se va aplicar para representar el arbol mediante niveles e invocando el
#metodo representar recusivo para regresar niveles
    def representar(self):
        niveles = []
        self._representar_recursivo(self.raiz, 0, niveles)
        return niveles
#Es la candtidad de niveles más 1 para agregar y como se guardo en el
#metodo representar, ya sea izquierda o derecha lo va guardar así en niveles
    def _representar_recursivo(self, nodo, nivel, niveles):
        if nodo is not None:
            if len(niveles) < nivel + 1:
                niveles.append([])
            niveles[nivel].append(nodo.dato)
            self._representar_recursivo(nodo.izquierda, nivel + 1, niveles)
            self._representar_recursivo(nodo.derecha, nivel + 1, niveles)
#Aquí es cuando declaramos un elemento arbol binario, le asignamos datos de una
#vez con los cuales se van a utilizar en la iteración que viene
arbol = ArbolBinario()
datos =  [2, 10, 1, 0, 0, 2, 3, 8, 10, 2, 3]
for d in datos:

    arbol.insertar(d)

niveles = arbol.representar()
#Esto para representar en código de html
html_niveles = "".join([f"<li>{''.join(map(str, nivel))}</li>" for nivel in niveles])
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Arbol Binario</title>
    <style>
        *{{
            margin: 45px;
            padding: auto;
            box-sizing: border-box;
        }}
        body{{
            background-color: black;
            text-align: center;
            font-family: 'Itim', cursive;
            top: 50%;
            left: 50%;
            border: 1px solid rgba(0,0,0,0,2);
        }}
        h2{{
            font-family: 'Dancing Script', cursive;
            color:  #52D7FE;
        }}

        .arbol-binario ul{{
            position: center;
            justify-content: center;
            aling-items: center;
            list-style-type: none;
            padding: 20px;
            text-align: center;
            font-family: 'Roboto', sans-serif;
            border-radius: 10px;
            background-color: #47FF7C;
            width: 300px;

            -webkit-box-shadow: 6px 5px 24px #D3CECE;
            -moz-box-shadow: 6px 5px 24px #D3CECE;
            box-shadow: 6px 5px 24px #666666;
            -webkit-border-radius: 28;
            -moz-border-radius: 28;
        }}
        .arbol-binario ul{{
            margin: 0 auto;
            padding: 20px;

        }}
    </style>
</head>
<body>
    <h2>Árbol Binario</h2>
    <div class= "arbol-binario">
        <ul>
            {html_niveles}
        </ul>
    </div>
</body>
</html>
"""
#esto va hacer que al crear el arcivo html se va guardar con el respectivo nombre
#que le asignemos
file_name = "arbol_binario.html"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(html_content)

import webbrowser
import os
