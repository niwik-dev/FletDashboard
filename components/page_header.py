import flet as ft


def Notification():
    return ft.Container(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.END,
            controls=[
                ft.IconButton(
                    icon=ft.icons.NOTIFICATIONS
                )
            ]
        )
    )


def AvatarMenu(avatar: str):
    avatar_size = 40
    return ft.Container(
        border_radius=ft.border_radius.all(
            avatar_size
        ),
        content=ft.Image(
            src=avatar,
            width=avatar_size,
            height=avatar_size,
            fit=ft.ImageFit.COVER,
            border_radius=ft.border_radius.all(
                avatar_size
            )
        ),
        on_click=lambda _: print('expand menu')
    )


def PageHeader(
    avatar: str
):
    return ft.ListTile(
        leading=ft.IconButton(ft.icons.MENU),
        trailing=ft.Row(
            alignment=ft.MainAxisAlignment.END,
            controls=[
                Notification(),
                AvatarMenu(avatar)
            ]
        )
    )
