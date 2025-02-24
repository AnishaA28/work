import reflex as rx
from demo1.components.navbar import navbar_buttons 
from demo1.components.drawercom import lateral_menu
from ..state.drawer import DrawerState
from ..components.chatbox import chat,action_bar



        

@rx.page(route="/")
def index_page():
    return rx.vstack(navbar_buttons(),),rx.box(
        rx.container(
        rx.heading("Welcome to All!", size="9",align="center"),
        rx.text("This is where you can learn more course",align="center"
                ),
        background_color="var(--gray-3)",
        width="100%",),
        rx.vstack(
        lateral_menu(),
        rx.section(
            rx.heading("Chat Area", size="8"),
            rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
        ),
    ),
            id="section1",
            height="900px",
        ),
        rx.divider(),
        rx.section(
            rx.heading("Placement&Pricing", size="8"),
            rx.scroll_area(
    rx.flex(
        rx.text(
            """Placement Guidance
Benefit from real-time interview experiences, placement guidance & mentorship from top industry professionals to confidently navigate your job search.
""",
        ),
       
        direction="column",
        spacing="4",
    ),
    type="always",
    scrollbars="vertical",
    style={"height": 180},),
            id="section2",
            height="900px",
        )
    ),
                spacing="9",
                padding="1em",
                align="center",
                )
        
     
    