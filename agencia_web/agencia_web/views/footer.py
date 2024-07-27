import reflex as rx
from agencia_web.styles.styles import Size
import agencia_web.constants as constants
from agencia_web.components.link_icon import link_icon

def footer() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.hstack(
                rx.text(
                    "© 2024 Agencia Contentcraft | Todos los derechos reservados.",
                    margin_left=f"{Size.SMALL.value}rem"
                ),
                rx.box(
                    link_icon(
                        "github.png",
                        constants.GITHUB_URL,
                        "Logo de Github",
                        height="30px",  # Ajustar el tamaño para mejor alineación
                        width="40px"
                    ),
                    margin_y=f"{Size.ZERO.value}rem",
                    margin_left=f"{Size.SMALL.value}rem"  # Ajustar margen izquierdo para separación
                ),
                margin_y=f"{Size.SMALL.value}rem",
                alignItems="center",  # Asegurar que el contenido esté centrado verticalmente
            ),
        ),
        style={ # Estilo ligeramente distinto al content_in_the_center_style, para que el logo esté , más cerca del texto
            "display": "flex",
            "justifyContent": "start",
            "flexDirection": "row",
            "textAlign": "start",
            "width": "100%",
            "max-width": "100%",
            "alignItems": "start",
            "padding": f"{Size.SMALL.value}rem",  # Padding para centrar el contenido sin ocupar toda la altura
            "height": "auto",  # Altura automática en lugar de 100vh
            "marginLeft": "auto",  # Centrar horizontalmente usando auto margin
            "marginRight": "auto",  # Centrar horizontalmente usando auto margin
        }
    )