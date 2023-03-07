import flet as ft

def main(page: ft.Page):
    # Establecer el tamaño específico en altura que tandrá el despliegue de la lista
    # lv = ft.ListView(height=300, spacing=10)
    # Establecer TODA la ventana en altura para el despliegue de la lista
    lv = ft.ListView(expand=True, spacing=10)
    for i in range(5000):
        lv.controls.append(ft.Text(f"Linea {i}"))
    page.add(lv)

#ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER)
 