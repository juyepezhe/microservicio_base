from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Microservicio activo'})

@app.route('/api/sumar', methods=['POST'])
def sumar():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({'error': 'Parámetros a y b requeridos'}), 400
    return jsonify({'resultado': a + b})

@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({
        'autor': 'Equipo X',
        'version': '1.0',
        'descripcion': 'Microservicio de ejemplo para clases de cloud, APIs y Docker.'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')