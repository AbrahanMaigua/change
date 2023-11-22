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
        self.seconds = 0
        self.con1 = 1 # numeros pincipales 00 00 00
        self.con2 = 1 # numeros secudarios 0


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
        self.contador = 0
        self.result = Text(value="00:00:12", color=colors.BLACK, size=20)

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
                                         on_click=lambda _: self.page.go(f"/check/{self.result.value}")),

                        ]
                    ),
                ]
            ),
            
        )

    def convert(self, seconds): 
        min, sec = divmod(seconds, 60) 
        hour, min = divmod(min, 60) 
        return "%d:%02d:%02d" % (hour, min, sec) 
        

    def button_clicked(self, e):
        data = e.control.data
        value = self.result.value.split(':') # [00, 00, 00]
        try:
            if int(data) in tuple(range(0,10)):
                con = list(value[-self.con1]) # [0, 0]
                # 00 00 00 
                #        ^-1 self.con2
                con[-self.con2] = data
                value[-self.con2] = ''.join(con) # modifica la fila
                # 00 00 00 
                #       ^^
                print(value)
                if self.con2 >= 2:
                    self.con1 += 1 
                    self.con2 = 1 

                self.con2 += 1
                 
                self.result.value = ':'.join(value)
        except ValueError:
            if data == 'x':
               self.contador -= 1
               if self.contador // 3 == 1 or 0:
                  self.contador -= 1
               self.result.value[:-self.contador] = 0
                

        self.page.update()

    def reset(self):
        self.new_operand = True

