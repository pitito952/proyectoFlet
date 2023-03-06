import flet as ft


def main(page):
    lbl_texto = ft.Text(
            value = 'Ejemplo de un control -Text- .',
            size = 20,          # Tamaño de la fuente
            color = 'white',    # Color de la fuente
            bgcolor = 'blue',   # Fondo del campo
            weight = 'bold',    # Tipo de fuente
            italic = True       # Tipo de fuente
    )

    page.add(lbl_texto)


ft.flet.app(target=main)
