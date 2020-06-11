#Lo primero de todo es importar la libreria flask

try:

    from flask import Flask, jsonify, request

    tienda = Flask(__name__)

    #Importar la lista de juegos:

    from Productos import Productos

    #Pedir la lista de juegos

    @tienda.route('/Juegos')
    def Lista():
        return jsonify({"Juegos": Productos, "Mensaje": "Lista de juegos."})

    #Pedir un juego en concreto

    @tienda.route('/Juegos/<string:nombre_producto>')
    def producto(nombre_producto):
        producto_encontrado = [producto for producto in Productos if producto['Nombre'] == nombre_producto]
        if (len(producto_encontrado) > 0):
            return jsonify({"Juego": producto_encontrado[0]})
        else:
            return jsonify({"message": "Juego no encontrado."})

    #Añadir un juego

    @tienda.route('/Juegos', methods = ['POST'])
    def AgregarProducto():
        nuevo_producto = {
            "Nombre": request.json['Nombre'],
            "Precio(€)": request.json['Precio(€)'],
            "Categoria": request.json['Categoria'],
            "Fecha_Salida": request.json['Fecha_Salida'],
            "En Stock": request.json['En Stock']
        }
        Productos.append(nuevo_producto)
        return jsonify({"Mensaje": "Añadido correctamente.", "Nueva lista de juegos": Productos})

    #Actualizar un producto

    @tienda.route('/Juegos/<string:nombre_producto>', methods = ['PUT'])
    def ActualizarProducto(nombre_producto):
        producto_encontrado = [producto for producto in Productos if producto['Nombre'] == nombre_producto]
        if (len(producto_encontrado) > 0):
            producto_encontrado[0]['Nombre'] = request.json['Nombre']
            producto_encontrado[0]['Precio(€)'] = request.json['Precio(€)']
            producto_encontrado[0]['Categoria'] = request.json['Categoria']
            producto_encontrado[0]['Fecha_Salida'] = request.json['Fecha_Salida']
            producto_encontrado[0]['En Stock'] = request.json['En Stock']
            return jsonify({
                "Mensaje": "Juego correctamente actualizado.",
                "Nueva lista de juegos": producto_encontrado[0]
            })
        else:
            return jsonify({"Mensaje": "Producto no encontrado."})

    #Eliminar productos

    @tienda.route('/Juegos/<string:nombre_producto>', methods = ['DELETE'])
    def EliminarProducto(nombre_producto):
        producto_encontrado = [producto for producto in Productos if producto['Nombre'] == nombre_producto]
        if (len(producto_encontrado) > 0):
            Productos.remove(producto_encontrado[0])
            return jsonify({
                "Mensaje": "Juego eliminado.",
                "Nueva lista de juegos": Productos
            })
        else:
            return jsonify({"Mensaje": "Juego no encontrado."})



    #Ahora vamos a ejecutar nuestro servidor:

    if __name__ == '__main__':
        tienda.run(debug=True, port=4000)



except:
    print("Ha courrido un error.")

finally:
    print("Hasta luego.")



