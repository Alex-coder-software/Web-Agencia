import reflex as rx
from agencia_web.styles.styles import Size, content_in_the_center_style
from agencia_web.styles.styles import Color
from agencia_web.styles.fonts import FontWeight
import agencia_web.constants as constants

def dashboard() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Portafolio",
                size=Size.GIANT.value,  
                font_size=FontWeight.MEDIUM.value,
                margin_top=f"{Size.VERY_BIG.value}rem",
                style=content_in_the_center_style
            ),
            rx.box(
                rx.text(
                    "¡Así son nuestros resultados! Estos son nuestros proyectos personales destacados para que previsualices algunos resultados."
                ),
                style=content_in_the_center_style
            ),
            rx.hstack(
                rx.vstack(
                    rx.box(
                        rx.link(
                            rx.image(
                                src="project_1.jpg",
                            ),
                            href=constants.PROJECT_1_URL,
                            is_external=True
                        ),
                        radius="full", # Para hacer borde
                        border=f"4px solid {Color.PRIMARY.value}", # Para hacer borde
                    ),
                    rx.heading(
                        "Voces del Fútbol Sala",
                        margin_left=["0px !important", "0px !important", "270px", "270px", "270px"],
                    ),
                    rx.text(
                        """\"Voces del Fútbol Sala\" es una inspiradora colección de citas de figuras influyentes en el mundo del futsal. 
                        Con 12 páginas, este ebook ofrece una visión íntima de los pensamientos y emociones de jugadores y entrenadores 
                        como Ferrao, Ricardinho, o Javier Limones. Cada cita ha sido seleccionada para proporcionar una perspectiva única 
                        y enriquecer la comprensión del fútbol sala. Disponible gratuitamente en Wattpad, este proyecto celebra el futsal y 
                        busca inspirar a aficionados y jugadores por igual con las palabras de aquellos que viven y respiran este deporte.""",
                    ),
                    margin_left="0.4rem",
                    width="60%",
                    max_width="40%",
                ),
                rx.vstack(
                    rx.box(
                        rx.link(
                            rx.image(
                                src="project_2.jpg",
                            ),
                            href=constants.PROJECT_2_URL,
                            is_external=True
                        ),
                        radius="full", # Para hacer borde
                        border=f"4px solid {Color.PRIMARY.value}" # Para hacer borde
                    ),
                    rx.heading(
                        "De las Canchas al Corazón",
                        margin_left=["0px !important", "0px !important", "270px", "270px", "270px"],
                    ),
                    rx.text(
                        """\"De las Canchas al Corazón: Biografías Inspiradoras del Fútbol Sala\" es un eBook que recoge las historias de vida de ocho 
                        de los jugadores más influyentes en la historia del fútbol sala. Desde sus humildes comienzos hasta sus grandes logros, se destacan 
                        figuras como Falcão, Ricardinho y Kike Boned. Este eBook presenta no solo sus logros deportivos, sino también sus momentos personales 
                        y anécdotas. Con un diseño atractivo y redacción amena, está pensado para inspirar a aficionados y jugadores de fútbol sala en todo el 
                        mundo. Descubre más en mi portafolio.""",
                    ),
                    margin_left=Size.ZERO.value,
                    width="60%",
                    max_width="40%",
                ),
                margin_top=f"{Size.SMALL.value}rem",
                spacing="0.2rem",  # Añade un poco de espacio entre las columnas
                justify_content="space-around",  # Asegura que las columnas estén espaciadas uniformemente
                width="100%",  # Asegura que el contenedor ocupe todo el ancho disponible
                columns=[1, 2]
            ),
        ),
        max_width="100%", 
        style=content_in_the_center_style # En esta sección hemos eliminado muchas líneas gracias a content_in_the_center_style
    )