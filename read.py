from flask import Flask, Response, render_template
import time
import random

app = Flask(__name__, template_folder='./')

if __name__ == '__main__':
    app.run(debug=True)
