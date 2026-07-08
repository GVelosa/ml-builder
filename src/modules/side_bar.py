import flet as ft

from src.components.drawer_button import drawer_button

def side_bar(page: ft.Page):

    async def upload_call():
        await page.push_route("/upload")

    async def config_call():
        await page.push_route("/config")

    async def preprocessing_call():
        await page.push_route("/preprocessing")

    async def model_parameters_call():
        await page.push_route("/model_parameters")

    async def training_call():
        await page.push_route("/training")

    async def results_call():
        await page.push_route("/results")

    return ft.Container(
        width=200,
        content=ft.Column(
            spacing=0,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                drawer_button("Upload", upload_call, active=page.route == "/upload"),
                drawer_button("Config", config_call, active=page.route == "/config"),
                drawer_button("Preprocessing", preprocessing_call, active=page.route == "/preprocessing"),
                drawer_button("Model Parameters", model_parameters_call, active=page.route == "/model_parameters"),
                drawer_button("Training", training_call, active=page.route == "/training"),
                drawer_button("Results", results_call, active=page.route == "/results"),
            ]
        )
    )