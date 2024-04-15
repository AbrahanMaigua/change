from flask import Flask, render_template, request, Response, abort, redirect, url_for
from os import path, getcwd, chdir
from libs.pixadd import create_cob, get_cob
from libs.db import *
from dotenv import dotenv_values
from datetime import datetime
from time import sleep
from libs.relay.acrive import *

app = Flask(__name__)

#chdir('home/kuro/change')
app.template_folder = getcwd() + r'/tamplante' 
app.static_folder   = getcwd() + r'/static'
print(app.static_folder ,
      app.template_folder)

@app.route('/')
def home():
   pedido_id = ultimo_registro()
   if pedido_id != None:
      registro = view_pedido(pedido_id) 
      print(registro)
      if registro[-4] == False and registro[-5] == True  :
         return redirect(url_for('timer', 
                                 pedido_id=registro[0],
                                 startauto='true'))
         

   return render_template('page.html')

@app.route('/btn')
def button():
   return render_template('btn.html')

@app.route('/carton')
def carton():
    return render_template('carton.html', img='nfc.jpg')

@app.route('/timer/<int:pedido_id>')
def timer(pedido_id):
      start = request.args.get('startauto')
      print(start)
      info = view_pedido(pedido_id)
      print(info)
      return render_template('timer.html', Time=info[-3])


@app.route('/cheking')
def show_post():
   date = datetime.now()
   # ['%d/%m/%Y,  %H:%M:%S']
   date_row = date.strftime('%d/%m/%Y %H:%M:%S').split(' ')

   try:
      hora     = int(request.args.get('hours'))
      minutos  = int(request.args.get('min'))
      segundos = int(request.args.get('seg'))
   except TypeError:
      hora     = 00
      minutos  = 00
      segundos = 00 
   
   carga = "{:02d}:{:02d}:{:02d}".format(
                          int(hora), int(minutos), int(segundos))

   totalseg = hora * 3600 + minutos * 60 + segundos
   total_pagar = totalseg / 40 # 60 seg valeria 1,5 reales
   total_pagar = '%.2f' % float(total_pagar) 
   # save pedido
   create_pedido(date_row[0],date_row[1], carga, totalseg, total_pagar)
   pedido_id = ultimo_registro()

   if total_pagar != '0':
      return render_template('cheking.html', 
                             time=carga,
                             total=total_pagar,
                             pedido_id=pedido_id[0][0] )
   
   abort(404)

@app.route('/pix/<pedido_id>')
def pix(pedido_id):
   pedido = view_pedido(pedido_id)
   print(pedido)

   total  = str(pedido[-2]).replace(',', '')
   print(total)

   if total != '0.00':
      print(pedido)
      if path.exists(".env"):   
         config = dotenv_values(".env")
         appid = config['APP_ID']
         pix = (0,pedido[1])
         if pix[1] == None:
            pix = create_cob(appid, total, cometdv='')
            add_pix_id(pedido_id, pix[1])
         print(pix)
         cob = get_cob(appid, pix[1])
         print(cob)
      

         try:
            img = cob['charge']['qrCodeImage']

         except KeyError:
            error = cob['error']
            return  render_template('pix.html', e=error)
         return render_template('pix.html', total_pagar='%.2f' % float(total), 
                              img=img,
                              ID=cob['charge']['correlationID'],
                              pedido_id=pedido_id)
      abort(500)      
   abort(404)

# server APi
@app.route('/pixcheck/<idPix>')
def pixcheck(idPix):
    def generate_data():
        config = dotenv_values(".env")
        appid  = config['APP_ID']
        while True:
            ultima_trastion = get_cob(appid, idPix)
            status = ultima_trastion['charge']['status']  
            if status != 'ACTIVE':
               update_value('status_pagamento',True,'pedido_id = {idPix}')
            yield 'data: {}\n\n'.format(status)
            sleep(2)  # Espera 2 segundo antes de generar el próximo dato

    return Response(generate_data(), mimetype='text/event-stream', headers={'Cache-Control': 'no-cache'})

@app.route('/complete')
def completestatus():
   def tiempo_a_segundos(tiempo):
      horas, minutos, segundos = tiempo.split(':')
      total_segundos = int(horas) * 3600 + int(minutos) * 60 + int(segundos)
      return total_segundos
   
   def formatear_tiempo(segundos):
      horas = segundos // 3600
      minutos = (segundos % 3600) // 60
      segundos_restantes = segundos % 60
      return f"{pad(horas)}:{pad(minutos)}:{pad(segundos_restantes)}"

   def pad(numero):
      return str(numero).zfill(2)
  
   def generate_data():
      
      while True:
            pedido_id = ultimo_registro()
            registro = view_pedido(pedido_id) 

            if registro[-3] == "00:00:00":
               data = update_value('status_carga',True, "pedido_id = {pedido_id}")
               control_relay().stop()
            else:
               seg = tiempo_a_segundos(registro[-3])
               timeformat = formatear_tiempo(seg - 60)
               control_relay().start()

               print(timeformat)
               update_value('tiempo_carga', f"\'{timeformat}\'", f"pedido_id = {pedido_id}")
            print(registro)
            yield 'data: {}\n\n'.format(pedido_id)
            sleep(60)

   return Response(generate_data(), mimetype='text/event-stream', headers={'Cache-Control': 'no-cache'})


# section error

  
# error 
@app.errorhandler(404)
def not_found(e):
  print(e)
  return render_template('error.html', num='2'), 404
  
@app.errorhandler(500)
def internal_server(e):
  print(e)
  return render_template('error.html', num='3'), 500