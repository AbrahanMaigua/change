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
        
   
    def build(self):
        self.result = Text(value="0", color=colors.BLACK, size=20)

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
                            value='             R$ 12,25',
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
                            size=15
                        ),
                        ft.Text(
                            value='       6:00:00',
                            text_align='END',
                            size=15,
                            height=230,

                        ),
                        # adicionar botonos pagamentos
                        # pix
                        # caton de convenio 

                        ]    
                    ),

                    ],
                    

                    ),
        )
            

    