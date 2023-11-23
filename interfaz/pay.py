import flet as ft
from lib import pixadd
from dotenv import dotenv_values
import countdown

def build(page):
    config = dotenv_values(".env") 
    print(page.id)
    price, segs = page.id.split('&')[0] + '', page.id.split('&')[1]

    appid  = config['APP_ID']
    pix    = pixadd.create_cob(appid,price, 'teste interfaz')
    print(pix)
    qr     = pixadd.get_cob(appid,pix[1])
    #print(qr['charge'])
    pixid = qr['charge']['correlationID']


    url = qr['charge']['qrCodeImage']

    return ft.Row(
                controls=[
                    
                    ft.Column([
                        countdown.Countdown(60,page,pixid,appid, 
                                            check_Trastion=True,
                                            time=segs),
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