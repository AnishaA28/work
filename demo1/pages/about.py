import reflex as rx
from demo1.components.navbar import NavbarState, navbar_buttons 


class CondState(rx.State):
    page: str = ""

    def set_page(self, new_page: str):
        self.page = new_page


@rx.page(route="/about")
def about_page():
    return rx.vstack(navbar_buttons(),rx.container(
        rx.heading("Welcome to the About Page!", size="9"),
        rx.text("This is where you can learn more about us."),
        rx.script(
        "window.__page = '/about'",  # Inline script
        on_ready=CondState.set_page("/about")
    )
    ),
    )   
