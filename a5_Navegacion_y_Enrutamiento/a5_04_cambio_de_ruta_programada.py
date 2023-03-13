
import flet as ft


def main(page: ft.Page):
    page.add(ft.Text(f"Ruta inicial:  {page.route}"))

    def route_change(route):
        page.add(ft.Text(f"Nueva ruta: {route.route}"))

    def go_store(evento):
        page.route = "/tienda"
        page.update()

    page.on_route_change = route_change
    page.add(ft.ElevatedButton("Ir a la tienda", on_click=go_store))


ft.app(target=main, view=ft.WEB_BROWSER)
