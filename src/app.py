"""
Dash App for Data Analysis

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-12
"""
from controller.CleanUp import clean_up
from components.AppFactory import create_app
from layouts.HomePageLayout import HomePageLayout
from callbacks.CallbackManager import CallbackManager

clean_up()


from dash import Dash, dcc, html, Input, Output, callback
from pages import page1, page2, HomePage, NOF_404


app = create_app(name="OD Turning Data Analysis App")


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
# TODO: move on from here to make the multipage app work more smoothly

callback_manager = CallbackManager()
callback_manager.register_callbacks(app=app)


if __name__ == "__main__":
    app.run_server(debug=True, port=2000)
