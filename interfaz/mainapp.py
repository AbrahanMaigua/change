import flet as ft
from flet import colors, ElevatedButton
import home, pay, button, checking 
import countdown


    
def main(page: ft.Page):
    def btn(text,
            bg=colors.BLUE_GREY_100,
            color=colors.BLACK, expand=1,
            data=0,
            on_click=None,
            ref=None):
        return  ElevatedButton(text=text, 
                               bgcolor=bg,
                               color=color,
                               expand=expand,
                               on_click=on_click,
                               data=data,
                               height=100,
                               width=100,
                               ref=ref )

    def go_pay(e):
        page.route = "/pay"
        page.update()

    def route_change(route):
        troute = ft.TemplateRoute(page.route)

        if troute.match("/pay/:id"):
            print("Book view ID:", troute.id)
        elif troute.match("/account/:account_id/orders/:order_id"):
            print("Account:", troute.account_id, "Order:", troute.order_id)
        else:
            print("Unknown route")
            page.title = "Routes Example"
        a = home.home(page)
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    a,
                    ft.Row(
                        controls=[
                            btn(text="1 hora", on_click=a.add, data=60),
                            btn(text="Personalizado", on_click=lambda _: page.go("/btn")),
                        ]
                    ),
                    
                ],
            )
        )
        if troute.match("/pay/:id"):
            page.views.append(
                ft.View(
                    "/pay/:id",
                    [
                        ft.AppBar(title=ft.Text("Store"),
                                  bgcolor=ft.colors.SURFACE_VARIANT),
                        pay.build(troute)

                        

                    ],
                )
            )
            page.update()

        elif troute.match("/btn"):
            page.views.append(
                ft.View(
                    "btn",
                    [
                        ft.AppBar(title=ft.Text(""), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Row(
                            [
                                button.CalculatorApp(page).build()
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                )
            )
        elif troute.match("/carga/:timpo"):
            page.views.append(
                ft.View(
                   "/carga/:timpo",
                    [
                       ft.Row([
                           countdown.Countdown(int(troute.timpo))
                       ],
                       alignment=ft.MainAxisAlignment.CENTER,
                       vertical_alignment=ft.CrossAxisAlignment.CENTER,
                       )
                       
                    ],
                )
            )
        elif troute.match('/check/:time'):
               page.views.append(
                ft.View(
                    "/check/:time",
                    [
                        ft.AppBar(title=ft.Text(""), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Row(
                            [
                               checking.check(page).build()
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    


ft.app(target=main)
