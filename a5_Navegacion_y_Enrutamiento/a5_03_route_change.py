import flet as ft


def main(page: ft.Page):
    page.add(ft.Text(f"Initial route: {page.route}"))

    def route_change(route):
        # page.add(ft.Text(f"New route: {route}"))      # Original del ejerccicio
        page.add(ft.Text(f"New route: {route.route}"))  # Modificado por instructor
        page.on_route_change = route_change
    page.update()


ft.app(target=main, route_url_strategy="hash", view=ft.WEB_BROWSER)
