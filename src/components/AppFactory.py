"""
This module creates the Dash App.
"""

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from callbacks.CutFileParserCallbackManager import CutFileParserCallbackManager
from callbacks.NavBarCallbackManager import NavBarCallbackManager
from callbacks.ReviewPageCallbackManager import ReviewPageCallbackManager
from callbacks.FFTPageCallbackManager import FFTPageCallbackManager
from controller.CleanUp import clean_up


def create_app(name=__name__):

    clean_up()

    external_stylesheets = [
        'https://codepen.io/chriddyp/pen/bWLwgP.css',
        dbc.themes.BOOTSTRAP,
        "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css"
    ]
    app = Dash(name, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])

    # Register all essential callbacks
    nav_bar_callback_manager = NavBarCallbackManager()
    nav_bar_callback_manager.register_callbacks(app=app)

    callback_manager = CutFileParserCallbackManager()
    callback_manager.register_callbacks(app=app)

    review_page_callback_manager = ReviewPageCallbackManager()
    review_page_callback_manager.register_callbacks(app=app)

    fft_page_callback_manager = FFTPageCallbackManager()
    fft_page_callback_manager.register_callbacks(app=app)

    return app
