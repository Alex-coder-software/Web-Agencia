import reflex as rx
import agencia_web.styles.styles as styles
from agencia_web.styles.styles import Size, Spacing, content_in_the_center_style
from agencia_web.styles.colors import Color

def link_button(title: str, body: str, url: str, is_external=True, highlight_color=None, animated=False) -> rx.Component:
    return rx.button( # Función button para hacerlo más vistoso
        rx.hstack(
            rx.vstack(
                rx.text(
                    title,
                    size=Spacing.SMALL.value,
                    style=styles.button_title_style # Automatizamos el tamaño y los estilos para ahorrar trabajo al usarlo 
                ),
                rx.text(
                    body,
                    size=Spacing.VERY_SMALL.value,
                    style=styles.button_body_style # Automatizamos el tamaño y los estilos para ahorrar trabajo al usarlo
                ),
                align_items="start",
                spacing=Spacing.VERY_SMALL.value,
                margin_y=Size.SMALL.value,
                margin_right=Size.SMALL.value,
                margin_left=Size.SMALL.value
            ),
            align="center",
            width="100%",
            style=content_in_the_center_style # Automatizamos el tamaño y los estilos para ahorrar trabajo al usarlo
        ),
        border=f"{'2px' if highlight_color != None else '0px'} solid {highlight_color}", # Con implementación de css está sección podría ser válida, pero en este caso no la usamos
        class_name=styles.BOUNCEIN_ANIMATION if animated else None,
        on_click=rx.redirect(path=url, external=is_external),
        bg=Color.SECONDARY.value
    )