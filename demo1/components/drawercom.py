import reflex as rx
from ..state.drawer import DrawerState

def drawer_content():
    return rx.drawer.content(
        rx.flex(
            rx.drawer.close(
                rx.button(
                    "Close",
                    on_click=DrawerState.toggle_drawer,
                )
            ),
            rx.link(
                "Chat",
                href="#section1",
                on_click=DrawerState.toggle_drawer,
            ),
            rx.link(
                "Detail",
                href="#section2",
                on_click=DrawerState.toggle_drawer,
            ),
            align_items="start",
            direction="column",
        ),
        height="100%",
        width="20%",
        padding="2em",
        background_color=rx.color("mauve", 7),
    )

def lateral_menu():
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.button(
                "View More",
                on_click=DrawerState.toggle_drawer,
            )
        ),
        rx.drawer.overlay(),
        rx.drawer.portal(drawer_content()),
        open=DrawerState.is_open,
        direction="left",
        modal=False,
    )