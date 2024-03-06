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

def create_pedido(date, status, fomatado, seg, valor):
    """ Create new pedido in database

    :param
        date::      time zone create pedido
        status::    true pay not pay false
        formatado:: HH:MM:SS
        valor::     valor a pagar
        seg::       total seconds

    """
    sql = '''
    INSERT INTO pedido(create_at, status_pagamento, tiempo_carga, valor, segundo_total)
      VALUES (?,?,?,?,?)
        
    '''
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql, (date, status, fomatado,  valor,seg))
    conn.commit()
    

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
    



def pay_paedido(idPix):
    """ Update pedido in True status

    :param
        pedido_id::: is identification pedido

    """
    
    sql = f""" UPDATE pedido 
               SET status_pagamento = TRUE
               WHERE pix_id = {idPix}   
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

    return cur.fetchall()[0]


def view_all():

    conn = create_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM pedido')

    return cur.fetchall()
def ultimo_registro():

    sql = '''SELECT pedido_id FROM pedido 
    WHERE pedido_id = (SELECT MAX(pedido_id)  FROM pedido);'''

    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql)

    return cur.fetchall()[0][0]


conn = create_connection()
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS pedido (
    pedido_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    pix_id              INTERGER DEFAUL NULL,
    create_at           DATE,  
    status_pagamento    BOOL DEFAULT FALASE,
    tiempo_carga        TEXT,
    valor               FLOAT,
    segundo_total       INTEGER          
); ''')



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
