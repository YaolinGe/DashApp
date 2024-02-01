"""
This module handles the layout for the home page

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-30
"""
from __future__ import annotations
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Container

from layouts.LayoutManager import LayoutManager
from layouts.FileUploaderLayout import FileUploaderLayout
from layouts.NavBarLayout import update_nav_bar


class HomePageLayout:

    def update_view_port(self) -> Container:
        return (
            dbc.Container(
                [
                    html.Div(
                        [
                            html.Div(
                                dcc.Loading(
                                    id="loading-output",
                                    children=[html.Div(id="output")],
                                    type="circle",  # You can choose from 'graph', 'cube', 'circle', 'dot', or 'default'
                                ),
                                id="upload-div",
                                style={
                                    "padding": "10px",
                                    "border": "thin lightgrey solid",
                                    "height": "35vh",
                                    "text-align": "center",
                                    "margin": "auto",
                                    "display": "flex",
                                    "justifyContent": "center",
                                    "alignItems": "center",
                                    "backgroundColor": "lightYellow",
                                    "overflow": "auto"
                                }
                            )
                        ],
                    ),
                    FileUploaderLayout.create(),
                ]
            )
        )

    def layout(self) -> Container:
        return LayoutManager.update_page_layout(nav_bar_content=update_nav_bar(activate_page="Home"),
                                                view_port_content=self.update_view_port())


if __name__ == "__main__":
    app = Dash(__name__)
    app_layout = HomePageLayout()
    app.layout = app_layout.layout()
    # Additional setup and running the app
