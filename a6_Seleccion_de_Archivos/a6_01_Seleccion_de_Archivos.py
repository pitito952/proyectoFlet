
#   Manejo de archivos y directorios
#       Permite seleccionar uno o mas archivos
#       Permite actualizar o guardar un archivo
#       Permite abrir un directorio
#
import flet
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
)


def main(page: Page):

    # Diálogo de seleeción de archivos
    def pick_files_result(e: FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelado!"
        )
        selected_files.update()

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files = Text()

    # Diálogo para Actualizar archivo
    def save_file_result(e: FilePickerResultEvent):
        save_file_path.value = e.path if e.path else "Cancelado!"
        save_file_path.update()

    save_file_dialog = FilePicker(on_result=save_file_result)
    save_file_path = Text()

    # Diálogo para Abrir Directorio
    def get_directory_result(e: FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Cancelado!"
        directory_path.update()

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()

    # Ocultar todos los diálogos (superpuestos?)
    page.overlay.extend([pick_files_dialog, save_file_dialog, get_directory_dialog])

    # Crear botones
    page.add(
        Row(
            [
                ElevatedButton(
                    "Seleccionar archivos",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True),
                ),
                selected_files,
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Actualizar archivo",
                    icon=icons.SAVE,
                    on_click=lambda _: save_file_dialog.save_file(),
                    disabled=page.web,   # Deshabilita botón cuando página web
                ),
                save_file_path,
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Abrir directorio",
                    icon=icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web,  # Deshabilita botón cuando página web
                ),
                directory_path,
            ]
        ),
    )


flet.app(target=main, view=flet.WEB_BROWSER)
