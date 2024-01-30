"""
This module handles all the layout of the Dash App.

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-30
"""
from __future__ import annotations
from dash import Dash, html
import dash_bootstrap_components as dbc

from layouts.ControlDashboard import ControlDashboard
from layouts.Visualization import Visualization


class MainLayout:

    def __init__(self) -> None:
        self._control_dashboard = ControlDashboard.create()
        self._visualization = Visualization.create()

    def define_layout(self, app: Dash = None) -> None:
        app.layout = dbc.Container(
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
                            width=4,
                            style={"height": "90vh",
                                   "border": "thin lightgrey solid",
                                   "padding": "10px"}
                        ),
                        dbc.Col(
                            self._visualization,
                            width=8,
                            style={"height": "90vh",
                                   "border": "thin lightgrey solid",
                                   "padding": "10px"}
                        ),
                    ]
                )
            ],
            style={"height": "100vh"}, fluid=True)


if __name__ == "__main__":
    app = Dash(__name__)
    app_layout = MainLayout()
    app_layout.define_layout(app=app)
    # Additional setup and running the app
