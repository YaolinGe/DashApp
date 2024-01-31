"""
This module handles the layout for the data analysis page

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-31
"""
from __future__ import annotations
import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Container

from layouts.BaseLayout import BaseLayout
from layouts.NavBarLayout import update_nav_bar


class DataAnalysisPageLayout:

    def __init__(self) -> None:
        self._base_layout = BaseLayout()

    def layout(self) -> Container:
        self._base_layout.create_nav_bar(update_nav_bar(activate_page="EDA"))
        self._base_layout.create_view_port(html.Div())
        layout = self._base_layout.update_layout()
        return layout


if __name__ == "__main__":
    app = Dash(__name__)
    app_layout = DataAnalysisPageLayout()
    app.layout = app_layout.layout()
    # Additional setup and running the app
