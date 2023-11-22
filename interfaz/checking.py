from typing import Any, Optional, Union
import flet as ft
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
    
)

# terminar la tela hacer que funcione
class check(UserControl):
    def __init__(self, page=None):
        self.page = page
        
    def btn(self,text,
            bg=colors.BLUE_GREY_100,
            color=colors.BLACK, expand=1,
            on_click=None,
            ref=None, data=0):
        return  ElevatedButton(text=text, 
                               bgcolor=bg,
                               color=color,
                               expand=expand,
                               on_click=on_click,
                               data=data,
                               height=100,
                               width=100,
                               ref=ref)
   
    def build(self, time):
        self.result = Text(value="0", color=colors.BLACK, size=20)

        price = '12,25'
        print(time)
        # application's root control (i.e. "view") containing all other controls
        return Container(
           
            alignment=ft.alignment.center,
            content=Column(
                controls=[
                     ft.Text(
                        value='',
                        height=20,
                            text_align='center',
                            size=20
                            ),
                    ft.Text(
                        value='verificacion ',
                        height=130,
                        text_align='center',
                        size=30
                            ),
                    ft.Row(
                        [
                        ft.Text(
                            value='Valor a Pagar',
                            text_align='START',
                            size=15
                        ),
                        ft.Text(
                            value=f'             R$ {price}',
                            text_align='END',
                            size=15
                        ),

                        ]    
                    ),
                  ft.Row(
                        [
                        ft.Text(
                            value='tiempo de Carga',
                            text_align='START',
                            size=15,
                            height=80

                        ),
                        ft.Text(
                            value='       6:00:00',
                            text_align='END',
                            size=15,
                            height=80
                            

                        ),
             

                        ]

                    ),
                    Row(
                        controls=[
                           ft.ElevatedButton(
                               text='Pix',
                               on_click=lambda _: self.page.go(f"/pay/{price.replace(',', '')}")
                           ),
                           ft.ElevatedButton(
                               text='mobility cart'

                          )
                        ]
                    ),

                    ],
                    

                    ),
        )
            

    