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

from layouts.LayoutManager import LayoutManager
from layouts.BaseLayout import BaseLayout
from layouts.NavBarLayout import update_nav_bar


class DataAnalysisPageLayout:

    def layout(self) -> Container:
        return LayoutManager.update_page_layout(update_nav_bar(activate_page="EDA"), dbc.Container())


if __name__ == "__main__":
    app = Dash(__name__)
    app_layout = DataAnalysisPageLayout()
    app.layout = app_layout.layout()
    # Additional setup and running the app
