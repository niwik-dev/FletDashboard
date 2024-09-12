import flet as ft

from context.router import Router
from components.typography import H1, H2, H3, H4


def NotFoundPage():
    def back_to_index(event: ft.ControlEvent):
        router = Router()
        router.go('/index')

    return ft.Container(
        expand=True,
        content=ft.Column(
            spacing=16,
            expand_loose=True,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(
                    width=320,
                    height=320,
                    src='assets/error/404.svg'
                ),
                ft.Text(
                    'Opps!!!',
                    size=32,
                    weight=ft.FontWeight.W_500,
                ),
                ft.Text(
                    'This page you are looking for could not be found.',
                    size=18,
                    color=ft.colors.GREY_800,
                    weight=ft.FontWeight.W_500,
                ),
                ft.FilledButton(
                    height=32,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(
                            radius=8
                        ),
                    ),
                    text='Back to home',
                    icon=ft.icons.ARROW_BACK,
                    on_click=back_to_index
                )
            ]
        )
    )
