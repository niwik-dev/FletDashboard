from typing import Optional

import flet as ft

from context.router import Router


def MenuItem(
        title: str,
        icon: Optional[str] = None,
        path: Optional[str] = None,
        controls: Optional[list[ft.Control]] = None,
        **kwargs
):
    icon_size: float = 25
    arrow_icon = ft.Icon(
        name=ft.icons.ARROW_DROP_DOWN,
    )

    def on_change(event: ft.ControlEvent):
        router.go(path)
        selected = event.data
        if selected == 'true':
            arrow_icon.name = ft.icons.ARROW_DROP_UP
        if selected == 'false':
            arrow_icon.name = ft.icons.ARROW_DROP_DOWN
        arrow_icon.update()

    router = Router()
    if controls is None:
        tile = ft.ListTile(
            leading=ft.Container(
                width=icon_size,
                height=icon_size,
                alignment=ft.alignment.center,
                content=ft.Icon(
                    name=icon,
                    size=icon_size
                )
                if icon else ft.Icon(
                    name=ft.icons.CIRCLE_OUTLINED,
                    size=8
                )
            ),
            title=ft.Text(
                value=title
            ),
            **kwargs,
            on_click=lambda event: router.go(path)
        )
    else:
        tile = ft.ExpansionTile(
            leading=ft.Icon(
                name=icon,
                size=icon_size
            ),
            title=ft.Text(
                value=title
            ),
            trailing=arrow_icon,
            controls=controls,
            on_change=on_change,
            **kwargs
        )
    return tile


def MenuTitle(title: str):
    return ft.Container(
        height=25,
        padding=ft.padding.only(
            left=8
        ),
        content=ft.Text(
            value=title,
            weight=ft.FontWeight.BOLD,
            size=14
        )
    )


def MenuHeader(controls: list[ft.Control]):
    return ft.WindowDragArea(
        content=ft.Container(
            height=40,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=controls
            )
        )
    )


def MenuBody(controls: list[ft.Control]):
    return ft.Container(
        expand=True,
        content=ft.ListView(
            spacing=0,
            controls=controls
        )
    )


def MenuFooter(avatar: str, title: str, sub_title: str):
    return ft.Container(
        height=55,
        alignment=ft.alignment.center,
        content=ft.ListTile(
            leading=ft.CircleAvatar(
                content=ft.Icon(name=avatar)
            ),
            title=ft.Text(value=title),
            subtitle=ft.Text(value=sub_title),
        )
    )
