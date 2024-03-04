from flask import Flask, render_template, request, Response, abort
import os
from os import path
from libs.pixadd import create_cob, get_cob
from dotenv import dotenv_values
import random
import time

print(os.chdir(os.getcwd()))

app = Flask(__name__)
app.template_folder = os.getcwd() + r'/tamplante' 
app.static_folder   = os.getcwd() + r'/static'
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
   total_pagar = totalseg // 40 # 60 seg valeria 1,5 reales
   print(total_pagar)
   total_pagar = '%.2f' % float(total_pagar) 

   if total_pagar != '0.00':
      return render_template('cheking.html', 
                          time="{:02d}:{:02d}:{:02d}".format(
                          int(hora), int(minutos), int(segundos)),
                          total=total_pagar  )
   
   abort(404)
@app.route('/btn')
def button():
   return render_template('btn.html')


@app.route('/pix/<total>')
def pix(total):

   if total != '0.00':
      if path.exists(".env"):   
         config = dotenv_values(".env")
         appid = config['APP_ID']
         
         pix = create_cob(appid, total, cometdv='')
         cob = get_cob(appid, pix[1])
      
         print(pix)
         print(cob)
         try:
            img = cob['charge']['qrCodeImage']

         except KeyError:
            error = cob['error']
            return  render_template('pix.html', e=error)
         return render_template('pix.html', total_pagar='%.2f' % float(total), 
                              img=img,
                              ID=cob['charge']['correlationID'])
      abort(500)      
   abort(404)


@app.route('/timer')
def timer():
    # show the subpath after /path/
    return render_template('timer.html')

@app.route('/carton')
def index():
    return render_template('carton.html')

@app.route('/pixcheck/<idPix>')
def pixcheck(idPix):
    def generate_data():
        config = dotenv_values(".env")
        appid  = config['APP_ID']
        while True:
            ultima_trastion = get_cob(appid, idPix)
            status = ultima_trastion['charge']['status']  # Genera datos aleatorios

            yield 'data: {}\n\n'.format(status)
            time.sleep(2)  # Espera 1 segundo antes de generar el próximo dato

    return Response(generate_data(), mimetype='text/event-stream', headers={'Cache-Control': 'no-cache'})

@app.errorhandler(404)
def not_found(e):
  return render_template('error.html', num='2'), 404
  
@app.errorhandler(500)
def internal_server(e):
  print(e)
  return render_template('error.html', num='3'), 500

@app.route('/pixdebug')
def debug():
   import json
   if path.exists(".env"):
         
      config = dotenv_values(".env")
      appid  = config['APP_ID']
         
      pix = create_cob(appid, '100', cometdv='test value')
      cob = get_cob(appid, pix[1])

      print(pix)
      print(cob)
      return json.dumps(cob)
   abort(500)

