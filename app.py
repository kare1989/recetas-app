from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
import os

app = Flask(__name__)

# Rutas para PWA: servir manifest.json y sw.js desde la raíz con send_file y ruta absoluta
@app.route('/manifest.json')
def manifest():
    return send_file(os.path.join(app.root_path, 'static', 'manifest.json'))

@app.route('/sw.js')
def service_worker():
    return send_file(os.path.join(app.root_path, 'static', 'sw.js'))

# Datos de ejemplo: lista de recetas (en un proyecto real podrías usar DB)
RECIPES = [
    {
        "id": 1,
        "title": "Crema Volteada",
        "ingredients": {
            "Caramelo": [
                "600 g azúcar blanca",
                "200 g agua",
                "1 limón",
                "3 huevos",
                "100 g harina"
            ],
            "Para la crema": [
                "2 tarros de leche",
                "2 leches condensada",
                "1 l agua",
                "90 g azúcar blanca",
                "1600 g huevo",
                "1/2 tapa de vainilla"
            ]
        },
        "steps": [
            "Agregar todos los ingredientes pesados a una olla en fuego para el caramelo",
            "Luego agregar el caramelo a los moldes y dejar enfriar",
            "En un bowl primero pesar los huevos y azúcar para luego batir hasta que se mezcle bien",
            "Después agregar los demás ingredientes y batir bien",
            "Hornear 70 min a 180°C"
        ],
        "image": "/static/images/crema volt.jpg"
    },
    {
        "id": 2,
        "title": "Keke de Zanahoria con Piña y Pecanas",
        "ingredients": {
            "Relleno": [
                "80 g pecanas",
                "420 g zanahoria",
                "500 g azúcar rubia",
                "6 huevos",
                "12 g bicarbonato",
                "1 cdta canela en polvo",
                "480 g harina pastelera",
                "330 g aceite",
                "100 g piña",
                "30 g coco rayado",
            ]
        },
        "steps": [
            "En un bowl pesar el huevo y azúcar, batir hasta que este cremoso.",
            "Luego echar el aceite hasta que se mezcle bien (empieza en velocidad 3 y termina en 7 por 1 minuto).",
            "Por último agregar todo lo seco hasta que se integre bien todo por 1 minuto (no batir mucho).",
            "Hornear 60 min en la temperatura programada."
        ],
        "image": "/static/images/Keke zanahoria.jpg"
    }
]

def get_next_id():
    return max([r['id'] for r in RECIPES], default=0) + 1

@app.route('/')
def index():
    return render_template('index.html', recipes=RECIPES)

@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    r = next((x for x in RECIPES if x['id'] == recipe_id), None)
    if not r:
        return "Receta no encontrada", 404
    return render_template('recipe.html', recipe=r)

# API para agregar receta (simple, desde formulario)
@app.route('/add', methods=['POST'])
def add_recipe():
    title = request.form.get('title')
    ingredients = request.form.get('ingredients', '').split('\n')
    steps = request.form.get('steps', '').split('\n')
    image = request.form.get('image', '')
    new = {
        'id': get_next_id(),
        'title': title,
        'ingredients': [i.strip() for i in ingredients if i.strip()],
        'steps': [s.strip() for s in steps if s.strip()],
        'image': image or '/static/images/default.jpg'
    }
    RECIPES.append(new)
    return redirect(url_for('index'))

# API JSON (útil para futuras apps móviles o exportar)
@app.route('/api/recipes')
def api_recipes():
    return jsonify(RECIPES)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
