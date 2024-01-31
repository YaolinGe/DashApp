"""
This module handles the layout for the home page

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-30
"""
from __future__ import annotations
from dash import Dash
from dash_bootstrap_components import Container

from layouts.LayoutManager import LayoutManager
from layouts.FileUploaderLayout import FileUploaderLayout
from layouts.NavBarLayout import update_nav_bar


class HomePageLayout:

    def __init__(self) -> None:
        self._file_uploader_layout = FileUploaderLayout.create()

    def layout(self) -> Container:
        return LayoutManager.update_page_layout(nav_bar_content=update_nav_bar(activate_page="Home"),
                                                view_port_content=self._file_uploader_layout)


if __name__ == "__main__":
    app = Dash(__name__)
    app_layout = HomePageLayout()
    app.layout = app_layout.layout()
    # Additional setup and running the app
