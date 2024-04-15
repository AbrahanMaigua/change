<<<<<<< HEAD
from flask import g
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-

>>>>>>> 527fb03 (alter db)
from .config import load_config 
import psycopg2


def create_connection():
    config = load_config()
    db = psycopg2.connect(**config)
    return db

def create_table_pedido():
     execute('''
        CREATE TABLE IF NOT EXISTS pedido (
            pedido_id           SERIAL PRIMARY KEY,
            pix_id              INTEGER DEFAULT NULL,
<<<<<<< HEAD
            created_date        TEXT ,
            created_time        TEXT ,
=======
            created_at          VARCHAR,
            time_create         VARCHAR,
>>>>>>> 527fb03 (alter db)
            status_pagamento    BOOLEAN DEFAULT FALSE,
            status_carga        BOOLEAN DEFAULT FALSE,
            tiempo_carga        TEXT,
            valor               FLOAT,
            segundo_total       INTEGER
    ); ''')
     
def execute(sql, values=None):
    try:
        conn = create_connection()
        cur  = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
    except  psycopg2.errors.UndefinedTable as e:

        print(e)
        create_table_pedido()
       


    #return cur.fetchall()[0]


<<<<<<< HEAD
def create_pedido(date, time_c, fomatado, seg, valor):
=======
def create_pedido(date,time_row, fomatado, seg, valor):
>>>>>>> 527fb03 (alter db)
    """ Create new pedido in database

    :param
        date::      time zone create pedido
        status::    true pay not pay false
        formatado:: HH:MM:SS
        valor::     valor a pagar
        seg::       total secondss

    """

    sql = '''
<<<<<<< HEAD
    INSERT INTO pedido(created_date, created_time,  tiempo_carga, segundo_total, valor)
      VALUES (%s, %s, %s, %s, %s);
        
    '''
    execute(sql, values=(date,time_c, fomatado, seg, valor))
=======
    INSERT INTO pedido(created_at, time_create, tiempo_carga, segundo_total, valor)
      VALUES (%s, %s, %s, %s, %s);
        
    '''
    execute(sql, values=(date,time_row, fomatado, seg, valor))
>>>>>>> 527fb03 (alter db)

def add_pix_id(pedido_id ,pix_id):
    """ add pix_id ref in pix 

    :param
        pedido_id::: is identification pedido

    """
    
    sql = f""" UPDATE pedido 
               SET pix_id = {pix_id}
               WHERE pedido_id = {pedido_id}   
    """
    conn = create_connection()
    cur  = conn.cursor()
    cur.execute(sql)
    conn.commit()
    

<<<<<<< HEAD
def update_value(column,value,where):
    """ Update pedido in True status

    :param
        pedido_id::: is identification pedido
        column   ::: is column name updare
=======
def update_status(colunm,idPix):
    """ Update pedido in True status

    :param
        pedido_id ::: is identification pedido
        colunm    ::: is update status 
>>>>>>> 527fb03 (alter db)

    """
    
    sql = f""" UPDATE pedido 
<<<<<<< HEAD
               SET {column} = {value}
               WHERE {where}; 
=======
               SET {colunm} = TRUE
               WHERE pix_id = {idPix}   
>>>>>>> 527fb03 (alter db)
    """
    print(sql)
    conn = create_connection()
    cur  = conn.cursor()
    cur.execute(sql)
    conn.commit()
<<<<<<< HEAD
    cur.close()
    conn.close()
=======

def view_status(colunm):

    sql = f'''SELECT {colunm} FROM pedido 
             WHERE  pedido_id = (SELECT MAX(pedido_id)
             FROM   pedido);'''

    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql)

    return cur.fetchall()
    
>>>>>>> 527fb03 (alter db)



def check_status():
    """ query pedido by id  
    :param
        pedido_id::: is identification pedido


    :return list[tuple]
    """ 
    regitro_id = ultimo_registro()
   
    return view_pedido(regitro_id)[2]
    
    
def view_pedido(pedido_id):
    """ query pedido by id  
    :param
        pedido_id::: is identification pedido


    :return list[tuple]
    """ 
    sql = f'SELECT * FROM pedido WHERE pedido_id = {pedido_id} '
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql)

    return cur.fetchall()[0]

def view_all():

    conn = create_connection()
    cur  = conn.cursor()
    row = cur.fetchone()
    if row:
        return row[0]
    return None



<<<<<<< HEAD
=======
    return cur.fetchall()

>>>>>>> 527fb03 (alter db)
def ultimo_registro():

    sql = '''SELECT pedido_id FROM pedido 
             WHERE  pedido_id = (SELECT MAX(pedido_id)
             FROM   pedido);'''

    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql)
    row = cur.fetchone()
    if row:
        return row[0]
    return None


create_table_pedido()

"""
example use
 
date = datetime.now()

date_row = date.strftime('%m/%d/%Y %H:%M:%S')
form     = date.strftime('%H:%M:%S') 
carga    = '00:30:00'
valor    =  45.00
segTotal = '1800'

create_pedido(date_row, False, carga, valor, segTotal)
pay_paedido(ultimo_registro())
print(view_all())

"""

