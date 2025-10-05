import flet as ft

def main(page: ft.Page):
    page.title = 'My first app'

    greeting_text = ft.Text('hello world!')


    page.add(greeting_text)
ft.app(target=main, view=ft.WEB_BROWSER)