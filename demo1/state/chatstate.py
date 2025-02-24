import reflex as rx


class ChatState(rx.State):
    """Define the app state."""
    question: str = ""  # Initialize with empty string
    chat_history: list[tuple[str, str]] = []  # Initialize empty list

    @rx.event
    def handle_change(self, value: str):
        """Handle changes to the input."""
        self.question = value

    @rx.event
    async def handle_submit(self):
        """Handle the form submission."""
        if self.question:
            answer = "This is a response"
            self.chat_history.append((self.question, answer))
            self.question = ""

    @rx.event
    def clear_history(self):
        """Clear the chat history."""
        self.chat_history = []        
        