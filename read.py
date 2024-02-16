from flask import Flask, Response, render_template
import time
import random

app = Flask(__name__, template_folder='./')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    def generate_data():
        while True:
            data = str(random.randint(0, 100))  # Genera datos aleatorios
            yield 'data: {}\n\n'.format(data)
            time.sleep(0.1)  # Espera 1 segundo antes de generar el próximo dato

    return Response(generate_data(), mimetype='text/event-stream', headers={'Cache-Control': 'no-cache'})

if __name__ == '__main__':
    app.run(debug=True)
