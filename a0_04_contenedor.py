import time
import flet
from flet import Page, Row, Text, TextField, ElevatedButton


def main(page: Page):
    # Definir variable y aplicar controles
    row_datos = Row(
                controls=
                    [
                        Text('Python'), 
                        Text('Flet'), 
                        Text('Flutter')
                    ]
                )
    # Agregar variable al contenedor (página)
    page.add(row_datos)

    ##############################################
    # Otra manera de hacer lo mismo
    #
    # Definir una lista con los datos
    lenguajes = ['Cobol', 'Assembler', 'PL/1']
    # Definir una lista vacía a usar en el iterador
    etiquetas = []

    # Agregar los datos de la lista "lenguajes" a la lista "etiquetas"
    for e in lenguajes:
        etiquetas.append(Text(e))
    # Componer la variable que se mostrará en pantalla
    row_datos = Row(controls=etiquetas)
    # Incluir la variable en la página
    page.add(row_datos)

    #############################################
    # Agregar controles sin usar una variable
    page.add(
        Row(controls=[
        TextField(label="Tu nombre"),
        ElevatedButton(text="Escribe tu nombre!")
        ])
    )

    for i in range(10):
        page.controls.append(Text(f"Linea {i}"))
        if i > 6:
            page.controls.pop(0)
        page.update()
        time.sleep(1.3)


flet.app(target=main)