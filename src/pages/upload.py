import flet as ft

from src.components.data_table import data_table
from src.components.base_border import base_border

from src.modules.side_bar import side_bar
from src.modules.load_file import load_file
from src.modules.workflow import complete_step

from src.models.ml_projects import MLProject

from src.theme import colors

def view_upload_page(page:ft.Page, ml_project: MLProject):
    table_placeholder = ft.Row(
        scroll=ft.ScrollMode.AUTO,
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.START,
        controls=(
            [data_table(ml_project.dataframe)]
            if ml_project.dataframe is not None
            else []
        ),
    )
    pick_btn = ft.Button("Selecionar arquivo", on_click=lambda e: page.run_task(file_picker))
    file_info = ft.Text(value="", visible=False, color=colors.TEXT)
    

    async def select_file(e):
        if ml_project.dataframe is None:
            return
        complete_step(ml_project, "upload")
        await page.push_route("/config")

    confirm_button = ft.Button("Confirm Selection", on_click=select_file, disabled=ml_project.dataframe is None)
    

    async def file_picker():
        result = await load_file()
        pick_btn.text = "Selecionar outro arquivo"
        file_info.value = result["name"]
        file_info.visible = True
        table_placeholder.controls = [data_table(result["df"])]
        confirm_button.disabled = False
        ml_project.dataframe = result["df"]
        ml_project.name = result["name"]
        page.update()

    upload_page = ft.Container(
        expand=True,
        content=ft.Row(
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                side_bar(page, ml_project),
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        expand=True,
                        controls=[
                            ft.Text("Upload", color=colors.TEXT, size=30, weight=ft.FontWeight.W_700),
                            ft.Text("Upload your dataset to begin your machine learnig model.", color=colors.TEXT, size=18),
                            ft.Container(
                                align = ft.Alignment.CENTER,
                                expand=1,
                                padding=20,
                                border_radius=10,
                                border=base_border(1),
                                content=ft.Column(
                                    controls=[
                                        pick_btn, 
                                        file_info
                                    ]
                                )
                            ),
                            ft.Container(
                                expand=3,
                                padding=20,
                                border_radius=10,
                                border=base_border(1),
                                content=ft.Column(   
                                    controls=[
                                        ft.Row(
                                            controls = [
                                                ft.Text("Preview of Your Dataset", color=colors.TEXT, size=30, weight=ft.FontWeight.W_700),
                                            ]
                                        ),
                                        ft.Column(
                                            expand=True,
                                            scroll=ft.ScrollMode.AUTO,
                                            controls=[
                                                table_placeholder,
                                            ],
                                        ),     
                                    ] 
                                ),
                            ),
                            confirm_button
                        ]
                    )
                )
            ]
        )
    )

    return upload_page
