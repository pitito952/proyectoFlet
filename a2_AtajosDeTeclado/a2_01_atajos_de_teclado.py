import flet as ft

def main(page: ft.Page):

    def on_keyboard(e: ft.KeyboardEvent):
        page.add(
            ft.Text(
                f"Valor de cada Tecla: Tecla pulsada={e.key}, Shift={e.shift}, Control={e.ctrl}, Alt={e.alt}, Meta={e.meta}")
        )

    page.on_keyboard_event = on_keyboard
    page.add(
        ft.Text("Pulse una tecla en combinación con las teclas CTRL, ALT, SHIFT y META")
    )

ft.app(target=main)    