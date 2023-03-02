#
#   Programa similar al anterior (a0_08).
#   Acá se aplica el método Ref a variables y controles para que al desplegar la pantalla
#   (page.add) se pueda diferenciar claramente que tipo de variable o control se está
#   mostrando.
#   Sin embargo SIN el método Ref, tal como el programa a0_08, se pueden identificar
#   las variables y los controles manualmente agregando un prefijo a los mismos.
#

import flet as ft  # Al colocarle "as" no es necesario importar los módulos por separado
#from flet import Column, ElevatedButton, Text, TextField, Page


def main(page):           # Así aparece en los ejemplos de la guía.
#def main(page: Page):    # Modo inicial. El instructor lo sigue usando ya que permite ver los módulos
                          # de "page" cuando se escribe, lo cual ayuda.
    nombre = ft.Ref[ft.TextField]()     # Nótese los paréntesis fuera de los corchetes
    apellido = ft.Ref[ft.TextField]()   # Nótese los paréntesis fuera de los corchetes
    saludo = ft.Ref[ft.Column]()        # Nótese los paréntesis fuera de los corchetes


    def btn_click(evento):
        saludo.current.controls.append(
            ft.Text(f'¡Hola, {nombre.current.value} {apellido.current.value}!'))
        # Limpiar los campos UNO x UNO (no funciona limpiarlos todos en una sola linea)
        nombre.current.value = "" 
        apellido.current.value = ""
        page.update()
        nombre.current.focus()

    # Definir botón
    btn_saludar = ft.ElevatedButton('Hola', on_click=btn_click)


    # Agregar a la página todos los campos y controles preparados antes
    page.add(
        ft.TextField(ref=nombre, label='Nombre:', autofocus=True),
        ft.TextField(ref=apellido, label='Apellido'),
        btn_saludar,
        ft.Column(ref=saludo)
        )
    

ft.app(target=main)

                             
