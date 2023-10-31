import flet as ft
class pay(ft.UserControl):
    def build(self):
        url = 'https://picsum.photos/500/500?1'
        return ft.Row(
                [
                ft.Column(
                    wrap=True,
                    spacing=1,
                    controls=[
                        ft.Row([ft.Text('text')],alignment='CENTER'),
                        ft.Row([ft.Image(src=url)]),
                        ],
                )
            ],
            alignment="CENTER",
           
            )
         

        

def main(page:ft.Page):
    page.add(pay())

ft.app(
    target=main,
    assets_dir="assets"
)