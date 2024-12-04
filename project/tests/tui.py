from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Static, Button, Input
import requests

API_URL = "http://localhost:5000/api"

class TUIFrontEnd(App):
    CSS = """
    Screen {
        align: center middle;
    }
    Static#output {
        border: round green;
        padding: 1;
        height: 10;
        overflow: scroll;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("TUI for REST Services", id="header")
        yield Button("View Appointments", id="view_btn")
        yield Button("Add Appointment", id="add_btn")
        yield Button("Delete Appointment", id="delete_btn")
        yield Input(placeholder="Enter JSON for POST / ID for DELETE", id="input")
        yield Static("Output will appear here...", id="output")

    def on_button_pressed(self, event):
        btn_id = event.button.id
        user_input = self.query_one("#input").value
        output_widget = self.query_one("#output")

        try:
            if btn_id == "view_btn

