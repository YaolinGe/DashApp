"""
This module defines the visualization part of the dash app.

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-30
"""

from dash import html, dcc
import dash_bootstrap_components as dbc


class Visualization:
    @staticmethod
    def create():
        return (
            dbc.Row(
                [
                    dbc.Row(
                        dbc.Col(
                            html.Div(
                                "Visualization",
                                style={"fontSize": 16,
                                       "fontWeight": "bold",
                                       "text-align": "center"}
                            )
                        ),
                        style={"height": "5vh",
                               "text-align": "center"}
                    ),
                    dbc.Row(
                        dbc.Col(
                            dcc.Loading(
                                id="loading-output",
                                children=[html.Div(id="output")],
                                type="default",  # You can choose from 'graph', 'cube', 'circle', 'dot', or 'default'
                            ),
                        ),
                        style={"padding": "10px"}
                    )
                ]
            )
        )
