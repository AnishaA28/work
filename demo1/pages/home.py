import reflex as rx
from demo1.components.navbar import navbar_buttons
from ..state.auth_state import AuthState



        

@rx.page(route="/home", on_load=AuthState.require_auth)
def home_page():
    return rx.vstack(navbar_buttons(),
        rx.vstack(
        
        rx.box(
            rx.container(
                rx.vstack(
                    rx.text("Netphenix", size="9", weight="bold", color="blue.600"),
                    rx.text("This is where you can learn more course", size="6", weight="medium", color="gray.700"),
                    
                    
                    rx.hstack(
                        rx.flex(rx.card(
                            rx.vstack(
                                rx.text("Start Now", size="5", weight="bold", color="blue.600"),
                                rx.text("Free access to Course"),
                            ),
                            padding="1.5em",
                            border_radius="lg",
                            shadow="lg",
                            bg="white",
                            cursor="pointer",
                            _hover={"bg": "blue.50"},
                            on_click=lambda: rx.redirect("/courses"),
                        ),
                        rx.card(
                            rx.vstack(
                                rx.text("My App", size="5", weight="bold", color="blue.600"),
                                rx.text("Achieve your career goals"),
                            ),
                            padding="1.5em",
                            border_radius="lg",
                            shadow="lg",
                            bg="white",
                            cursor="pointer",
                            _hover={"bg": "blue.50"},
                           
                        ),
                        rx.card(rx.vstack(
                            rx.text("App1",size="5", weight="bold", color="blue.600"),
                            rx.text("Achieve your career goals"),),
                                padding="1.5em",
                                border_radius="lg",
                                shadow="lg",
                                bg="white",
                                cursor="pointer",
                                _hover={"bg": "blue.50"},
                                
                        ),
                        rx.card(rx.inset(
                                      rx.image(
                                            src="/logo.png",
                                            width="100%",
                                           height="auto",
                                           align="center",
                                        ),
                                      side="top",
                                    pb="current",
                                    ),
                          
                        ),
                        
                        spacing="5",
                    ),
                   
                    width="100%",
                    ),
                    spacing="6",
                    align="center",
                    wrap="wrap"
                ),
                rx.container(rx.vstack(rx.grid(
                                rx.foreach(
                                rx.Var.range(12),
                                lambda i: rx.card(f"Card {i + 1}", height="10vh"),
                        ),
                        columns="3",
                        spacing="4",
                        width="100%",
                        wrap="wrap",
                        ),),),
                align="center",
                padding="5em",
               
            ),
            bg="linear-gradient(to bottom, #E3F2FD, white)",  
            width="100%",
            height="80vh",
            justify="center",
            align="center",
           
        ),
        
        bg="white",
        width="100%",
       
    ), ),