import flet as ft


def StatsPanel(
        label: str,
        value: int,
        image: str,
        bgcolor: str,
        text_color: str,
):
    return ft.Column(
        col={"sm": 12, "md": 6, "lg": 4, "xl": 2},
        controls=[
            ft.Container(
                expand=True,
                height=160,
                alignment=ft.alignment.center,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=[
                        ft.colors.with_opacity(0.4, bgcolor),
                        ft.colors.with_opacity(0.6, bgcolor)
                    ],
                ),
                border_radius=8,
                content=ft.Column(
                    spacing=4,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                            src=image,
                        ),
                        ft.Text(
                            label,
                            color=text_color,
                            size=16,
                            weight=ft.FontWeight.W_500,
                        ),
                        ft.Text(
                            "{:,}".format(value),
                            color=text_color,
                            weight=ft.FontWeight.W_500,
                            size=24,
                        )
                    ]
                ),
            )
        ]
    )


def OverviewPage():
    return ft.Container(
        expand=True,
        padding=ft.padding.only(
            top=16, bottom=16,
            right=32, left=32
        ),
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        value='Overview',
                        size=32,
                        weight=ft.FontWeight.BOLD
                    )
                ),

                ft.ResponsiveRow(
                    spacing=24,
                    run_spacing=24,
                    controls=[
                        StatsPanel(
                            image='assets/icons/icon-user-male.svg',
                            label='Employees',
                            value=96,
                            bgcolor=ft.colors.PURPLE_100,
                            text_color=ft.colors.PURPLE_400,
                        ),
                        StatsPanel(
                            image='assets/icons/icon-briefcase.svg',
                            label='Clients',
                            value=3650,
                            bgcolor=ft.colors.ORANGE_100,
                            text_color=ft.colors.ORANGE_400
                        ),
                        StatsPanel(
                            image='assets/icons/icon-mailbox.svg',
                            label='Projects',
                            value=356,
                            bgcolor=ft.colors.BLUE_100,
                            text_color=ft.colors.BLUE_400
                        ),
                        StatsPanel(
                            image='assets/icons/icon-favorites.svg',
                            label='Clients',
                            value=696,
                            bgcolor=ft.colors.RED_100,
                            text_color=ft.colors.RED_400
                        ),
                        StatsPanel(
                            image='assets/icons/icon-pay-roll.svg',
                            label='Payroll',
                            value=3650,
                            bgcolor=ft.colors.GREEN_100,
                            text_color=ft.colors.GREEN_400
                        ),
                        StatsPanel(
                            image='assets/icons/icon-connect.svg',
                            label='Reports',
                            value=59,
                            bgcolor=ft.colors.BLUE_GREY_100,
                            text_color=ft.colors.BLUE_GREY_400
                        )
                    ]
                ),

                ft.ResponsiveRow(

                )
            ]
        )
    )
