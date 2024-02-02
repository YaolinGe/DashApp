"""
This module handles the layout for the data analysis page

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-31
"""
from __future__ import annotations
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Container

from layouts.LayoutManager import LayoutManager
from layouts.NavBarLayout import update_nav_bar


class ReviewPageLayout:

    def update_view_port(self) -> Container:
        return (
            dbc.Container(
                dbc.Row(
                    [
                        dcc.Interval(
                            id='review-interval-update',
                            interval=60000,  # in milliseconds (e.g., 60000ms = 60s)
                            n_intervals=0
                        ),
                        dbc.Col(
                            children=[
                                html.Div(id="review-graph")
                            ],
                            style={
                                "width": "95vw",
                                "height": "80vh",
                                "overflow": "auto",
                            }
                        )
                    ],
                    style={
                        "height": "85vh",
                    }
                )
            )
        )

    def layout(self) -> Container:
        return LayoutManager.update_page_layout(update_nav_bar(activate_page="Review"), self.update_view_port())


if __name__ == "__main__":
    app = Dash(__name__)
    app_layout = ReviewPageLayout()
    app.layout = app_layout.layout()
    # Additional setup and running the app
