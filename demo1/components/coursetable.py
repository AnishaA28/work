import reflex as rx
from demo1.state.coursestate import CourseState


def course_table():
    return rx.vstack(
        rx.input(
            placeholder="🔍 Search...", 
            value=CourseState.search_query,
            on_change=CourseState.update_search
        ),
        rx.hstack(
            rx.input(
                placeholder="Name",
                value=CourseState.new_course_name,
                on_change=lambda e: CourseState.set_new_course_name(e)
            ),
            rx.input(
                placeholder="Instructor",
                value=CourseState.new_course_instructor,
                on_change=lambda e: CourseState.set_new_course_instructor(e)
            ),
            rx.input(
                placeholder="Duration",
                value=CourseState.new_course_duration,
                on_change=lambda e: CourseState.set_new_course_duration(e)
            ),
            rx.input(
                placeholder="Image URL",
                value=CourseState.new_course_image,
                on_change=lambda e: CourseState.set_new_course_image(e)
            ),
            rx.button("Add", on_click=CourseState.add_course),
            spacing="4"
        ),
        
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell(rx.text(f"Name {CourseState.get_sort_symbol('name')}"), on_click=lambda: CourseState.toggle_sort("name"), cursor="pointer"),
                    rx.table.column_header_cell(rx.text(f"Instructor {CourseState.get_sort_symbol('instructor')}"), on_click=lambda: CourseState.toggle_sort("instructor"), cursor="pointer"),
                    rx.table.column_header_cell(rx.text(f"Duration {CourseState.get_sort_symbol('duration')}"), on_click=lambda: CourseState.toggle_sort("duration"), cursor="pointer"),
                    rx.table.column_header_cell(rx.text(f"Image {CourseState.get_sort_symbol('image')}"), on_click=lambda: CourseState.toggle_sort("image"), cursor="pointer"),
                    rx.table.column_header_cell("Actions"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    CourseState.courses,
                    lambda data: rx.table.row(
                        rx.table.cell(data["name"]),
                        rx.table.cell(data["instructor"]),
                        rx.table.cell(data["duration"]),
                        rx.table.cell(rx.image(
                            src=data["image"],
                            height="60px",
                            width="60px",
                            border_radius="md"
                        )),
                        rx.table.cell(rx.button("Delete", on_click=lambda: CourseState.delete_course(data["id"])),),
                        rx.table.cell(rx.button("Edit", on_click=lambda: CourseState.select_course(data["id"])),),
                        
                    ),
                ),
            ),
            variant="surface",
            size="3",
            width="100%"
        ),
        rx.hstack(
            rx.button(
                "Previous",
                on_click=CourseState.prev_page,
                is_disabled=CourseState.is_first_page
            ),  
            rx.text(f"Page {CourseState.page} of {CourseState.total_pages}"),
            rx.button(
                "Next", 
                on_click=CourseState.next_page,
                is_disabled=CourseState.is_last_page
            ),
            
        
        ),
        on_mount=CourseState.fetch_courses(""),
        spacing="4",
        width="100%"
    )
