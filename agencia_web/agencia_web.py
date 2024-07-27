"""Welcome to Reflex! This file outlines the steps to create a basic app."""

### Importar estilos y vistas para que se vean en la web ###

import reflex as rx
from agencia_web.styles.styles import STYLESHEETS, BASE_STYLE
from agencia_web.views.navbar import navbar
from agencia_web.views.header import header
from agencia_web.views.services import services
from agencia_web.views.pricing import pricing
from agencia_web.views.dashboard import dashboard
from agencia_web.views.contact import contact
from agencia_web.views.footer import footer

def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang = 'es'"),
        navbar(),
        header(),
        services(),
        pricing(),
        dashboard(),
        contact(),
        footer()
    )

app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
)

app.add_page(
    index,
    title="Contentcraft",
    description=
        "Web de la agencia de redacción de contenidos especializados \"Contentcraft\""
    )

app._compile()