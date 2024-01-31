from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    with open('url.txt', 'r') as file:
        url = file.read().splitlines()
    size = len(url)
    
    data = {'url': f'{url[random.randrange(0, size)]}'}
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)