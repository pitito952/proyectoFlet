import flet as ft

def main(page: ft.Page):

    contenedor = ft.Container(
        width=100,
        height=100,
        bgcolor="blue",
        border_radius=5,
        scale=ft.transform.Scale(scale=1),
        animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT)
    )

    def animar(evento):
        contenedor.scale = 2
        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 30

    page.add(
        contenedor,
        ft.ElevatedButton("Pulsa para Animar!", on_click=animar)
    )        

ft.app(target=main)        