#
#   Ejemplo del uso de "flet" con Python
#
import flet as ft
from flet import IconButton, Page, Row, TextField, icons


def main(page: ft.Page):
    page.title = "Ejemplo de Contador en Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(event):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    def plus_click(event):
        txt_number.value = int(txt_number.value) + 1
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click), txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click), 
            ],
            alignment = ft.MainAxisAlignment.CENTER,
        )
    )        

# Modo Desktop
#ft.flet.app(target=main)

# Modo Web
ft.flet.app(target=main, view=ft.WEB_BROWSER, port=6173)