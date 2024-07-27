import reflex as rx
from agencia_web.styles.styles import Size, content_in_the_center_style, table_style
from agencia_web.styles.colors import Color, TextColor
from agencia_web.components.link_button import link_button
from agencia_web.styles.fonts import FontWeight
import agencia_web.constants as constants

def pricing() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Precios",
                size=Size.GIANT.value,  
                font_size=FontWeight.MEDIUM.value,
                style=content_in_the_center_style
            ),
            rx.box(
            rx.table.root(
                rx.table.header(
                    rx.table.row( # La sección principal será una línea
                        rx.table.column_header_cell("Paquete", style=table_style),
                        rx.table.column_header_cell("Entrega", style=table_style),
                        rx.table.column_header_cell("Artículos", style=table_style),
                        rx.table.column_header_cell("Guiones", style=table_style),
                        rx.table.column_header_cell("PDF/Ebook", style=table_style),
                    ),
                ),
                rx.table.body(
                    rx.table.row( #Escribiremos por líneas, si fuera por columnas sería rx.table.column
                        rx.table.row_header_cell("500 palabras máx", style=table_style),
                        rx.table.cell("48 horas", style=table_style),
                        rx.table.cell("2€", style=table_style),
                        rx.table.cell( # Las secciones vacías tendrán un color distinto. Me parecío la mejor forma para evitar confusiones con los precios.
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("1000 palabras máx", style=table_style),
                        rx.table.cell("48 horas", style=table_style),
                        rx.table.cell("5€", 
                            " ¡En oferta!", 
                            style={ # Este es el table_style pero con algunas modificaciones para hacerlo más vistoso
                                "color": TextColor.BODY.value, 
                                "border": "1px solid #CCCCCC", 
                                "font_size": ["0.6rem", "1rem", "1.2rem"], 
                                "padding": "0.5rem", 
                                "line-height": "1.2",
                                "font-weight": "bold" # Texto en negrita
                            }
                        ),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("3000 palabras máx", style=table_style),
                        rx.table.cell("48 horas", style=table_style),
                        rx.table.cell("10€", style=table_style),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("Vídeo/Podcast de 5 minutos max", style=table_style),
                        rx.table.cell("48 horas", style=table_style),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                        rx.table.cell("10€", style=table_style),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("Vídeo/Podcast de 10 minutos max", style=table_style),
                        rx.table.cell("72 horas", style=table_style),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                        rx.table.cell("15€", style=table_style),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("Vídeo/Podcast de 15 minutos max", style=table_style),
                        rx.table.cell("72 horas", style=table_style),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                        rx.table.cell("18€ ¡Mejor precio!", style={ # Este es el table_style pero con algunas modificaciones para hacerlo más vistoso
                            "color": TextColor.BODY.value, 
                            "border": "1px solid #CCCCCC", 
                            "font_size": ["0.6rem", "1rem", "1.2rem"], 
                            "padding": "0.5rem", 
                            "line-height": "1.2",
                            "font-weight": "bold" # Texto en negrita
                            }
                        ),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("PDF/ebook de 10 páginas máx", style=table_style),
                        rx.table.cell("5 días", style=table_style),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                        rx.table.cell("20€", style=table_style),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("PDF/ebook de 20 páginas máx", style=table_style),
                        rx.table.cell("7 días", style=table_style),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                        rx.table.cell("30€", style=table_style),
                    ),
                    rx.table.row(
                        rx.table.row_header_cell("PDF/ebook de 40 páginas máx", style=table_style),
                        rx.table.cell("15 días", style=table_style),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                        rx.table.cell(
                            "",
                            bg=Color.SECONDARY.value,
                            style=table_style
                        ),
                        rx.table.cell("35€ ¡Mejor precio/página!", 
                            style={ # Este es el table_style pero con algunas modificaciones para hacerlo más vistoso
                                "color": TextColor.BODY.value, 
                                "border": "1px solid #CCCCCC", 
                                "font_size": ["0.6rem", "1rem", "1.2rem"], 
                                "padding": "0.5rem", 
                                "line-height": "1.2",
                                "font-weight": "bold"
                            }
                        ),
                    ),
                ),
                style={"width": "100%", "maxWidth": "100%", "margin": "0 auto", "textAlign": "left"},
                margin_top=f"{Size.BIG.value}rem",
            ),
            margin_top=f"{Size.DEFAULT.value}rem",
            width="100%"
            ),
        ),
        rx.box(
            rx.text(
                "Si quieres contratar más de un servicio, tenemos la mejor opción para ti.",
                font_size="1.1rem"
            ),
            rx.text(
                "Ofertas por contratar más de un servicio:",
                font_size="1.1rem"
            ),
            margin_top=f"{Size.BIG.value}rem",
            style=content_in_the_center_style,
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row( # La tabla sigue el mismo estilo que la anterior
                    rx.table.column_header_cell("Combo de paquetes", style=table_style),
                    rx.table.column_header_cell("Precio", style=table_style),
                    rx.table.column_header_cell("Entrega", style=table_style),
                ),
            ),
            rx.table.body(
                rx.table.row(
                    rx.table.row_header_cell("Artículo + Guion", style=table_style),
                    rx.table.cell("desde 10€", style=table_style),
                    rx.table.cell("Máximo 12 días", style=table_style),
                ),
                rx.table.row(
                    rx.table.row_header_cell("Artículo + Ebook/PDF", style=table_style),
                    rx.table.cell("desde 18€", style=table_style),
                    rx.table.cell("Máximo 15 días", style=table_style),
                ),
                rx.table.row(
                    rx.table.row_header_cell("Guion + PDF/Ebook", style=table_style),
                    rx.table.cell("desde 22€", style=table_style),
                    rx.table.cell("Máximo 20 días", style=table_style),
                ),
                rx.table.row(
                    rx.table.row_header_cell("Artículo + Guion + PDF/ebook", style=table_style),
                    rx.table.cell("desde 25€", style=table_style),
                    rx.table.cell("Máximo 30 días", style=table_style),
                ),
            ),
            margin_top=f"{Size.BIG.value}rem",
        ),
        rx.box(
            rx.text(
                "Para información más exacta y personalizada según el tamaño de los paquetes contáctanos desde Fiverr.",
                font_size="1.1rem",
                margin_top=f"{Size.BIG.value}rem",
            ),
        ),
        rx.box(
            link_button(
                "Contáctanos",
                "por Fiverr",
                constants.FIVERR_URL,
            ),
            margin_top=f"{Size.BIG.value}rem",
            width="40%"
        ),
        max_width="100%", # Evitar que se exceda de las dimesniones de la pantalla
        margin_top=f"{Size.BIG.value}rem",
        style=content_in_the_center_style,
        margin_right=Size.ZERO.value
    )
