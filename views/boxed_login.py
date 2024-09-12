import flet as ft

from components.logo import Logo
from context.router import Router


def RegisterButton(src: str, text: str):
    return ft.OutlinedButton(
        height=48,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(
                radius=8
            ),
        ),
        content=ft.Row(
            controls=[
                ft.Image(
                    src=src,
                    width=24,
                    height=24,
                    fit=ft.ImageFit.CONTAIN,
                    border_radius=ft.border_radius.all(8)
                ),
                ft.Text(
                    value=text
                )
            ]
        )
    )


def LoginCard():
    input_username = ft.TextField(
        label='Username',
        autofocus=True,
        autocorrect=False,
    )

    input_password = ft.TextField(
        label='Password',
        password=True,
        can_reveal_password=True,
    )

    def login(event:ft.ControlEvent):
        username = input_username.value
        password = input_password.value
        router = Router()
        if username == 'admin' and password == 'admin123':
            router.go('/')
            router.go('/index')
        else:
            print('Wrong Password')

    return ft.Card(
        width=480,
        height=600,
        elevation=4,
        content=ft.Container(
            padding=ft.padding.only(
                top=32, bottom=32, left=16, right=16
            ),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    Logo(),
                    ft.Text(
                        value='Your Social Campaigns',
                        color=ft.colors.GREY_400,
                    ),
                    ft.Row(
                        controls=[
                            RegisterButton(
                                src='assets/icons/facebook.svg',
                                text='Sign in with Facebook'
                            ),
                            RegisterButton(
                                src='assets/icons/google.svg',
                                text='Sign in with Google'
                            )
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Container(
                                width=135,
                                content=ft.Divider(
                                    color=ft.colors.GREY_300
                                ),
                            ),
                            ft.Text(
                                value='or sign in with',
                                size=16
                            ),
                            ft.Container(
                                width=135,
                                content=ft.Divider(
                                    color=ft.colors.GREY_300
                                ),
                            ),
                        ]
                    ),
                    ft.ListTile(
                        leading=ft.Icon(
                            ft.icons.PERSON,
                            color=ft.colors.GREY_600,
                        ),
                        title=input_username
                    ),
                    ft.ListTile(
                        leading=ft.Icon(
                            ft.icons.LOCK,
                            color=ft.colors.GREY_600,
                        ),
                        title=input_password
                    ),
                    ft.ListTile(
                        leading=ft.Checkbox(
                            label='Remember me',
                            label_position=ft.LabelPosition.RIGHT,
                        ),
                        trailing=ft.TextButton(
                            content=ft.Text(
                                value='Forgot input_password?',
                                color=ft.colors.BLUE_500,
                                size=14,
                            ),
                        )
                    ),
                    ft.FilledButton(
                        height=42,
                        width=400,
                        text='Sign In',
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(
                                radius=8
                            ),
                        ),
                        on_click=login
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                value='Don\'t have an account?',
                                size=14
                            ),
                            ft.TextButton(
                                content=ft.Text(
                                    value='Create an account',
                                    color=ft.colors.BLUE_500,
                                    size=14
                                ),
                            )
                        ]
                    )
                ]
            ),
        )
    )


def BoxLoginView():
    return ft.View(
        route="/login",
        padding=0,
        controls=[
            ft.Container(
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=[
                        ft.colors.WHITE10,
                        ft.colors.BLUE_50
                    ]
                ),
                expand=True,
                alignment=ft.alignment.center,
                content=LoginCard()
            )
        ]
    )
