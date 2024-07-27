import reflex as rx
from agencia_web.components.link_icon import link_icon
import agencia_web.constants as constants
from agencia_web.styles.styles import Size
from agencia_web.styles.colors import Color

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.image(
                    src="logo_agencia.jpg",
                    height="70px", #Ajustar la imagen para que se vea más bien pequeña, ya que no quiero una navbar grande
                    width="90px",
                    margin_left=f"{Size.SMALL.value}rem"
                ),
                rx.text(
                    "Contentcraft, agencia de contenidos especializados",
                    margin_top=f"{Size.LARGE.value}rem", # No hacer margin_y para que se despegue del techo pero no del suelo
                    padding=Size.BIG.value,
                    trim="normal",
                    align="center",
                    font_size=["0.8rem", "0.8rem", "1rem", "1rem"],  # Ajustar tamaño de texto para móviles
                ),
                margin_y=f"{Size.MEDIUM.value}rem",
                margin_right="auto",
                margin_left=["70px", "80px", "auto", "auto", "auto"] # En móvil queremos que se ajuste al centro, ya que es lo único que habrá en la navbar
            ),
            rx.spacer(flex=1),
            rx.center(
                rx.hstack(
                    link_icon(
                        "fiverr.jpg",
                        constants.FIVERR_URL,
                        "Logo de fiverr"    
                    ),
                    link_icon(
                        "upwork.jpg",
                        constants.UPWORK_URL,
                        "Logo de upwork",
                        "50px" # Ajustar imágenes ya que algunas son muy grandes (Esto se corrigiría con un diseñador especializado)
                    ),
                    link_icon(
                        "workana.jpg",
                        constants.WORKANA_URL,
                        "Logo de workana",
                    ),
                    link_icon(
                        "instagram.png",
                        constants.INSTAGRAM_URL,
                        "Logo de instagram",
                        "40px"
                    ),
                    link_icon(
                        "linkedin.png",
                        constants.LINKEDIN_URL,
                        "Logo de linkedin",
                        "50px"
                    ),
                    link_icon(
                        "tiktok.png",
                        constants.TIKTOK_URL,
                        "Logo de tiktok",
                        "40px"
                    ),
                    link_icon(  
                        "twitter.png",
                        constants.TWITTER_URL,
                        "Logo de twitter"
                    ),
                margin_y=f"{Size.SMALL.value}rem",
                justify="center",
                margin_left="850px",  # Despegar ambos componentes de la barra
                width="30%",  # Para que no ocupe toda la navbar 
                ),
            ),
        ),
        z_index="9999", # Asegurarse de que la navbar esté en la parte superior
        position="fixed",
        border_bottom=f"0.45rem solid {Color.SECONDARY.value}", # Línea inferior azul de la navbar
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        top="0",
        left="0",  
        right="0", 
        width="100%",
        background_color=Color.BACKGROUND.value, # Asegurar que la navbar tiene un fondo opaco, lo cual es crucial para evitar que otros elementos la atraviesen visualmente
    )