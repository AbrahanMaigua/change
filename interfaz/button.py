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
class CalculatorApp(UserControl):
    def __init__(self, page=None):
        self.page = page
    def btn(self,text,
            bg=colors.BLUE_GREY_100,
            color=colors.BLACK, expand=1,
            ):
        
        return  ElevatedButton(text=text, 
                               bgcolor=bg,
                               color=color,
                               expand=expand,
                               on_click=self.button_clicked,
                               data=text )
    
    def btnIcon(self, name, color, bg, on_click=None):
        return ft.ElevatedButton(
                    bgcolor=bg,
                    content=ft.Row(
                        [
                            ft.Icon(name=name, color=color),
                        ],
                    alignment=ft.MainAxisAlignment.CENTER,

                    ),
                    on_click=on_click,
                    data='x'
                )
    def build(self):
        self.reset()
        self.result = Text(value="0", color=colors.BLACK, size=20)

        # application's root control (i.e. "view") containing all other controls
        return Container(
            padding=20,
            width=300,
            
            alignment=ft.alignment.center,
            content=Column(
                controls=[
                    Row(controls=[self.result], alignment="center"),
                    
                    Row(
                     alignment=ft.MainAxisAlignment.CENTER,

                        controls=[
                            self.btn(text="7"),
                            self.btn(text="8"),
                            self.btn(text="9"),
                        ]
                    ),
                    Row(
                        controls=[
                            self.btn(text="4"),
                            self.btn(text="5"),
                            self.btn(text="6"),
                        ]
                    ),
                    Row(
                        controls=[
                            self.btn(text="1"),
                            self.btn(text="2"),
                            self.btn(text="3"),
                        ]
                    ),
                    Row(
                        controls=[
                            
                            self.btnIcon(ft.icons.DELETE_OUTLINE, 'white', colors.RED, 
                                         on_click=self.button_clicked),

                            self.btn(text="0"),
                            self.btnIcon(ft.icons.CHECK, 'white', 
                                         colors.GREEN, 
                                         on_click=lambda _: self.page.go(f"/pay/{self.result.value}")),

                        ]
                    ),
                ]
            ),
            
        )

    def button_clicked(self, e):
        data = e.control.data
        print(self.result.value)
        try:
               
            if int(data) in tuple(range(0,10)):
                if self.result.value == "0" or self.new_operand == True:
                    self.result.value = data
                    self.new_operand = False
                else:
                    self.result.value = self.result.value + data
        except ValueError:
            if data == 'x':
               self.result.value = self.result.value[:-1]
                

        self.page.update()

    def reset(self):
        self.new_operand = True

