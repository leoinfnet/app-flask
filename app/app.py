from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message='Hello, World5!')

@app.route('/status')
def status():
    return jsonify(status='running')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)

