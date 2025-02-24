import reflex as rx
from demo1.components.navbar import navbar_buttons 
from demo1.components.coursetable import course_table
from demo1.state.coursestate import CourseState
from demo1.state.auth_state import AuthState



@rx.page(route="/course")

def course_page() -> rx.Component:
    return rx.vstack(
        navbar_buttons(),
        rx.container(
            rx.box(
                rx.heading("📚 Explore Our Courses", size="9", weight="bold"),
                rx.text(
                    "Welcome to the course page! Discover a variety of high-quality courses "
                    "designed to enhance your skills and knowledge.",
                    size="5",
                    color="gray",
                ),
                spacing="4",
                padding="1em",
                align="center",
            ),
            
            # Conditional Rendering for Course Table
            rx.cond(
                AuthState.is_logged_in,
                rx.box(
                    rx.card(
                        rx.heading("Available Courses", size="7", weight="bold"),
                        rx.divider(),
                        rx.center(
                            course_table(), 
                            height="auto", 
                            on_mount=CourseState.fetch_courses
                        ),
                        padding="2em",
                        shadow="lg",
                        border_radius="lg",
                        bg="white",
                    ),
                    margin_top="2em",
                ),
                rx.box(
                    rx.text(
                        "🔒 You must be logged in to view the courses.",
                        size="5",
                        color="red",
                        align="center",
                    ),
                    rx.button(
                        "Log In",
                         on_click=rx.redirect("/login"),
                        variant="solid",
                        color_scheme="purple",
                        size="3",
                        margin_top="1em",
                    ),
                    align="center",
                    padding="2em",
                ),
            ),
        ),
        spacing="3",
        padding="2em",
        bg="gray.50",
        height="100vh",
        align_items="center",
        justify_content="center",
    )