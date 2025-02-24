import reflex as rx
from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import Field

Base = declarative_base() 

class Data(rx.Model, table=True):
    """The course model."""
    id: int = Field(default=None, primary_key=True)
    name: str
    instructor: str 
    duration: str
    image: str
   