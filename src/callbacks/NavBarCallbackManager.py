from dash import Dash, Output, Input
from pages import HomePage, ReviewPage, NF404Page, FFTPage


class NavBarCallbackManager:

    def register_callbacks(self, app: Dash = None):
        @app.callback(Output('page-content', 'children'),
                  Input('url', 'pathname'))
        def register_page(pathname):
            if pathname == '/':
                return HomePage.layout
            elif pathname == '/review':
                return ReviewPage.layout
            elif pathname == '/fft':
                return FFTPage.layout
            else:
                return NF404Page.layout


if __name__ == "__main__":
    app = Dash(__name__)
    nav_bar_callback_manager = NavBarCallbackManager()
    nav_bar_callback_manager.register_callbacks(app)
