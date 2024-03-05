import sqlite3
from sqlite3 import Error
from datetime import datetime

def create_connection(db_file='db.sqlite3'):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_pedido(date, status, fomatado, seg):
    """ Create new pedido in database

    :param
        date::      time zone create pedido
        status::    true pay not pay false
        formatado:: HH:MM:SS
        seg::       total seconds
    """
    sql = '''
    INSERT INTO pedido(create_at, status_pagamento, tiempo_carga, segundo_total)
      VALUES (?,?,?,?)
        
    '''
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql, (date, status, fomatado, seg))
    conn.commit()
    

def pay_paedido(pedido_id):
    """ Update pedido in True status

    :param
        pedido_id::: is identification pedido

    """
    
    sql = f""" UPDATE pedido 
               SET status_pagamento = TRUE
               WHERE pedido_id = {pedido_id}   
    """
    conn = create_connection()
    cur  = conn.cursor()
    cur.execute(sql)
    conn.commit()
    


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

    return cur.fetchall()


def view_all():

    conn = create_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM pedido')

    return cur.fetchall()

conn = create_connection()
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS pedido (
    pedido_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    create_at           DATE,  
    status_pagamento    BOOL DEFAULT FALASE,
    tiempo_carga        TEXT,
    segundo_total       INTEGER          
); ''')



"""
example use
 
date = datetime.now()

date_row = date.strftime('%m/%d/%Y %H:%M:%S')
form     = date.strftime('%H:%M:%S') 
carga    = '00:30:00'
segTotal = '1800'

create_pedido(date_row, False, carga, segTotal)
pay_paedido(1)
print(view_all())

"""