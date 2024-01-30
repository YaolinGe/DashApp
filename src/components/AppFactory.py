"""
This module creates the Dash App.
"""

from dash import Dash
import dash_bootstrap_components as dbc


import os


def create_app(name=__name__):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]
    app = Dash(name, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
    return app
