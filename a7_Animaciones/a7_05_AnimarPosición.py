import flet as ft


def main(page: ft.Page):

    c1 = ft.Container(width=50, height=50, bgcolor="red", animate_position=1000)
    c2 = ft.Container(width=50, height=50, bgcolor="green", top=60, left=0, animate_position=500)
    c3 = ft.Container(width=50, height=50, bgcolor="blue", top=120, left=0, animate_position=1000)


    def animar_contenedor(evento):

        c1.top = 20 
        c1.left = 200

        c2.top = 100
        c2.left = 40

        c3.top = 180
        c3.left = 100

        page.update()

    
    page.add(
        ft.Stack([c1, c2, c3], height=250),
        ft.ElevatedButton("Pulse para Animar!", on_click=animar_contenedor)
    )        

ft.app(target=main)