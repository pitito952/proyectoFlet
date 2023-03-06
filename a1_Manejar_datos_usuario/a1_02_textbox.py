
import flet as ft


def main(page):

    def btn_click(evento):
    
        if not txt_nombre.value:
            txt_nombre.error_text = "Introduce tu nombre:"
            page.update()
        else:
            nombre = txt_nombre.value
            page.clean()                # Limpiar TODA la pantalla
            page.add(ft.Text(f"Hola, {nombre}!"))

    txt_nombre = ft.TextField(label="Nombre:")

    page.add(
        txt_nombre, 
        ft.ElevatedButton("Di Hola!", on_click=btn_click)
        )


ft.app(target=main)    