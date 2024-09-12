from typing import Optional
import flet as ft


class PageContext:
    _instance = None
    _is_inited = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, page: ft.Page = None):
        super().__init__()
        if not self._is_inited:
            self._page: Optional[ft.Page] = page
            self._is_inited = True

    def set_page(self, page: ft.Page) -> None:
        self._page = page

    def get_page(self) -> ft.Page:
        return self._page

    def is_dark(self) -> bool:
        return self._page.theme_mode == ft.ThemeMode.DARK

    def with_title_bar(self) -> bool:
        return not self._page.window.title_bar_hidden
