"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from .pages.about import about_page

from .pages.index import index_page

from .pages.login import login

from .pages.register import signup

from .pages.course import course_page

from .pages.contact import contact_page
from .pages.allcourses import all_course
from .models.coursemodel import Data



from .pages.home import home_page

from .components.coursetable import course_table







#urls
async def api_test(item_id: int):
    return {"my_result": item_id}

app = rx.App()
app.api.add_api_route("/items/{item_id}", api_test)






app.add_page(about_page, route="/about")
app.add_page(index_page, route="/")
app.add_page(home_page, route="/home")
app.add_page(login, route="/login")
app.add_page(signup, route="/signup")
app.add_page(course_page, route="/course")
app.add_page(contact_page, route="/contact")
app.add_page(all_course, route="/courses")

app.add_page(course_table)






