
# Ejemplo de Navegación y rutas con página (web)

import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors


def main(page: Page):
    page.title = "Ejemplo de Enrutamiento"
    # Imprimir en consola la ruta inicial o de comienzo del ejercicio
    print("Ruta inicial:", page.route)

    # Función que responde al cambio de ruta
    def route_change(evento):
        # Imprimir la nueva ruta en consola
        print("Ruta cambiada:", evento.route)
        # Limpiar la vista o ventana
        page.views.clear()

        # Crear la vista Principal
        page.views.append(
            View(
                "/",        # Ruta designada
                [
                    AppBar(title=Text("Aplicación Flet")),
                    ElevatedButton("Ir a configuración", on_click=open_settings),
                ],
            )
        )
        # Si la ruta es cualquiera de 'configuración' mostrar vista de 'Detalle de Configuracón'
        if page.route == "/settings" or page.route == "/settings/mail":
            page.views.append(
                View(
                    "/settings",    # Ruta designada
                    [
                        AppBar(title=Text("Configuración"), bgcolor=colors.SURFACE_VARIANT),
                        # Text("Settings!", style="bodyMedium"),   # Vino en el ejemplo
                        Text("Detalle de la Configuración!", style=flet.TextThemeStyle.LABEL_MEDIUM),
                        ElevatedButton(
                            "Ir a la configuración de correo", on_click=open_mail_settings
                        ),
                    ],
                )
            )
        # Si la ruta es de 'configuración de correo' mostrar vista de "Detalle configuración de
        # correo"
        if page.route == "/settings/mail":
            page.views.append(
                View(
                    "/settings/mail",       # Ruta designada
                    [
                        AppBar(
                            title=Text("Configuración de correo"), bgcolor=colors.SURFACE_VARIANT),
                        Text("Detalle de la Configuración de Correo!"),
                    ],
                )
            )
        page.update()

    def view_pop(evento):
        print("View pop", evento.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def open_mail_settings(evento):
        page.go("/settings/mail")

    def open_settings(evento):
        page.go("/settings")

    page.go(page.route)


flet.app(target=main, view=flet.WEB_BROWSER)
