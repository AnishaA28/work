import reflex as rx
from demo1.components.navbar import navbar_buttons 

@rx.page(route="/contact")
def contact_page():
    return rx.vstack(navbar_buttons(),),rx.box(rx.container(rx.center(
    rx.text("Hello World!"),
    border_radius="15px",
    border_width="thick",
    width="100%",
),
        rx.heading("Welcome to the Contact Page!", size="9",align="center"),
        
    ),)
    