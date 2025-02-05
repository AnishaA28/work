import reflex as rx
from ..models.user import User
from passlib.context import CryptContext

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthState(rx.State):
    """The auth state."""
    # Base vars for tracking login status and user info
    is_authenticated: bool = False
    email_address: str = ""
    password: str = ""
    error_message: str = ""

 
    
    @rx.var(cache=True)  # Enable caching for this computed property
    def is_logged_in(self) -> bool:
        """Check if user is logged in."""
        return self.is_authenticated
    
    def set_email_address(self, value: str):
        self.email_address = value
    
    @rx.event
    def login(self):
        """Handle login."""
        try:
            with rx.session() as session:
                user = session.query(User).filter(
                    User.email_address == self.email_address
                ).first()
                
                if user and User.verify_password(self.password, User.password):
                    self.is_authenticated = True
                    self.error_message = ""
                    return rx.redirect("/home")
                else:
                    self.error_message = "Invalid username or password"
                    self.is_authenticated = False
        except Exception as e:
            self.error_message = "An error occurred during login"
            print(f"Error: {e}")

    @rx.event
    def signup(self):
        """Handle signup."""
        try:
            with rx.session() as session:
                # Check if user already exists
                existing_user = session.query(User).filter(
                    User.email_address == self.email_address
                ).first()
                
                if existing_user:
                    self.error_message = "Email already exists"
                    return rx.redirect("/login")  # Redirect to signup page with error message
                
                # Hash password
                hashed_password = pwd_context.hash(self.password)
                
                # Create new user
                new_user = User(
                    email_address=self.email_address,
                    password=hashed_password
                )
                session.add(new_user)
                session.commit()
                
                # Log user in after signup
                self.is_authenticated = True
                self.error_message = ""
                return rx.redirect("/")  # Redirect to home page after successful signup
        except Exception as e:
            self.error_message = "An error occurred during signup"
            print(f"Error: {e}")

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