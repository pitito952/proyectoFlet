#
#   Autenticación mediante API de Github.
#   Programa que solicita datos de login (usuario y contraseña).
#
#   1.- Configurar el Proveedor de OAuth (Github, Azure, Google, Auth0).
#       
#       1.1.- En Github pulsar en ícono del usuario (a mano derecha).
#       1.2.- Pulsar sobre "Settings".
#       1.3.- En menú de la izquierda pulsar sobre "Developer settings".
#       1,4,- En menú de la izquierda pulsar sobre "OAuth Apps".
#       1.5.- Registrar la aplicación que efectuará el login rellenando los datos solicitados.
#       1.6.- Copiar "Client ID" y "Client secret" en lugar seguro.
#       1.7.- Llevar los datos en 1.6.- a variables en memoria para luego usar en el programa:
#           1.7.1.- $ export GITHUB_CLIENT_ID="<client_id>"
#           1.7.2.- $ export GITHUB_CLIENT_SECRET="<client_secret>"
#       1.8.- Ejecutar éste programa......
#
#       1.9.- Client ID generado:  04b5442c57a166852276
#       1.10.- Client secret generado: 192698191eeecb0afb11db40034edbd29ad687bd

import os

import flet
from flet import Page, ElevatedButton
from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider


def main(page: Page):

    proveedor = GitHubOAuthProvider(
        client_id=os.getenv("GITHUB_CLIENT_ID"),
        client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
        redirect_url="http://localhost:8550/api/oauth/redirect"
    )

    def login_click(evento):
        page.login(proveedor)

    def on_login(evento):
        print("Token de acceso: ", page.auth.token.access_token)
        print("User ID: ", page.auth.user.id)

    page.on_login = on_login
    page.add(ElevatedButton("Login con Github", on_click=login_click))


flet.app(target=main, port=8550, view=flet.WEB_BROWSER)    
