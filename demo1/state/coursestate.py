from pathlib import Path
import reflex as rx
import requests
from typing import List, Dict
from demo1.models.coursemodel import Data
import json
from reflex_ag_grid import ag_grid

class CourseState(rx.State):
    data: list[Data] = []
    page: int = 1
    page_size: int = 10
    search_query: str = ""
    sort_column: str = "courses"
    sort_ascending: bool = True
    filtered_courses_data: List[Data] = []

  
    @rx.var(cache=True)
    def filtered_courses(self) -> List[Data]:
        if not self.data:
            return []
        filtered = [
            row for row in self.data 
            if self.search_query.lower() in row["name"].lower()  # Changed to match your JSON keys
        ]
        return sorted(
            filtered,
            key=lambda x: getattr(x,self.sort_column, ""),
            reverse=not self.sort_ascending
        )

    @rx.event
    def load_data(self):
        try:
            with open("assets/courses.json", "r") as file:
                data = json.load(file)
                # Extract just the courses list from the JSON structure
                if isinstance(data, dict) and "courses" in data:
                    self.data = data["courses"]  # Set data to the courses list directly
                else:
                    raise ValueError("Invalid data structure in JSON file")
        except Exception as e:
            print(f"Error loading data: {e}")
            self.data = []

    @rx.var
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
    @rx.event
    def toggle_sort(self, column: str):
        """Toggle sorting order on column click."""
        if self.sort_column == column:
            self.sort_ascending = not self.sort_ascending
        else:
            self.sort_column = column
            self.sort_ascending = True