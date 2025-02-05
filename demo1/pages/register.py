import reflex as rx
from ..state.auth_state import AuthState


@rx.page(route="/register")
def signup() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                rx.flex(
                    rx.image(
                        src="/logo.png",
                        width="2.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Create an account",
                        size="6",
                        as_="h2",
                        width="100%",
                    ),
                ),
                rx.form(  # Form wrapper here
                    rx.vstack(  # VStack inside form
                        rx.text(
                            "Email address",AuthState.email_address,
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="Email",
                            name="email_address",  # This name must match what you're accessing
                            is_required=True,
                            type="email",
                            size="3",
                            width="100%",
                            on_change=AuthState.set_email_address,
                            value=AuthState.email_address
                        ),
                        rx.text(
                            "Password",
                            size="3",
                            weight="medium",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock")),
                            placeholder="Enter your password",
                            type="password",
                            name="password",
                            size="3",
                            width="100%",
                        ),
                        rx.button(
                            "Register",on_click=AuthState.signup,
                            type="submit",
                            size="3",
                            width="100%",
                        ),
                    ),
                    on_submit=AuthState.signup,  # on_submit goes here
                    reset_on_submit=True,
                ),
                # Social buttons section
                rx.hstack(
                rx.divider(margin="0"),
                rx.text(
                    "Or continue with",
                    white_space="nowrap",
                    weight="medium",
                ),
                rx.divider(margin="0"),
                align="center",
                width="100%",
            ),
            rx.center(
                rx.icon_button(
                    rx.icon(tag="github"),
                    variant="soft",
                    size="3",
                ),
                rx.icon_button(
                    rx.icon(tag="facebook"),
                    variant="soft",
                    size="3",
                ),
                rx.icon_button(
                    rx.icon(tag="twitter"),
                    variant="soft",
                    size="3",
                ),
                spacing="4",
                direction="row",
                width="100%",
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="28em",
        width="100%",
        bg="blue",
    ),),