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
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                "Upload Data Files",
                                style={
                                    "fontSize": "24px",  # Larger font size for the title
                                    "textAlign": "center",
                                    "backgroundColor": "lightBlue",  # change to another color
                                    "color": "black",
                                    "padding": "10px",
                                    "borderRadius": "5px"  # Optional: adds rounded corners to the title bar
                                }
                            ),
                            html.Div(
                                dcc.Upload(
                                    id='datafiles',
                                    children=html.Div(
                                        [
                                            "Drag and Drop or ",
                                            html.A('Select Files')
                                        ],
                                        style={
                                            "fontSize": "20px",  # Large font size for the text
                                            "textAlign": "center",  # Center the text
                                            "lineHeight": "100px"  # Increase line height to enlarge the area
                                        }
                                    ),
                                    style={
                                        "height": "40vh",  # Increase the height to make the area larger
                                        "width": "55vw",  # Increase the width to make the area larger
                                        "lineHeight": "200px",
                                        "borderWidth": "2px",
                                        "borderStyle": "dashed",
                                        "borderRadius": "5px",
                                        "textAlign": "center",
                                        "margin": "auto",  # Center the upload component horizontally
                                        "display": "flex",
                                        "justifyContent": "center",
                                        "alignItems": "center"  # Center the text vertically
                                    }
                                ),
                                style={
                                    "textAlign": "center",
                                    "margin": "auto",  # Center the div horizontally
                                    "width": "fit-content"  # Adjust the width based on the content
                                }
                            )
                        ],
                        style={
                            "textAlign": "center",
                            "alignItems": "center",
                            "display": "flex",
                            "flexDirection": "column",
                            "justifyContent": "center",
                            "height": "45vh"  # Use the full height of the viewport to center vertically
                        }
                    )
                ]
            )
        )
