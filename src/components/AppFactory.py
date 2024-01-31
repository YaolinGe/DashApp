"""
This module creates the Dash App.
"""

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


def create_app(name=__name__):
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

    return app
