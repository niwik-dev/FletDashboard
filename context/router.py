import flet as ft

from context.page import PageContext


class Router:
    _instance = None
    _is_inited = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self._is_inited:
            self._router: dict[str, ft.Control] = dict()
            self._context = PageContext()
            self._is_inited = True

    def go(self, route: str):
        if route is None:
            return
        self._context.get_page().go(route)

    def add_route(self, route: str, page: ft.Control):
        self._router[route] = page

    def set_route(self, home=None, **kwargs):
        if home is not None:
            self._router.update({'/': home})

        for route, page in kwargs.items():
            self._router.update({'/' + route: page})

    def get_route(self, route) -> ft.Control:
        from pages.error import NotFoundPage

        if route not in self._router:
            return NotFoundPage()

        return self._router[route]
