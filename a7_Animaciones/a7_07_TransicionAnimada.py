import time
import flet as ft


def main(page: ft.Page):

    imagen = ft.Image(src="https://picsum.photos/150/150", width=150, height=150)


    def animar(evento):

        sw.content = ft.Image(src=f"https://picsum.photos/150/150?{time.time()}", width=150, height=150)

        page.update()


    sw = ft.AnimatedSwitcher(
        imagen,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=500,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN
    )

    page.add(
        sw,
        ft.ElevatedButton("Pulsa para Poceder", on_click=animar)
    )


ft.app(target=main) 
