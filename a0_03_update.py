import time

import flet
from flet import Page, Text


def main(page: Page):
    lbl_texto = Text()
    page.add(lbl_texto)

    for i in range(10):
        lbl_texto.value = f'Ciclo No.: {i}'
        page.update()

        time.sleep(.2)



flet.app(target=main)