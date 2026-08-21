import flet as ft

from src.components.drawer_button import drawer_button

from src.modules.workflow import can_access_step

from src.models.ml_projects import MLProject

from src.theme import colors

def side_bar(page: ft.Page, ml_project: MLProject):
    config_available = can_access_step(ml_project, "config")
    preprocessing_available = can_access_step(ml_project,"preprocessing",)
    model_parameters_available = can_access_step(ml_project,"model_parameters",)
    training_available = can_access_step(ml_project,"training",)
    results_available = can_access_step(ml_project,"results",)

    async def upload_call(e):
        await page.push_route("/upload")

    async def config_call(e):
        await page.push_route("/config")

    async def preprocessing_call(e):
        await page.push_route("/preprocessing")

    async def model_parameters_call(e):
        await page.push_route("/model_parameters")

    async def training_call(e):
        await page.push_route("/training")

    async def results_call(e):
        await page.push_route("/results")

    return ft.Container(
        width=200,
        content=ft.Column(
            spacing=0,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                drawer_button("Upload", upload_call, active=page.route == "/upload", disabled = False),
                drawer_button("Config", config_call, active=page.route == "/config", disabled = not config_available),
                drawer_button("Preprocessing", preprocessing_call, active=page.route == "/preprocessing", disabled = not preprocessing_available),
                drawer_button("Model Parameters", model_parameters_call, active=page.route == "/model_parameters", disabled = not model_parameters_available),
                drawer_button("Training", training_call, active=page.route == "/training", disabled = not training_available),
                drawer_button("Results", results_call, active=page.route == "/results", disabled = not results_available),
            ]
        )
    )