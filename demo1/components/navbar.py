import reflex as rx
from demo1.state.auth_state import AuthState
from demo1.state.navbarstate import NavbarState



def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"),
        href=url,
        color="Blue",
        size="3",
        variant="outline",
        _hover={"text_decoration": "underline"},
    )

def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Anisha", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("About", "/about"),
                    navbar_link("Course", "/course"),
                    navbar_link("Contact", "/contact"),
                    rx.cond(NavbarState.is_logged_in,navbar_link("AllCourse", "/courses")),
                    spacing="5",),
                    rx.cond(
                    ~NavbarState.is_logged_in,
                    rx.hstack(
                        rx.link("Sign Up", href="/signup",color="Blue"),
                        rx.link("Login", href="/login", on_click=NavbarState.login,color="Blue"),
                        spacing="4",
                    ),
                ),
                # Conditionally render Logout button
                rx.cond(
                    NavbarState.is_logged_in,
                    
                    rx.button("Logout", on_click=NavbarState.toggle_login),
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Anisha", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Course"),
                        rx.menu.item("Contact"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )