import flet
from flet import Page, Row, TextField, ElevatedButton, Column, Text




def main(page: Page):
    
    txt_nombre = TextField(label="Escribe tu nombre:")

    def botonPulsado(evento):
        print(f"Hola....{txt_nombre.value}")

    # Agregar controles a la página sin usar una variable
    page.add(
        Row(controls=[
            txt_nombre,
            ElevatedButton(text="Obtener nombre!", on_click=botonPulsado)
            ])
    )

    # Agregar controles usando una variable
    #row = Row(controls=[
    #        TextField(label="Escribe tu nombre:"),
    #        ElevatedButton(text="Obtener nombre!", on_click=botonPulsado)
    #        ])
    #page.add(row)


flet.app(target=main)    