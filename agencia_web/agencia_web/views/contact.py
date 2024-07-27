import reflex as rx
from agencia_web.styles.styles import Size, content_in_the_center_style, Spacing
from agencia_web.styles.fonts import FontWeight
import agencia_web.constants as constants
from agencia_web.components.link_icon import link_icon

def contact() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Contacto",
                size=Size.GIANT.value,  
                font_size=FontWeight.MEDIUM.value,
                margin_top=f"{Size.VERY_BIG.value}rem",
                style=content_in_the_center_style
            ),
            rx.text(
                "Si te interesa contratar nuestros servicios, puedes contactarnos desde estas tres aplicaciones:",
                style=content_in_the_center_style
            ),
            rx.hstack(
                rx.box(
                    link_icon(
                        "fiverr.jpg",
                        constants.FIVERR_URL,
                        "Logo de Fiverr",
                        "50px",
                        "75px"
                    ),
                    margin_left="auto",
                    margin_right="auto" # Con los márgenes en auto hacemos que sea responsive
                ),
                rx.spacer(), # Espacio entre elementos
                rx.box(
                    link_icon(
                        "upwork.jpg",
                        constants.UPWORK_URL,
                        "Logo de Upwork",
                        "60px",
                        "75px"
                    ),
                    margin_left="auto", 
                    margin_right="auto" # Con los márgenes en auto hacemos que sea responsive
                ),
                rx.spacer(), # Espacio entre elementos
                rx.box(
                    link_icon(
                        "workana.jpg",
                        constants.WORKANA_URL,
                        "Logo de Workana"
                        "30px",
                        "60px"
                    ),
                    margin_left="auto",
                    margin_right="auto" # Con los márgenes en auto hacemos que sea responsive
                ),
                margin=f"{Spacing.DEFAULT.value}rem",
                margin_top=f"{Size.SMALL.value}rem",
                width="75%"
            ),
        ),
        max_width="100%", # Evitar que se exceda de las dimesniones de la pantalla
        style=content_in_the_center_style
    )