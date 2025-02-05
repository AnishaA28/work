import reflex as rx
import bcrypt
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

class User(rx.Base):
    __tablename__ = "users"
    
    email_address = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Store hashed password

    def set_password(self, password: str):
        """Hash and store the password."""
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verify_password(self, password: str) -> bool:
        """Check if entered password matches the hashed password."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
