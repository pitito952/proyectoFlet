import flet as ft
from flet import Checkbox, ElevatedButton, Row, TextField, Page

def main(page: Page):
    def agregar_tarea_clicked(evento):
        page.add(ft.Checkbox(label=txt_nueva_tarea.value))
        txt_nueva_tarea.value = ""
        txt_nueva_tarea.focus()
        txt_nueva_tarea.update()

    txt_nueva_tarea = ft.TextField(hint_text="Nueva tarea a realizar...", width=500)
    page.add(ft.Row([txt_nueva_tarea, ft.ElevatedButton("Agregar tarea", on_click=agregar_tarea_clicked)]))

ft.app(target=main)