"""
This module defines the control dashboard for the dash app.

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-30
"""
import os
from controller.paths import datafolder_path

from dash import html, dcc
import dash_bootstrap_components as dbc


class FileUploaderLayout:

    @staticmethod
    def create():
        return (
            dbc.Container(
                [
                    dbc.Row(
                        html.Div(
                            "Upload Data Files",
                            style={"fontSize": 16,
                                   "fontWeight": "bold",
                                   "text-align": "center"}
                        ),
                        align="center",
                        style={"height": "5vh",
                               "text-align": "center"}
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Upload(
                                    id='datafiles',
                                    children=html.Div(
                                        [
                                            'Drag and Drop or ',
                                            html.A('Select Files')
                                        ],
                                        style={"height": "100%"}
                                    ),
                                    multiple=False,
                                    style={
                                        "border": "solid",
                                        "borderRadius": "50px",
                                        "borderStyle": "dashed",
                                        "height": "10vh",
                                        "backgroundColor": "blue",
                                        "text-align": "center",
                                        "display": "grid",
                                        "place-content": "center",
                                        "fontSize": 16,
                                    }
                                )
                            )
                        ]
                    ),
                ]
            )
        )
