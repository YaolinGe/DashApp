"""
This module handles the layout for the home page

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-30
"""
from __future__ import annotations
from dash import Dash, html
from dash_bootstrap_components import Container
import dash_bootstrap_components as dbc

from layouts.LayoutManager import LayoutManager
from layouts.NavBarLayout import update_nav_bar


class NF404Layout:

    def layout(self) -> Container:
        return LayoutManager.update_page_layout(nav_bar_content=update_nav_bar(activate_page="NF404"),
                                                view_port_content=dbc.Container(html.Div("404 Page Not Found")))


if __name__ == "__main__":
    app = Dash(__name__)
    app_layout = NF404Layout()
    app.layout = app_layout.layout()
    # Additional setup and running the app
