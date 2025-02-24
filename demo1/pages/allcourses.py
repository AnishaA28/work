import reflex as rx
from demo1.components.navbar import navbar_buttons 
from demo1.components.coursetable import course_table
from demo1.state.coursestate import CourseState


@rx.page(route="/courses")
def all_course():
    return rx.box(rx.box(rx.vstack(navbar_buttons(),),),rx.box(rx.container(
        rx.heading("Welcome to the Course Page!", size="9",align="center"),
        rx.text("This is where you can learn more course",align="center"),),
        background_color="var(--gray-3)",
        width="100%",),
        rx.box(rx.vstack(rx.container(rx.center(course_table(), height="130vh",width="90vw", on_mount=CourseState.fetch_courses()) ,),
    ),),
     spacing="4",  # spacing value set here
    padding="10px",
    
    ), 