"""
This module handles all the layout of the Dash App.

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-31
"""
from __future__ import annotations
from dash import Dash, html
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Container


class BaseLayout:

    def __init__(self) -> None:
        self._nav_bar = None
        self._view_port = None

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
                                    style={"fontSize": 20,
                                           "fontWeight": "bold"}
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
                                style={"height": "90vh",
                                       "border": "thin lightgrey solid",
                                       "padding": "10px"}
                            ),
                            dbc.Col(
                                self._view_port,
                                width=11,
                                style={"height": "90vh",
                                       "border": "thin lightgrey solid",
                                       "padding": "10px"}
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
