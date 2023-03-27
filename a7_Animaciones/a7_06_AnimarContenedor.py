import flet as ft


def main(page: ft.Page):

    contenedor = ft.Container(
        width=150,
        height=150,
        bgcolor='red',
        animate=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT)
    )


    def animar_contenedor(evento):
        contenedor.width = 100 if contenedor.width == 150 else 150
        contenedor.height = 50 if contenedor.height == 150 else 150
        contenedor.bgcolor = 'blue' if contenedor.bgcolor == 'red' else 'red'

        contenedor.update()

    page.add(
        contenedor,
        ft.ElevatedButton("Animar contenedor!", on_click=animar_contenedor)
        )
    

ft.app(target=main)    
