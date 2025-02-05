import reflex as rx
from demo1.state.coursestate import CourseState


def course_table():
    return rx.vstack(
        rx.input(
            placeholder="🔍 Search...", 
            value=CourseState.search_query,
            on_change=CourseState.update_search
        ),
        
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Name", on_click=lambda: CourseState.toggle_sort("name"), cursor="pointer"),
                    rx.table.column_header_cell("Instructor", on_click=lambda: CourseState.toggle_sort("name"), cursor="pointer"),
                    rx.table.column_header_cell("Duration",on_click=lambda: CourseState.toggle_sort("name"), cursor="pointer")
                ),
            ),
            rx.table.body(
                rx.foreach(
                    CourseState.filtered_courses,
                    lambda data: rx.table.row(
                        rx.table.cell(data["name"]),
                        rx.table.cell(data["instructor"]),
                        rx.table.cell(data["duration"]),
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
            )
        ),
        on_mount=CourseState.load_data,
        spacing="4",
        width="100%"
    ),