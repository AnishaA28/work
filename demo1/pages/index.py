import reflex as rx
from demo1.components.navbar import navbar_buttons 
from demo1.components.drawercom import lateral_menu
from ..state.drawer import DrawerState



        

@rx.page(route="/")
def index_page():
    return rx.vstack(navbar_buttons(),),rx.box(
        rx.container(
        rx.heading("Welcome to All!", size="9"),
        rx.text("This is where you can learn more course"
                ),
        background_color="var(--gray-3)",
        width="100%",),
        rx.vstack(
        lateral_menu(),
        rx.section(
            rx.heading("Chat Area", size="8"),
            id="section1",
            height="900px",
        ),
        rx.section(
            rx.heading("Detail View", size="8"),
            id="section2",
            height="900px",
        )
    ),
                spacing="9",
                padding="1em",
                align="center",
                )
        
     
    