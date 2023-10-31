import flet as ft
import home

def main(page: ft.Page):

    def route_change(route):
        troute = ft.TemplateRoute(page.route)

        if troute.match("/s/:id"):
            print("Book view ID:", troute.id)
        elif troute.match("/account/:account_id/orders/:order_id"):
            print("Account:", troute.account_id, "Order:", troute.order_id)
        else:
            print("Unknown route")
            page.title = "Routes Example"

        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    home.home(),
                    
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store/:id",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
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

    


ft.app(target=main, view=ft.AppView.WEB_BROWSER)