from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from demo1.models.coursemodel import Base


engine = create_engine('sqlite:///reflex.db')

Base = declarative_base()
Session = sessionmaker(bind=engine)

