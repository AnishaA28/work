from pathlib import Path
from urllib import response
import reflex as rx
import requests
import logging
from typing import List, Dict

from demo1.models.coursemodel import Data
import json
from reflex_ag_grid import ag_grid
from sqlalchemy.orm import sessionmaker
from demo1.database import engine
from sqlmodel import select
from sqlalchemy.sql.expression import func
from sqlalchemy import or_, func
import http


PREFIX_URL = "http://localhost:3001/"



class CourseState(rx.State):
    token: str =""
    courses: list[Data] = []
    page: int = 1
    page_size: int = 10
    search_query: str = ""
    sort_column: str = "courses"
    sort_ascending: bool = True
    filtered_courses_data: List[Data] = []

    new_course_name: str = ""
    new_course_instructor: str = ""
    new_course_duration: str = ""
    new_course_image: str = ""

    sort_direction = "asc"  # Default sort direction
    sort_column = "name"  # Default sort column
    search_value = ""
    error=""

    @rx.var(cache=True)
    def filtered_courses(self) -> List[Data]:
        if not self.data:
            return []
        filtered = [
            row for row in self.data 
            if self.search_query.lower() in getattr(row, "name", "").lower()  # Changed to match your JSON keys
        ]
        return sorted(
            filtered,
            key=lambda x: getattr(x,self.sort_column, ""),
            reverse=not self.sort_ascending
        )

    def fetch_courses(self, token: str = ""):
       """Fetch courses from the API."""
       url = f"{PREFIX_URL}/courses"
       headers = {"Content-Type": "application/json"}

       if token:
            headers["Authorization"] = f"Token {token}"
            url = f"{PREFIX_URL}/login"

       logging.info("Fetching courses from API...")
       
       try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            self.courses = response.json()
       except requests.exceptions.RequestException as e:
            self.error = f" Error fetching courses: {e}"
    
        

    @rx.var(cache=True)
    def paginated_data(self) -> List[Dict]:
        """Returns paginated data."""
        start = self.page * self.page_size
        end = start + self.page_size
        return self.filtered_courses_data[start:end]
    
    @rx.var
    def total_pages(self) -> int:
        return max(1, (len(self.filtered_courses_data) - 1) // self.page_size + 1)

    

    @rx.var(cache=True)
    def is_first_page(self) -> bool:
        return self.page == 0

    @rx.var(cache=True)
    def is_last_page(self) -> bool:
        return len(self.filtered_courses) <= (self.page + 1) * self.page_size

    @rx.event
    def next_page(self):
        if not self.is_last_page:
            self.page += 1

    @rx.event
    def prev_page(self):
        if not self.is_first_page:
            self.page -= 1
    @rx.event
    def update_search(self, query: str):
        """Update search query and reset pagination."""
        self.search_query = query
        self.page = 0  # Reset to first page when searching
   

    def add_course(self):
        """Add a new course via API."""
        if not self.new_course_name or not self.new_course_instructor or not self.new_course_duration or not self.new_course_image:
            self.error = "Course name and instructor are required!"
            return
        
        course_data = {
            "name": self.new_course_name,
            "instructor": self.new_course_instructor,
            "duration": self.new_course_duration,
            "image":self.new_course_image
        }

        try:
            response = requests.post(f"{PREFIX_URL}/courses", json=course_data)
            response.raise_for_status()
            self.fetch_courses()  # Refresh course list
        except requests.exceptions.RequestException as e:
            self.error = f"Error adding course: {str(e)}"
        
    def delete_course(self, course_id: int):
        """Delete a course via API."""
        try:
            response = requests.delete(f"{PREFIX_URL}/courses/{course_id}")
            response.raise_for_status()
            self.fetch_courses()
        except requests.exceptions.RequestException as e:
            self.error = f"Error deleting course: {str(e)}"

    def select_course(self, course_id: int):
        """Set selected course for editing."""
        self.selected_course = next((c for c in self.courses if c["id"] == course_id), {})

    def update_course(self):
        """Update selected course via API."""
        if not self.selected_course:
            self.error = "No course selected for editing."
            return

        try:
            response = requests.put(
                f"{PREFIX_URL}/courses/{self.selected_course['id']}", json=self.selected_course
            )
            response.raise_for_status()
            self.fetch_courses()
        except requests.exceptions.RequestException as e:
            self.error = f"Error updating course: {str(e)}"
    @rx.event
    def set_new_course_name(self, value: str):
        self.new_course_name = value

    @rx.event
    def set_new_course_instructor(self, value: str):
        self.new_course_instructor = value


    @rx.event
    def set_new_course_duration(self, value: str):
        self.new_course_duration = value

    @rx.event
    def set_new_course_image(self, value: str):
        self.new_course_image = value
        
    
    

    def toggle_sort(column):
        if CourseState.sort_column == column:
            CourseState.sort_direction = rx.cond(
                CourseState.sort_direction == "asc",
                "desc",
                "asc"
            )
        else:
            CourseState.sort_column = column
            CourseState.sort_direction = "asc"
        CourseState.sort_courses()

    @staticmethod
    def sort_courses():
        sorted_courses = sorted(
            CourseState.filtered_courses,
            key=lambda x: getattr(x, CourseState.sort_column),
            reverse=CourseState.sort_direction == "desc"
        )
        CourseState.filtered_courses_data = sorted_courses

    @staticmethod
    def get_sort_symbol(column):
        return rx.cond(
            CourseState.sort_column == column,
            rx.cond(
                CourseState.sort_direction == "desc",
                "▼",
                "▲"
            ),
            ""
        )
    
    @rx.event 
    def load_entries(self) -> list[Data]:
        """Get all courses from the database."""
        with rx.session() as session:
            query = select(Data)
            
            if self.search_value != "":
                search_value = f"%{self.search_value.lower()}%"
                query = query.where(
                or_(
                    func.lower(Data.name).like(func.lower(search_value)),
                    func.lower(Data.instructor).like(func.lower(search_value)),
                    func.lower(Data.duration).like(func.lower(search_value)),
                    func.lower(Data.image).like(func.lower(search_value))
                )
            )
        
        self.data = session.exec(query).all()
    @rx.event
    def get_data(self):
        with rx.session() as session:
             
            return session.exec(
                select(Data)
            ).all()
        
    def get_course(self, course_id: int):
        with rx.session() as session:
             course_id = session.exec(
            select(Data).where(Data.id == course_id)
        ).first()    