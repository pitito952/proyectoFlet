import flet as ft


def fin_de_la_animacion(evento):
    print("Contenido del objeto 'evento': \n", dir(evento))


def main(page: ft.Page):

    contenedor = ft.Container(
        width=150,
        height=150,
        bgcolor="blue",
        border_radius=10,
        animate_opacity=300,
        on_animation_end=fin_de_la_animacion
    )


    def animate_opacity(evento):
        contenedor.opacity = 0 if contenedor.opacity == 1 else 1
        contenedor.update()

    page.add(
        contenedor,
        ft.ElevatedButton(
            "Animar Transparencia",
            on_click=animate_opacity
        )
    )        


ft.app(target=main)