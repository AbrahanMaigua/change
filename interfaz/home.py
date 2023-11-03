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

        # application's root control (i.e. "view") containing all other controls
        return Container(
            padding=5,
            alignment=ft.alignment.center,
            content=Column(
                
                controls=[
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
                    Row(
                        controls=[
                            self.btn(text="9"),
                            self.btn(text="4"),
                        ]
                    ),
                    
                ]
            ),
        )

   

