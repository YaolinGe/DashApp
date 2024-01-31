from dash import Dash, Output, Input
from pages import HomePage, DataAnalysisPage, NF404Page


class NavBarCallbackManager:

    def register_callbacks(self, app: Dash = None):
        @app.callback(Output('page-content', 'children'),
                  Input('url', 'pathname'))
        def register_page(pathname):
            if pathname == '/':
                return HomePage.layout
            elif pathname == '/eda':
                return DataAnalysisPage.layout
            else:
                return NF404Page.layout


if __name__ == "__main__":
    app = Dash(__name__)
    nav_bar_callback_manager = NavBarCallbackManager()
    nav_bar_callback_manager.register_callbacks(app)