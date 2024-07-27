import reflex as rx
from agencia_web.styles.styles import Size

def link_icon(image: str, url: str, alt: str, height="40px", width="55px") -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=width,
            height=height,
            margin_top=f"{Size.MEDIUM.value}rem",
            alt=alt,
            style={
                "transition": "all 0.3s ease"  # Agregar transición para un efecto suave
            }
        ),
        href=url,
        is_external=True
    )