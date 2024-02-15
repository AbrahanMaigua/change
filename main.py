from flask import Flask, render_template, request
import json
import os
app = Flask(__name__)
app.template_folder = os.getcwd() + '\\tamplante' 

@app.route('/')
def home():
    # show the user profile for that user
    return f'page 1'

@app.route('/post')
def show_post():
   hora     = request.args.get('hora')
   minutos  = request.args.get('min')
   segundos = request.args.get('seg')

   return render_template('cheking.html', hora=hora,
                                           min=minutos,
                                           seg=segundos)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f''