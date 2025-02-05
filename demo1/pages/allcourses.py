import reflex as rx
from demo1.components.navbar import navbar_buttons 
from demo1.components.coursetable import course_table
from demo1.state.coursestate import CourseState


@rx.page(route="/courses")
def all_course():
    return rx.vstack(navbar_buttons(),rx.container(
        rx.heading("Welcome to the Course Page!", size="9"),
        rx.text("This is where you can learn more course"),
        rx.box(rx.center(course_table(), height="50vh", on_mount=CourseState.load_data) ,),
    ),
     spacing="1",  # spacing value set here
    padding="10px",
    )  