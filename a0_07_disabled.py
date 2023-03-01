import flet
from flet import Column, Page, TextField


def main(page: Page):
    # Definir los campos que recibirán los datos
    txt_nombre = TextField(label="Nombre:")
    txt_apellido = TextField(label="Apellido:")
    
    # Definir la disposición de los controles (campos) en la página
    column_controles = Column(
                    controls=[txt_nombre, txt_apellido])
    
    # Deshabilitar campos INDIVIDUALMENTE
    txt_nombre.disabled = True
    txt_apellido.disabled = True
    
    # Deshabilitar TODOS los controles (campos) antes de mostrarlos
    #column_controles.disabled = True
    
    # Mostrar la página con los controles definidos deshabilitados
    page.add(column_controles)


flet.app(target=main)    