import flet as ft
from lib import pixadd
from dotenv import dotenv_values
import countdown

def build(page):
    """

    print(page.id)
    config = dotenv_values(".env") 
    appid  = config['APP_ID']
    pix    = pixadd.create_cob(appid,page.id+'00', 'teste interfaz')
    qr     = pixadd.get_cob(appid,pix[1])
    print(qr['charge']['qrCodeImage'])

    """
    url = "https://api.openpix.com.br/openpix/charge/brcode/image/35c15841-bb42-4000-a31c-829efb85b821.png"
    return ft.Row(
                controls=[
                    

                    ft.Column([
                      #  countdown.Countdown(50,page),
                        ft.Image(src=url, height=400, width=300),
                    
                    ],
                    )
                    ],
                   alignment=ft.MainAxisAlignment.CENTER,
        )