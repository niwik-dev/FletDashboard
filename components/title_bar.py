import flet as ft


def TitleBar():
    return ft.WindowDragArea(
        content=ft.Container(
            height=50,
            bgcolor=ft.colors.RED,
            content=ft.Row(
                controls=[

                ]
            )
        )
    )
