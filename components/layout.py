from typing import Optional

import flet as ft


def Layout(
    aside: ft.Control,
    body: ft.Control,
    header: ft.Control,
):
    return ft.Row(
        expand=True,
        controls=[
            ft.Container(
                width=300,
                border=ft.border.only(
                    right=ft.border.BorderSide(
                        width=1,
                        color=ft.colors.GREY_300,
                    )
                ),
                content=aside
            ),
            ft.Column(
                expand=True,
                controls=[
                    ft.WindowDragArea(
                        content=ft.Container(
                            height=50,
                            content=header,
                        ),
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        expand=True,
                        content=body
                    )
                ]
            )
        ]
    )