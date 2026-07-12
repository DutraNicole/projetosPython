import flet as ft

def main(page: ft.page):
    page.title = "Calculadora"
    page.bgcolor = "#2d2d2d"
    page.window.width = 350
    page.window.heigth = 470
    page.padding = 10
    
    resultado_teste = ft.Text(value = "0", size = 28, color="white", text_align = "right")
    
    display = ft.Container(
        content = resultado_teste,
        bgcolor = "#37474F",
        padding = 10,
        border_radius = 10,
        height = 70,
        alignment=ft.Alignment(1, 0)
        
        )
    
    button_grids = [
            [
                    ("C"),
                    ("%"),
                    ("/"),
                    ("*"),
            ],
            [
                    ("7"),
                    ("8"),
                    ("9"),
                    ("-"),
            ],
            [
                    ("4"),
                    ("5"),
                    ("6"),
                    ("+"),
            ],
            [
                    ("1"),
                    ("2"),
                    ("3"),
                    ("="),
            ],
            [
                    ("0"),
                    ("."),
                    ("x"),
            ]
        ]
    
        button = []
        for row in button_grid:
            row_controls = []
    
    page.add(
        
        ft.Column(
            [
                    display,
                
            ],
            )
        )
    
ft.app(target=main)
