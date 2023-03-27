import flet as ft

def main(page: ft.Page):

    contenedor = ft.Container(
        width=150,
        height=150,
        bgcolor="orange",
        border_radius=10,
        offset=ft.transform.Offset(-2, 0),
        animate_offset=ft.animation.Animation(1000)
    )

    def animar(evento):
        contenedor.offset = ft.transform.Offset(0, 0)
        contenedor.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.add(
        contenedor,
        ft.ElevatedButton("Mostrar control!", on_click=animar)
    )        

ft.app(target=main)    