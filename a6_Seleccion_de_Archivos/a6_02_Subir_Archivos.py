from typing import Dict

import flet
from flet import (
    Column,
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    FilePickerUploadEvent,
    FilePickerUploadFile,
    Page,
    ProgressRing,
    Ref,
    Row,
    Text,
    icons,
)


def main(page: Page):
    barra_progreso: Dict[str, ProgressRing] = {}
    archivos = Ref[Column]()
    btn_subir = Ref[ElevatedButton]()

    # Función que responde a la selección de archivos
    def file_picker_result(evento: FilePickerResultEvent):
        btn_subir.current.disabled = True if evento.archivos is None else False
        barra_progreso.clear()
        archivos.current.controls.clear()
        if evento.archivos is not None:
            for f in evento.archivos:
                progBar_archivo = ProgressRing(value=0, bgcolor="#eeeeee", width=20, height=20)
                barra_progreso[f.name] = progBar_archivo
                archivos.current.controls.append(Row([progBar_archivo, Text(f.name)]))
        page.update()

    # Función que reporta el progreso
    def on_upload_progress(evento: FilePickerUploadEvent):
        barra_progreso[evento.file_name].value = evento.progress
        barra_progreso[evento.file_name].update()

    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)

    def upload_files(evento):
        lista_archivos = []
        if file_picker.result is not None and file_picker.result.archivos is not None:
            for f in file_picker.result.archivos:
                lista_archivos.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            file_picker.upload(lista_archivos)

    # hide dialog in a overlay
    page.overlay.append(file_picker)

    page.add(
        ElevatedButton(
            "Seleccionar archivos...",
            icon=icons.FOLDER_OPEN,
            on_click=lambda _: file_picker.pick_files(allow_multiple=True),
        ),
        Column(ref=archivos),
        ElevatedButton(
            "Subir",
            ref=btn_subir,
            icon=icons.UPLOAD,
            on_click=upload_files,
            disabled=True,
        ),
    )


flet.app(target=main, upload_dir="uploads")