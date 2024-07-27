import reflex as rx
from agencia_web.styles.styles import Size, Spacing, content_in_the_center_style
from agencia_web.styles.colors import Color
from agencia_web.styles.fonts import FontWeight
from agencia_web.components.link_button import link_button
import agencia_web.constants as constants

def services() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Nuestros Servicios",
                size=Size.GIANT.value,  # Añadir un tamaño para el heading
                font_size=FontWeight.MEDIUM.value,
                style=content_in_the_center_style
            ),
            rx.hstack(
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "ARTÍCULOS PARA WEB",
                            margin_left="auto",
                            margin_right="auto"
                        ),
                        rx.text(
                            """Tú eliges la longitud y el tema y nosotros redactamos un artículo de calidad 
                            después de haber investigado sobre el tema y palabras clave. El límite de las opciones 
                            está en tu mente, y el límite de entrega en 48 horas sea cual sea la longitud del artículo."""
                        )
                    ),
                    size=Spacing.MEDIUM_BIG.value,
                    radius="full", # Para el borde
                    padding=f"{Size.DEFAULT.value}rem",
                    border=f"4px solid {Color.PRIMARY.value}",
                    margin=f"{Size.DEFAULT.value}rem", # Para el borde
                    width=["90%", "80%", "70%", "30%", "25%"],  # Ajustar ancho según el tamaño de la pantalla
                    style=content_in_the_center_style
                ),
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "GUIONES DE PODCASTS O VÍDEOS",
                            margin_left="auto",
                            margin_right="auto"
                        ),
                        rx.text(
                            """Si tu web no se encierra en el contenido escrito sino que también se pasa al mundo audiovisual, 
                            somos tu mejor opción. Redactamos guiones tanto para vídeos como para podcasts, pudiendo variar 
                            la entrega de 2 a 4 días."""
                        )
                    ),
                    size=Spacing.MEDIUM_BIG.value,
                    radius="full", # Para el borde
                    padding=f"{Size.DEFAULT.value}rem",
                    border=f"4px solid {Color.PRIMARY.value}", # Para el borde
                    margin=f"{Size.DEFAULT.value}rem",
                    width=["90%", "80%", "70%", "30%", "25%"],  # Ajustar ancho según el tamaño de la pantalla
                    style=content_in_the_center_style
                ),
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "PDFS O EBOOKS",
                            margin_left="auto",
                            margin_right="auto"
                        ),
                        rx.text(
                            """Muchos medios de comunicación están lanzando al mercado contenidos más extensos, 
                            tales como PDFs o ebooks con información más explícita. Nuestra agencia puede redactar estos contenidos también, 
                            siendo el tiempo de entrega dependiente de la longitud del contenido."""
                        )
                    ),
                    size=Spacing.MEDIUM_BIG.value,
                    radius="full", # Para el borde
                    padding=f"{Size.DEFAULT.value}rem",
                    border=f"4px solid {Color.PRIMARY.value}", # Para el borde
                    margin=f"{Size.DEFAULT.value}rem", 
                    width=["90%", "80%", "70%", "30%", "25%"],  # Ajustar ancho según el tamaño de la pantalla
                    style=content_in_the_center_style
                ),
                margin_top=f"{Size.DEFAULT.value}rem",
                justify="center",
                wrap="wrap" # Permitir que los elementos se envuelvan (que cambien de row a column y viceversa)
            ),
            rx.box(
                rx.text(
                    "Puedes conocer más sobre las entregas o características de cada servicio en nuestra cuenta de fiverr "
                ),
                rx.box(
                    link_button(
                        "Accede",
                        "A fiverr",
                        constants.FIVERR_URL
                    ),
                    margin_top=f"{Size.BIG.value}rem"
                ),
                margin_top=f"{Size.BIG.value}rem",
            ),
            align="center",  # Alinear el contenido del vstack al centro
            spacing=Spacing.BIG.value,  # Añadir espacio entre los elementos del vstack
            padding=f"{Size.BIG.value}rem",  # Añadir espacio de padding al vstack
            style=content_in_the_center_style
        ),
        max_width="100%", # Evitar que se exceda de las dimesniones de la pantalla
        margin_top=f"{Size.DEFAULT.value}rem",
        style=content_in_the_center_style
    )
