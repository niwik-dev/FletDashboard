import flet as ft

from context.page import PageContext


def Logo():
    src = 'assets/logo/logo.svg'
    dark_src = 'assets/logo/logo-dark.svg'

    context = PageContext()
    return ft.Image(
        src=dark_src if context.is_dark() else src,
    )
