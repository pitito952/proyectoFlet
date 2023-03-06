import flet as ft


def main(page):

    def casilla_cambiada(evento):
        lbl_resultado.value = (
            f'Has aprendido a programar: {tarea_marcada.value}.'
        )
        page.update()

    lbl_resultado = ft.Text()
    tarea_marcada = ft.Checkbox(label="Por hacer: Aprender a programar", 
                                value=False, on_change=casilla_cambiada)
    page.add(tarea_marcada, lbl_resultado)

ft.app(target=main)        