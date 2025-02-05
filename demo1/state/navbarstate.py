import reflex as rx

# Define the state
class NavbarState(rx.State):
    is_logged_in: bool = False

    def toggle_login(self):
        self.is_logged_in = not self.is_logged_in
   

    def logout(self):
        self.is_logged_in = False
        return rx.redirect("/")

    def login(self):
        self.is_logged_in = True
        return rx.redirect("/home")