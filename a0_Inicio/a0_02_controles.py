import flet as ft
from flet import Page, Text

def main(page: Page):
    lbl_texto = ft.Text(value="Hola, Mundo!", color="green")
    page.controls.append(lbl_texto)   # page.add(lbl_texto)
    page.update()

ft.app(target=main)
