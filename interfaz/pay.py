import flet as ft
from lib import pixadd
from dotenv import dotenv_values
import countdown

def build(page):
    config = dotenv_values(".env") 
    appid  = config['APP_ID']
    pix    = pixadd.create_cob(appid,page.id+'00', 'teste interfaz')
    qr     = pixadd.get_cob(appid,pix[1])
    print(qr['charge'])
    pixid = qr['charge']['correlationID']


    url = qr['charge']['qrCodeImage']

    return ft.Row(
                controls=[
                    
                    ft.Column([
                        countdown.Countdown(10,page,pixid,appid, check_Trastion=True),
                        #countdown.Countdown(10),
                        ft.Image(src=url, height=400, width=300),

                    ],
                    spacing=0,

                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                    ],
                   alignment=ft.MainAxisAlignment.CENTER,
                   
        )