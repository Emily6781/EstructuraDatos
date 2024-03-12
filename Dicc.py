from flask import Flask, request, render_template_string
import os
from fpdf import FPDF
os.system('cls' if os.name == 'nt' else 'clear')
app = Flask(__name__)

# Paso 1: Definir las ventas y los productos
productos = {
    "Leche": 20.00,
    "Pan": 10.00,
    "Refresco": 15.00,
    "Galletas": 5.00,
    "Agua": 8.00,
    "Jugo": 12.00,
    "Chips": 18.00,
    "Chocolate": 25.00,
}

def generar_pdf(elementos_selec):
    pdf = FPDF(orientation = 'P', unit = 'mm', format= 'A4')
    pdf.text(x= 60, y=50, txt = elementos_selec)
    pdf.output('C:/ed2024/hoja.pdf')

def calcular_total(productos_vendidos):
    return sum(productos[prod] for prod in productos_vendidos)

def generar_html(productos, mensaje="", articulo1="", total_venta=0, cambio=0):
    html = "<html><title>Diccionario python</title><body><h1>Lista de Productos</h1><table border='1'><tr><th>articulos</th><th>precio</th></tr>"
    for articulos, precio in productos.items():
        html += f"<tr><td>{articulos}</td><td>{precio}</td></tr>"
    html += "</table>"
    html += "<form method='post'><label for='elemento'>Articulo a Seleccionar:</label>"
    html += "<input type='text' id='elemento' name='elemento' required>"
    html += "<input type='submit' value='Buscar'></form>"
    if mensaje:
        html += f"<p>{mensaje}</p>"
    if elementos_selec:
        html += "<h2>Elementos Seleccionados:</h2>"
        html += "<ul>"
        for elemento in elementos_selec:
            html += f"<li>{elemento}</li>"
        html += "</ul>"
        html += f"<p>Total de la venta: ${total_venta}</p>"
        html += "<form method='post'><label for='cuenta'><input type='number' id='cuenta' name='cuenta' required>"
        html += "<input type='submit' value='Calcular'></form>"
        if cambio:
            html += f"<p>{cambio}</p>"
            generar_pdf(elementos_selec)
    html += "</body></html>"
    return html

elementos_selec = []

def buscar_y_cambio() :
    mensaje = " "
    articulo1 = ""
    total_venta = 0
    cambio = 0
    if request.method == 'POST':
        elemento_buscar = request.form.get('elemento', type=str)
        if not elemento_buscar:
            mensaje = "Por favor, ingrese un artículo."

        elif elemento_buscar in productos:
            elementos_selec.append(elemento_buscar)
            total_venta = calcular_total(elementos_selec)
            mensaje = "Elemento guardado"
            return generar_html(productos, mensaje, elementos_selec, total_venta)

            cantidad_pagada = request.form.get('cantidad', type=int)
            if cantidad_pagada is None:
                mensaje = "Por favor, ingrese una cantidad."
                return generar_html(productos, mensaje, elementos_selec, total_venta)

            elif cantidad_pagada < total_venta:
                mensaje = "Cantidad insuficiente para completar la compra."
                return generar_html(productos, mensaje, elementos_selec, total_venta)

            else:
                cambio = cantidad_pagada - total_venta
                mensaje = "Compra realizada con éxito."
                return generar_html( productos, elementos_selec,total_venta, cambio, mensaje)

        else:
            mensaje = "El artículo no está en la lista."

    return generar_html(productos, mensaje, elementos_selec, total_venta, cambio)

@app.route('/', methods=['GET', 'POST'])
def mostrar_compra():
    if request.method == 'POST':
        html = buscar_y_cambio()
    else:
        html = generar_html(productos)
    return render_template_string(html)

# Paso 3 y 4: Iniciar servidor y visualizar en navegador
if __name__ == '__main__':
    app.run(debug=True, port=56440)
