import flet as ft


def main(page):

    def boton_pulsado(evento):
        lbl_resultado.value = f"Color seleccionado: {lista_de_colores.value}"
        page.update()

    lbl_resultado = ft.Text()
    boton = ft.ElevatedButton(text='Presiona', on_click=boton_pulsado)
    lista_de_colores = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option('Rojo'),
            ft.dropdown.Option('Azul Marino'),
            ft.dropdown.Option('Verde Oliva')
        ]
    )       
    page.add(lista_de_colores, boton, lbl_resultado)

ft.app(target=main)