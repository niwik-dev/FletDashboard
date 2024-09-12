import flet as ft


def IndexPage():
    return ft.Container(
        content=ft.Column(
            spacing=32,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(
                            ft.icons.DASHBOARD,
                            size=60,
                            color=ft.colors.BLUE_400,
                        ),
                        ft.Text(
                            'Flet Dashboard',
                            size=40,
                            weight=ft.FontWeight.BOLD,
                        )
                    ]
                ),
                ft.Divider(),
                ft.Markdown(
                    value="""
This is a dashboard template built with Flet.
It is a good starting point for building your own dashboard.

How to use:
* Clone this repository.
* Run `pip install -r requirements.txt`
* Run `python main.py`
* Open http://localhost:8080 in your browser.
* Enjoy!

Any questions? Feel free to ask me on GitHub or Discord.
                """.strip(),
                    selectable=True,
                )
            ]
        )
    )
