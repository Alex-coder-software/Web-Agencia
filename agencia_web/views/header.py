import reflex as rx
from agencia_web.styles.styles import Size, Spacing, content_in_the_center_style
from agencia_web.styles.colors import Color, TextColor
from agencia_web.styles.fonts import FontWeight
from agencia_web.components.info_text import info_text
import agencia_web.constants as constants
import datetime

def header() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.avatar(
                        name="Contentcraft",
                        size=Spacing.MEDIUM_BIG.value,
                        src="/logo_agencia.jpg",
                        radius="full",
                        color=TextColor.BODY.value,
                        bg=Color.CONTENT.value,
                        padding="2px",
                        border=f"4px solid {Color.PRIMARY.value}",
                        margin_top=["4rem", "0.5rem", "10rem", "10rem", "10rem"] # Ajustar márgenes superiores según la pantalla
                    ),
                    rx.vstack(
                        rx.heading(
                            "@contentcraft",
                            size=Size.VERY_BIG.value,  # Añadir un tamaño para el heading
                            color=TextColor.HEADER.value,
                            font_size=FontWeight.MEDIUM.value,
                            margin_top=f"{Size.LARGE.value}rem",
                        ),
                        rx.hstack(
                            info_text(
                                f"+{experience()}",
                                "Años de experiencia"
                            ),
                            info_text(
                                "+2",
                                "Proyectos creados"
                            ),
                        ),
                        align="start"  # Alinear al inicio del vstack
                    ),
                    align="center",  # Alinear el contenido del box al centro
                    spacing=Spacing.DEFAULT.value,  # Añadir espacio entre los elementos del box
                    margin_top=["8rem", "12rem", "0px !important", "0px !important", "0px !important"],    
                ),
                spacing=Spacing.BIG.value,  
                align="center"  
            ),
            rx.box(
                rx.text(
                    """Hoy en día los portales de noticias o podcasts necesitan fijar su atención en otras áreas, 
                    viéndose obligados a dedicar menos tiempo a la creación de contenidos. 
                    Por ello, en nuestra agencia ayudamos a divulgadores de contenido sobre fútbol sala a lograr artículos, 
                    guiones o PDFs de calidad mediante nuestros conocimientos y experiencia en la redacción de contenidos.\n
                    """,
                    align="center",
                    style={
                        "textAlign": "center", 
                        "width": "100%", 
                        "marginLeft": "auto", 
                        "marginRight": "auto", 
                        "display": "block"
                    }
                ),
                rx.link( # En otro texto por qué en este caso es un enlace
                    rx.text(
                        "¿Te interesa? Contáctanos",
                        align="center",
                        style={
                            "textAlign": "center", 
                            "width": "100%", 
                            "marginLeft": "auto", 
                            "marginRight": "auto", 
                            "display": "block", 
                            "fontWeight": "bold" # Texto en negrita
                        }  
                    ),
                    href=constants.FIVERR_URL,
                    is_external=True,
                    _hover={
                        "transform": "scale(1.2)",  # Aumentar el tamaño del enlace
                        "boxShadow": "0px 4px 15px rgba(0, 0, 0, 0.2)",  # Añadir sombra al pasar el ratón
                        "borderRadius": "5px",  # Añadir borde redondeado al pasar el ratón
                        "backgroundColor": Color.PRIMARY.value,  # Cambiar el color de fondo al pasar el ratón
                        "padding": "5px"  # Añadir padding al pasar el ratón
                    }
                ),
                size=Spacing.MEDIUM_BIG.value,
                #radius="full", # Para hacer borde, en este caso no se usará, pero fue la idea inicial
                padding=f"{Size.DEFAULT.value}rem",
                #border=f"4px solid {Color.PRIMARY.value}" # Para hacer borde en este caso no se usará, pero fue la idea inicial
            ),
            align="center",  # Alinear el contenido del vstack al centro
            spacing=Spacing.BIG.value,  # Añadir espacio entre los elementos del vstack
            width="40%",
            margin_left=["0.5rem", "0.6rem", "4rem", "8rem", "12rem"],
            margin_right=["0.5rem", "0.6rem", "4rem", "8rem", "12rem"],
        ),
        max_width="100%", # Evitar que se exceda de las dimesniones de la pantalla
        style=content_in_the_center_style, # Stack alienado al centro
    )

def experience() -> int:
    return datetime.date.today().year - 2022 # Automatizar los años de experiencia