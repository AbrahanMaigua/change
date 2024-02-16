from flask import Flask, render_template, request
import json
import os
app = Flask(__name__)
app.template_folder = os.getcwd() + '\\tamplante' 
app.static_folder   = os.getcwd() + '\\static'
@app.route('/')

def home():
   return render_template('page.html')

@app.route('/cheking')
def show_post():
   hora     = request.args.get('hours')
   minutos  = request.args.get('min')
   segundos = request.args.get('seg')
   
   totalseg = hora * 3600 + minutos * 60 + segundos
   total_pagar = totalseg / 15 # 60 seg valeria 4 reales 
   return render_template('cheking.html', time=f'{hora}:{minutos}:{segundos}',
                                          total=total_pagar  )


@app.pix('/pix/<int:total>')
def pix(total):
   return render_template('pix.html', total_pagar=total)

@app.route('/timer')
def timer():
    # show the subpath after /path/
    return render_template('timer.html')

