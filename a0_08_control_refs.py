import flet as ft  # Al colocarle "as" no es necesario importar los módulos por separado
#from flet import Column, ElevatedButton, Text, TextField, Page


def main(page):         # Así aparece en los ejemplos de la guía.
#def main(page: Page):    # Modo inicial. El instructor lo sigue usando ya que permite ver los módulos
                          # de "page" cuando se escribe lo cual ayuda.
    txt_nombre = ft.TextField(label='Nombre:', autofocus=True)
    txt_apellido = ft.TextField(label='Apellido:')
    col_saludo = ft.Column()

    def btn_click(evento):
        col_saludo.controls.append(ft.Text(f'Hola, {txt_nombre.value} {txt_apellido.value}'))
        # Limpiar los campos UNO x UNO (no funciona limpiarlos todos en una sola linea)
        txt_nombre.value = "" 
        txt_apellido.value = ""
        page.update()
        txt_nombre.focus()

    # Definir botón
    btn_saludar = ft.ElevatedButton('Hola', on_click=btn_click)

    # Agregar a la página todos los campos y controles preparados antes
    page.add(
        txt_nombre,
        txt_apellido,
        btn_saludar,
        col_saludo,
        )
    

ft.app(target=main)

                             
