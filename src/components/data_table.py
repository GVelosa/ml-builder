import flet as ft

def data_table(df):
    return ft.DataTable(
        columns=[ft.DataColumn(ft.Text(col)) for col in df.columns],
        rows=[
            ft.DataRow(cells=[ft.DataCell(ft.Text(str(val))) for val in row])
            for row in df.itertuples(index=False)
        ]
    )