from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Static, Button, Input, TextLog
import requests

API_URL = "http://localhost:5000/api"

class TUIFrontEnd(App):
    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("TUI for REST Services", id="header")
        yield Button("View Appointments", id="view_btn")
        yield Button("Add Appointment", id="add_btn")
        yield Button("Delete Appointment", id="delete_btn")
        yield Input(placeholder="Enter JSON for POST / ID for DELETE", id="input")
        yield TextLog(id="output", highlight=True)

    def on_button_pressed(self, event):
        btn_id = event.button.id
        user_input = self.query_one("#input").value
        output_log = self.query_one("#output")

        try:
            if btn_id == "view_btn":
                response = requests.get(f"{API_URL}/appointments")
                output_log.write(response.json())
            elif btn_id == "add_btn":
                data = eval(user_input)  # Example: {"patient_name": "John", "date": "2024-12-04", "time": "10:00", "reason": "Checkup"}
                response = requests.post(f"{API_URL}/appointments", json=data)
                output_log.write(response.json())
            elif btn_id == "delete_btn":
                response = requests.delete(f"{API_URL}/appointments/{user_input}")
                output_log.write(response.json())
        except Exception as e:
            output_log.write(f"Error: {e}")

if __name__ == "__main__":
    TUIFrontEnd.run()

