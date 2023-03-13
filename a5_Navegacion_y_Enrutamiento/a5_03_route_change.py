import flet as ft


def main(page: ft.Page):
    page.add(ft.Text(f"Initial route: {page.route}"))

    def route_change(route):
        # page.add(ft.Text(f"New route: {route}"))      # Original del ejerccicio
        page.add(ft.Text(f"New route: {route.route}"))  # Modificado por instructor
        page.on_route_change = route_change
    page.update()


# Original del ejercicio
# ft.app(target=main, view=ft.WEB_BROWSER)

# Modificado por mi en base al punto "URL strategy for web" de la misma página del
# manual. Con la forma normal (anterior) NO hacía el cambio de página correctamente.
ft.app(target=main, route_url_strategy="hash", view=ft.WEB_BROWSER)
