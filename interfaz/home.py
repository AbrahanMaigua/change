from typing import Any, List, Optional, Union
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
    IconButton
    
)
from flet_core.buttons import ButtonStyle
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue


class home(UserControl):
    def add(self, e):
        con = self.contador.value
        self.seconds = e.control.data
        print(con)
        mins, secs = divmod(self.seconds, 60)
        self.contador.value = "{:02d}:{:02d}".format(mins, secs)


    def delete(self, e):
        self.contador.value = "00:00"
    

    def btn(self,text,
            bg=colors.BLUE_GREY_100,
            color=colors.BLACK, expand=1,
            on_click=None,
            ref=None):
        return  ElevatedButton(text=text, 
                               bgcolor=bg,
                               color=color,
                               expand=expand,
                               on_click=None,
                               data=text,
                               height=100,
                               width=100,
                               ref=ref )
    
    def btnIcon(self, name, color, bg):
        return ft.ElevatedButton(
                    bgcolor=bg,
                    content=ft.Row(
                        [
                            ft.Icon(name=name, color=color),
                        ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    ),
                )
    def build(self):
        url = 'https://picsum.photos/400/300?1'
        """
                    Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Image(
                                height=300,
                                width=300,
                                src=url,
                                )
                        ]
                    ),
                    """
                  
        # application's root control (i.e. "view") containing all other controls
        self.contador =  ft.Text(
                            value='00:00',
                            text_align='center',
                            size=20,
                            color='gray'
                         ),
        return Container(
            padding=1,
            alignment=ft.alignment.center,
            content=Column(
                
                controls=[
                    Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                
                                value='Seja Ben-vindo!\nEscolhea o Tempo de recarga ',
                                height=230,
                                text_align='center',
                                size=20
                                )
                        ]
                    ),
                      Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=0,
                        run_spacing=0,

                        controls=[
                         ft.ElevatedButton(
                            bgcolor="white",
                            content=ft.Row(
                                [
                                    ft.Icon(name=ft.icons.CHECK,
                                            color='red'),
                                ],
                            alignment=ft.MainAxisAlignment.CENTER,

                            ),
                            data='x',
                            on_click=Page.go(lambda _: self.page.go("/method") )
                        ),
                         self.contador,
                         ft.ElevatedButton(
                            bgcolor="white",
                            content=ft.Row(
                                [
                                   ft.Icon(name=ft.icons.DELETE_OUTLINE,
                                           color='GREEN'),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                height=5,
                                width=5,

                                ),
                                on_click=self.delete,

                                data='x'
                        ),
                        ]
                    ),
                    Row(
                        controls=[
                            self.btn(text="15 min"),
                            self.btn(text="30 min"),
                        ]
                    ),
                    
                ]
            ),
        )

   

