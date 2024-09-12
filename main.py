import flet as ft

from context.page import PageContext
from context.router import Router
from pages import *
from views.boxed_login import BoxLoginView
from views.home import HomeView


def main(page: ft.Page):
    context = PageContext()
    context.set_page(page)

    page.title = "Flet Dashboard"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.title_bar_hidden = True

    home_pages = ft.Container()

    router = Router()
    router.set_route(
        login=BoxLoginView(),
        logout=BoxLoginView(),
        home=HomeView(home_pages),

        index=IndexPage(),
        overview=OverviewPage(),
        settings=SettingsPage()
    )

    def route_change(event: ft.RouteChangeEvent):
        next_item = router.get_route(event.route)

        if isinstance(next_item, ft.View):
            if next_item in page.views:
                page.views.remove(next_item)
            page.views.append(next_item)
            page.update()
        else:
            home_pages.content = next_item
            home_pages.update()

    page.on_route_change = route_change
    page.go('/login')


ft.app(main)
