
from passlib.context import CryptContext
from reflex import Base
import bcrypt
from sqlalchemy import Column, Integer, String
from demo1.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

   
    def verify_password(plain_password, hashed_password):
        from passlib.context import CryptContext
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.verify(plain_password, hashed_password)
    
    def set_password(self, password: str):
        """Hash and store the password."""
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')