
#  Ejemplo 2 de arrastrar y soltar

import flet as ft


def main(page: ft.Page):
    page.title = "Ejemplo de Arrastrar y Soltar"

    def drag_accept(evento):
        # Obtener el origen o fuente (source) que se va a copiar en base a su ID
        origen = page.get_control(evento.src_id)
        # Actualizar texto dentro del control de origen o fuente (source)
        origen.content.content.value = "0"
        # Actualizar texto dentro del control de destino (target)
        evento.control.content.content.value = "1"
        page.update()

    page.add(
        ft.Row(
            [
                ft.Draggable(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", size=20),
                        alignment=ft.alignment.center,
                    ),
                    content_when_dragging=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                    content_feedback=ft.Text("1"),
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="number",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", size=20),
                        alignment=ft.alignment.center,
                    ),
                    on_accept=drag_accept,
                ),
            ]
        )
    )


ft.app(target=main, view=ft.WEB_BROWSER)
