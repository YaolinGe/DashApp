"""
This module handles the layout for FFT Page

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-02-01
"""
from __future__ import annotations
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Container

from layouts.LayoutManager import LayoutManager
from layouts.NavBarLayout import update_nav_bar
from controller.DataSources import DataSources


class FFTPageLayout:

    def update_view_port(self) -> Container:
        return (
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            dcc.RadioItems(
                                                id='fft-data-source',
                                                options=[
                                                    {'label': source, 'value': source} for source in DataSources
                                                ],
                                                # value='Deflection',
                                                style={  # Add this style dict
                                                    'display': 'flex',  # This makes the container a flex container
                                                    'flexDirection': 'row',
                                                    # This lays out the children in a horizontal row
                                                    'gap': '10px',  # Adds space between each radio item
                                                },
                                                labelStyle={  # Adjustments to labelStyle for better control
                                                    'marginRight': '15px',
                                                    # Adds space to the right of each label, if needed
                                                }
                                            ),
                                            style={
                                                "padding": "20px",
                                                "display": "flex",
                                                "justify-content": "left",
                                                "align-items": "center",
                                            }
                                        ),
                                        html.Div(
                                            children=[
                                                html.Div(
                                                    "Time Slider",
                                                    style={
                                                        "padding": "5px",
                                                        "display": "flex",
                                                        "justify-content": "center",
                                                        "font-size": "20px",
                                                    }
                                                ),
                                                dcc.Slider(
                                                    id='fft-time-slider',
                                                    min=0,
                                                    max=99,
                                                    step=1,
                                                    value=0,
                                                    marks={0: '0%', 99: '100%'}
                                                ),
                                                html.Div(
                                                    "Window Size",
                                                    style={
                                                        "padding": "5px",
                                                        "display": "flex",
                                                        "justify-content": "center",
                                                        "font-size": "20px",
                                                    }
                                                ),
                                                dbc.Input(
                                                    id="fft-window-size",
                                                    type="number",
                                                    value=1600,
                                                    style={

                                                        "padding": "5px",
                                                        "display": "flex",
                                                        "justify-content": "center",
                                                        "font-size": "20px",
                                                    }
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            id="fft-graph"
                                        ),
                                        dcc.Interval(
                                            id='fft-interval-update',
                                            interval=60000,  # in milliseconds (e.g., 60000ms = 60s)
                                            n_intervals=0
                                        )
                                    ]
                                )
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
        return LayoutManager.update_page_layout(update_nav_bar(activate_page="FFT"), self.update_view_port())


if __name__ == "__main__":
    app = Dash(__name__)
    app_layout = FFTPageLayout()
    app.layout = app_layout.layout()
    # Additional setup and running the app
