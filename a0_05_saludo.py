import flet
from flet import Page, Row, TextField, ElevatedButton, Column, Text


def main(page: Page):
    # Definir texto a mostrar en campo de entrada
    txt_textoCampo = TextField(label="Escribe tu nombre:")
    # Definir variable a usar para mostrar el saludo
    lbl_saludo = Text()


    def botonPulsado(evento):
        # Colocar en la etiqueta el texto que se muestra en pantalla
        lbl_saludo.value = (f"Hola....{txt_textoCampo.value}")
        # Se actualiza la página (pantalla)
        page.update()

    # Agregar controles a la página sin usar una variable
    page.add(
        Row(controls=[
            # Se muestra el campo donde ha de ingresarse el dato
            txt_textoCampo,
            # Se define el botón con su orden al pulsarse
            ElevatedButton(text="Obtener nombre!", on_click=botonPulsado),
            # Se muestra el saludo al texto ingresado
            lbl_saludo
            ])
    )
    

    # Agregar controles usando una variable
    #row = Row(controls=[
    #        TextField(label="Escribe tu nombre:"),
    #        ElevatedButton(text="Obtener nombre!", on_click=botonPulsado)
    #        ])
    #page.add(row)


flet.app(target=main)    