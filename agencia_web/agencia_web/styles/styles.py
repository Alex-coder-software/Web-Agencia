import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "560px" 

# Sizes

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Roboto:wght@300;500&display=swap" # La fuente que usamos: Roboto
]

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5"
    MEDIUM = "0.8"
    DEFAULT = "1"
    LARGE = "1.5"
    BIG = "2"
    VERY_BIG = "4"
    GIANT = "8"


class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"
    GIANT = "60"

# Styles

BASE_STYLE = { # Hacer que toda la web se vea con el mismo estilo
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    "color": TextColor.BODY.value,
    "breakpoints": ["520px", "768px", "1024px", "1280px", "1640px"],
    rx.heading: { # Estilos predeterminados para cada función que utilizamos
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "--cursor-button": "pointer",
        "_hover": {
            "background_color": Color.SECONDARY.value
        }
    },
    rx.link: {
        "color": TextColor.BODY.value,
        "text_decoration": "none",
        "_hover": {"background_color": Color.SECONDARY.value}
    },
    rx.text: {
        "color": TextColor.BODY.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value        
    },
    rx.table.root: {
        "font_size": "1.2rem"
    }
}

content_in_the_center_style={ # Estilo para alienar elementos al centro
    "display": "flex",
    "justifyContent": "center",
    "flexDirection": "column",
    "textAlign": "center",
    "width": "100%",
    "maxWidth": "100%",
    "alignItems": "center",
    "padding": f"{Size.SMALL.value}rem",  # Padding para centrar el contenido sin ocupar toda la altura
    "height": "auto",  # Altura automática en lugar de 100vh
    "marginLeft": "auto",  # Centrar horizontalmente usando auto margin
    "marginRight": "auto",  # Centrar horizontalmente usando auto margin
    }

link_hover= { # Estilo para el hover de los botones
    "transform": "scale(1.2)",  # Aumentar el tamaño del enlace
    "boxShadow": "0px 4px 15px rgba(0, 0, 0, 0.2)",  # Añadir sombra al pasar el ratón
    "borderRadius": "5px",  # Añadir borde redondeado al pasar el ratón
    "backgroundColor": Color.PRIMARY.value,  # Cambiar el color de fondo al pasar el ratón
    "padding": "5px"  # Añadir padding al pasar el ratón
}

table_style={ # Estilo para las tablas
    "color": TextColor.BODY.value, 
    "border": "1px solid #CCCCCC", 
    "font_size": ["0.6rem", "1rem", "1.2rem"], 
    "padding": "0.5rem", 
    "line-height": "1.2",
    "textAlign": "left"
}

### Estilos para los títulos de diferentes secciones ###

navbar_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_size=Size.LARGE.value
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    color=TextColor.HEADER.value,
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    color=TextColor.BODY.value
)