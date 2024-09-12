import flet as ft


def H1(text: str, **kwargs):
    return ft.Text(
        value=text,
        size=30,
        weight=ft.FontWeight.W_500,
        **kwargs
    )


def H2(text: str, **kwargs):
    return ft.Text(
        value=text,
        size=24,
        weight=ft.FontWeight.W_500,
        **kwargs
    )


def H3(text: str, **kwargs):
    return ft.Text(
        value=text,
        size=21,
        weight=ft.FontWeight.W_500,
        **kwargs
    )


def H4(text: str, **kwargs):
    return ft.Text(
        value=text,
        size=18,
        weight=ft.FontWeight.W_500,
        **kwargs
    )


def H5(text: str, **kwargs):
    return ft.Text(
        value=text,
        weight=ft.FontWeight.W_500
    )


def H6(text: str, **kwargs):
    return ft.Text(
        value=text,
        weight=ft.FontWeight.W_500
    )
