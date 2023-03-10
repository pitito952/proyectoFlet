#   10/03/2023  
# Listas extensas mostradas en bloques para acelerar renderizado
#
import flet as ft


def main(page: ft.Page):
    lista = ft.ListView(expand=1, spacing=10, item_extent=50)
    page.add(lista)

    for i in range(5100):
        lista.controls.append(ft.Text(f"Linea {i}"))

        if i % 500 == 0:
            page.update()

    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)
