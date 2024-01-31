"""
This module creates the Dash App.
"""

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


def create_app(name=__name__):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]
    app = Dash(name, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])

    return app
