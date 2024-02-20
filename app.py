from flask import Flask, render_template, request, Response
import os
from libs.pixadd import create_cob, get_cob
from dotenv import dotenv_values
import random
import time

app = Flask(__name__)
app.template_folder = os.getcwd() + '\\ad\\tamplante' 
app.static_folder   = os.getcwd() + '\\ad\\static'
@app.route('/')

def home():
   return render_template('page.html')

@app.route('/cheking')
def show_post():
   try:
         
      hora     = int(request.args.get('hours'))
      minutos  = int(request.args.get('min'))
      segundos = int(request.args.get('seg'))
   except TypeError:
      hora     = 00
      minutos  = 00
      segundos = 00 

   totalseg = hora * 3600 + minutos * 60 + segundos
   total_pagar = totalseg / 15 # 60 seg valeria 4 reales
   total_pagar = '%.2f' % float(total_pagar) 
   return render_template('cheking.html', 
                          time="{:02d}:{:02d}:{:02d}".format(
                                 int(hora), int(minutos), int(segundos)),
                          total=total_pagar  )
@app.route('/btn')
def button():
   return render_template('btn.html')


@app.route('/pix/<int:total>')
def pix(total):
   config = dotenv_values(".env")
   appid = config['APP_ID']
   '''
  
   pix = create_cob(appid, total, cometdv='')
   cob = get_cob(appid, pix[1])
  
   print(pix)
   print(cob)
   try:
      img = cob['charge']['qrCodeImage']

   except KeyError:
      error = cob['error']
      return  render_template('pix.html', e=error)
   
   '''
   img = 'https://api.openpix.com.br/openpix/charge/brcode/image/89570613-ef43-4ea5-8628-73212e1f28d1.png'
   print('%.2f' % float(total))
   return render_template('pix.html', total_pagar='%.2f' % float(total), 
                           img=img)

@app.route('/timer')
def timer():
    # show the subpath after /path/
    return render_template('timer.html')

@app.route('/carton')
def index():
    return render_template('carton.html')

@app.route('/stream')
def stream():
    def generate_data():
        while True:
            data = str(random.randint(0, 100))  # Genera datos aleatorios
            yield 'data: {}\n\n'.format(data)
            time.sleep(1)  # Espera 1 segundo antes de generar el próximo dato

    return Response(generate_data(), mimetype='text/event-stream', headers={'Cache-Control': 'no-cache'})
