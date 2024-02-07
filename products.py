from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de artículos de vehículos
articles = [
    {"id": 1, "name": "Llantas Michelin", "description": "Juego de llantas para automóvil", "image": "llantas_michelin.jpg", "price": 400},
    {"id": 2, "name": "Faros LED", "description": "Faros LED para camioneta todo terreno", "image": "faros_led.jpg", "price": 600},
    {"id": 3, "name": "Asientos de Cuero", "description": "Asientos de cuero genuino para automóvil", "image": "asientos_cuero.jpg", "price": 800},
    {"id": 4, "name": "Radio Touchscreen", "description": "Sistema de entretenimiento con pantalla táctil", "image": "radio_touchscreen.jpg", "price": 500}
]

# Obtener todos los artículos
@app.route('/articles', methods=['GET'])
def get_articles():
    return jsonify(articles)

# Obtener un artículo por su ID
@app.route('/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
    article = next((article for article in articles if article["id"] == article_id), None)
    if article:
        return jsonify(article)
    return jsonify({"error": "Artículo no encontrado"}), 404

# Agregar un nuevo artículo
@app.route('/articles', methods=['POST'])
def add_article():
    new_article = request.json
    required_fields = ["name", "description", "image", "price"]
    if all(field in new_article for field in required_fields):
        new_article["id"] = len(articles) + 1
        articles.append(new_article)
        return jsonify({"message": "Artículo agregado correctamente", "article": new_article}), 201
    return jsonify({"error": "Se requieren los campos 'name', 'description', 'image' y 'price' en el cuerpo de la solicitud"}), 400

if __name__ == '__main__':
    app.run(debug=True)
