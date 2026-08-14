import flet as ft

from src.components.app_bar import app_bar

from src.models.ml_projects import MLProject

from src.theme import colors

from src.pages.app import view_home_page
from src.pages.upload import view_upload_page
from src.pages.config import view_config_page
from src.pages.preprocessing import view_preprocessing_page
from src.pages.model_parameters import view_model_parameters_page
from src.pages.training import view_training_page
from src.pages.results import view_results_page

def main(page: ft.Page):
    page.title = "ML Builder"
    ml_project = MLProject()

    def route_change():
        page.views.clear()
        page.views.append(
            ft.View(
                align=ft.Alignment.CENTER,
                route="/",
                appbar=app_bar(),
                bgcolor=colors.BACKGROUND,
                controls=[
                    view_home_page(page)
                ],
            )
        )

        if page.route == "/upload":
            page.views.append(
                ft.View(
                    align=ft.Alignment.CENTER,
                    route="/upload",
                    appbar=app_bar(),
                    bgcolor=colors.BACKGROUND,
                    controls=[
                        view_upload_page(page, ml_project)
                    ],
                )
            )
        if page.route == "/config":
            page.views.append(
                ft.View(
                    align=ft.Alignment.CENTER,
                    route="/config",
                    appbar=app_bar(),
                    bgcolor=colors.BACKGROUND,
                    controls=[
                        view_config_page(page, ml_project)
                    ],
                )
            )
        if page.route == "/preprocessing":
            page.views.append(
                ft.View(
                    align=ft.Alignment.CENTER,
                    route="/preprocessing",
                    appbar=app_bar(),
                    bgcolor=colors.BACKGROUND,
                    controls=[
                        view_preprocessing_page(page, ml_project)
                    ],
                )
            )
        if page.route == "/model_parameters":
            page.views.append(
                ft.View(
                    align=ft.Alignment.CENTER,
                    route="/model_parameters",
                    appbar=app_bar(),
                    bgcolor=colors.BACKGROUND,
                    controls=[
                        view_model_parameters_page(page, ml_project)
                    ],
                )
            )
        if page.route == "/training":
            page.views.append(
                ft.View(
                    align=ft.Alignment.CENTER,
                    route="/training",
                    appbar=app_bar(),
                    bgcolor=colors.BACKGROUND,
                    controls=[
                        view_training_page(page, ml_project)
                    ],
                )
            )
        if page.route == "/results":
            page.views.append(
                ft.View(
                    align=ft.Alignment.CENTER,
                    route="/results",
                    appbar=app_bar(),
                    bgcolor=colors.BACKGROUND,
                    controls=[ 
                        view_results_page(page, ml_project)
                    ],
                )
            )

    page.update()

    async def view_pop(e):
        if e.view is not None:
            print("View pop:", e.view)
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()
if __name__ == "__main__":
    ft.run(main)