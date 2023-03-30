import os

import flet
from flet import Page, ElevatedButton, LoginEvent
from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider


def main(page: Page):

    proveedor = GitHubOAuthProvider(
        client_id=os.getenv("GITHUB_CLIENT_ID"),
        client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
        redirect_url="http://localhost:8550/api/oauth/redirect"
    )

    def login_button_click(evento):
        page.login(proveedor, scope=["public_repo"])


    def on_login(evento: LoginEvent):
        if not evento.error:
            toggle_login_buttons()


    def logout_button_click(evento):
        page.logout()


    def on_logout(evento):
        toggle_login_buttons()


    def toggle_login_buttons():
        login_button.visible = page.auth is None
        logout_button.visible = page.auth is not None
        page.update()


    login_button = ElevatedButton("Login con Github", on_click=login_button_click)
    logout_button = ElevatedButton("Logout", on_click=logout_button_click)
    toggle_login_buttons()
    page.on_login = on_login
    page.on_logout = on_logout

    page.add(
        login_button,
        logout_button
    )        


flet.app(target=main, port=8550, view=flet.WEB_BROWSER)    