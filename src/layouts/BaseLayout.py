"""
This module handles all the layout of the Dash App.

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-31
"""
from __future__ import annotations
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Container
from dash import html, Dash


class BaseLayout:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(BaseLayout, cls).__new__(cls)
            # Initialize any variables here if necessary
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, 'initialized'):  # This prevents reinitialization
            self._nav_bar = None
            self._view_port = None
            self.initialized = True

    def create_nav_bar(self, content=None):
        self._nav_bar = content

    def create_view_port(self, content=None):
        self._view_port = content

    def update_layout(self) -> Container:
        return (
            dbc.Container(
                [
                    dbc.Row(
                        dbc.Col(
                            [
                                html.Div(
                                    "OD Turning Data Analysis App",
                                    style={"fontSize": 20, "fontWeight": "bold"}
                                )
                            ],
                            width=4
                        ),
                        align="center",
                        justify="center",
                        style={"height": "10vh", "text-align": "center"}
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                self._nav_bar,
                                width=1,
                                style={"height": "90vh", "border": "thin lightgrey solid", "padding": "10px"}
                            ),
                            dbc.Col(
                                self._view_port,
                                width=11,
                                style={"height": "90vh", "border": "thin lightgrey solid", "padding": "10px"}
                            ),
                        ]
                    )
                ],
                style={"height": "100vh"}, fluid=True)
        )


if __name__ == "__main__":
    app = Dash(__name__)
    app_layout = BaseLayout()
    app.layout = app_layout.update_layout()
    # Additional setup and running the app
