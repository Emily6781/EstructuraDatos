from flask import Flask, request, render_template_string
import os
from fpdf import FPDF
#os.system('cls' if os.name == 'nt' else 'clear')
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

def calcular_total(productos_vendidos):
    return sum(productos[prod] for prod in productos_vendidos)

def generar_html(productos, mensaje="", articulo1="", total_venta=0, cambio=0):
    #Código para generar_pdf, se declara la variable con la libreria FPDF con la orientacion horintozal
    pdf = FPDF(orientation = 'P', unit = 'mm', format= 'A4')
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    html = "<html><title>Diccionario python</title><body><h1>Lista de Productos</h1><table><tr><th>articulos</th><th>precio</th></tr>"
    html += "<style>"
    html += "    *{  margin: auto;  padding: 10px; background-color: black; }"
    html += "body{font-family: 'Itim', cursive;font-size: 20px;  color: white;  width: 90%;  text-align: center;  display: flex; border-color: white; display: flex;flex-direction: column;} "
    html += "tr{  width: 10px;  margin: 5px;  height: 20;  border: 10px;  color: #b983ff;  font-family: 'Dancing Script', cursive;  padding: 10px;  margin-bottom: 5px;  border-radius: 10px;  background-color: #cab8ff;} "
    html += "p{  font-family: 'Itim', cursive;  font-size: 10px;  color: white; }"
    html += "button{  background: linear-gradient(#9a63ff, #7940ff);   border: 0;  color: white;  opacity: 0.6;  cursor: pointer;  border-radius: 50px; width: 100px;  height: 100px;  font-size: 20px;  }"
    html += "input {color: white; border-radius: 50px;}"
    html += "    }"
    html += "</style>"
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
        pdf.text(10, 10, 'Recivo de compra.')
        pdf.text(10, 15, '------------------------------------')
        for elemento in elementos_selec:
            html += f"<li>{elemento}</li>"
            #w= ancho, H= alto, txt: lo va ir dentro del archivo, borde derecho, alinear al centro
            pdf.multi_cell(w= 40, h= 20, txt= elemento, border = 'R', align= 'C', fill= False)
        html += "</ul>"
        html += f"<p>Total de la venta: ${total_venta}</p>"
        total = str(total_venta)
        pdf.text(10, 100, 'Total de venta: ' + total+ '\n')
        pdf.output('C:/ed2024/Rec.pdf')
        html += "<input type='number' id='pagado' placeholder='Cantidad pagada'>"
        html += "<button onclick='CalcularCambio()'>Calcular Cambio</button>"
        html += "<script>"
        html += "function CalcularCambio() {"
        html +=f" let total = {total_venta}; "
        html += "let pagado = document.getElementById('pagado').value;"
        html += "pagado = parseFloat(pagado);"
        html += "if (pagado < total) {"
        html += "alert('Cantidad insuficiente para pagar.');"
        html += "return;}"
        html += "let cambio = pagado - total;"
        html += "alert(cambio);"
        html += "document.getElementById('cambio').innerText = 'Cambio: $' + cambio.toFixed(2);}"
        html += "</script>"

    html += "</body></html>"
    return html

elementos_selec = []

def buscar_y_cambio() :
    mensaje = " "
    articulo1 = ""
    total_venta = 0
    if request.method == 'POST':
        elemento_buscar = request.form.get('elemento', type=str)
        if not elemento_buscar:
            mensaje = "Por favor, ingrese un artículo."

        elif elemento_buscar in productos:
            elementos_selec.append(elemento_buscar)
            total_venta = calcular_total(elementos_selec)
            mensaje = "Elemento guardado"
            return generar_html(productos, mensaje, elementos_selec, total_venta)
        else:
            mensaje = "El artículo no está en la lista."

    return generar_html(productos, mensaje, elementos_selec, total_venta)

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
