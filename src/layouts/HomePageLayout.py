"""
This module handles the layout for the home page

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-30
"""
from __future__ import annotations
import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Container

from layouts.ControlDashboard import ControlDashboard


class HomePageLayout:

    def __init__(self) -> None:
        self._control_dashboard = ControlDashboard.create()

    def layout(self) -> Container:
        layout = dbc.Container(
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
                            self._control_dashboard,
                            style={"height": "90vh",
                                   "border": "thin lightgrey solid",
                                   "padding": "10px"}
                        ),
                    ]
                ),
                dbc.Row(
                    dbc.Col(
                    )
                )
            ],
            style={"height": "100vh"}, fluid=True)
        return layout


if __name__ == "__main__":
    app = Dash(__name__)
    app_layout = HomePageLayout()
    app.layout = app_layout.layout()
    # Additional setup and running the app
