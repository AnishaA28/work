# pages/state.py
import logging
import reflex as rx
from demo1.models.user import User
from passlib.context import CryptContext
from sqlalchemy.orm import sessionmaker
from demo1.database import engine
import requests

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
PREFIX_URL = "http://localhost:3000"

class AuthState(rx.State):
    """The auth state."""
    # Base vars for tracking login status and user info
    
    email_address: str = ""
    password: str = ""
    error_message: str = ""
    token:str=""
    user: dict = {} # Store user details
    is_authenticated: bool = False
    error: str = ""   
    
    new_email: str = ""
    new_password: str = ""


    @rx.var(cache=True)  # Enable caching for this computed property
    def is_logged_in(self) -> bool:
        """Check if user is logged in."""
        return self.is_authenticated

    def set_email_address(self, value: str):
        self.email_address = value

    is_logged_in: bool = False
    @rx.event
    def login(self):
        print("calling login")
        """Method to handle user login via API."""
        self.error = ""  # Clear errors
        url = f"{PREFIX_URL}/login"
        payload = {"email": self.email_address, "password": self.password}
        headers = {"Content-Type": "application/json"}
        print("payload",payload)
        try:
            print("url",url)    
            response = requests.post(url, json=payload, headers=headers)
            print(response)
            response.raise_for_status()  # Raise error for bad status
            
            data = response.json()
            self.token = data.get("token")

            if not self.token:
                self.error = "Invalid credentials"
                return

            self.is_authenticated = True  # Mark user as authenticated
            logging.info(f"User logged in: {self.email_address}")

            # ✅ Redirect to Home Page after successful login
            return rx.redirect("/home")

        except requests.RequestException as e:
            print(e)
            self.error = f"Login failed: {str(e)}"

    @rx.event
    def signup(self):
        
        """Signup API call."""
        url = f"{PREFIX_URL}/register"
        payload = {"email": self.email_address, "password": self.password}
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()

            data = response.json()
            self.token = data.get("token")

            if not self.token:
                self.error = "Signup failed. Try again."
        

            self.user = data.get("email", {})
            self.is_authenticated = True

            logging.info(f"User signed up: {self.user.get('email', '')}")

        except requests.RequestException as e:
            self.error = f"Signup failed: {str(e)}"


    @rx.event
    def logout(self):
        """Handle logout."""
        self.is_authenticated = False
        self.email_address = ""
        self.password = ""
        return rx.redirect("/")
    

    @rx.event
    def require_auth(self):
        """Check if user is authenticated."""
        if not self.is_authenticated:
            return rx.redirect("/home")
    
    

    def toggle_login(self):
        self.is_logged_in = not self.is_logged_in
   

   