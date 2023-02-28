import flet as ft
from flet import Page, Text

def main(page: Page):
    t = ft.Text(value="Hola, Mundo!", color="green")
    page.controls.append(t)
    page.update()

ft.app(target=main)
