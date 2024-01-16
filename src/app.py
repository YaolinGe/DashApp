"""
Dash App for Data Analysis

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-12
"""
import base64
import datetime
import io

import pandas as pd

from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
from dash.exceptions import PreventUpdate
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Title("Dash App"),
    html.H1(children="Data Analysis App", style={'textAlign':'center'}),
    html.Hr(), 

    html.Div([
        # Left column for control
        html.Div([
            html.H3("Control Dashboard"),
            html.Div(dcc.Upload(
                id='datafiles',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]), multiple=False), className="row", style={'border': 'solid'}),
            
        ], className="four columns", style={'border': 'thin lightgrey solid'}),


        # Right column for visualization
        html.Div([
            html.H3("Visualization"),
            html.Div(id='output'),  # should change the id back to visualization since the callback needs to be updated to include several steps of rendering. 
        ], className="eight columns", style={'border': 'thin lightgrey solid'}),
    ], className="row"),  # This ensures that the columns are in one row
])


@callback(
    Output(component_id='output', component_property='children'), 
    Input(component_id='datafiles', component_property='contents'),
    State(component_id='datafiles', component_property='filename'),
)
def update_output(contents, filename):
    if contents is None: 
        raise PreventUpdate
    
    content_type, content_string = contents.split(',')
    return html.Div([html.H5(f"filename:L {filename}")])


if __name__ == "__main__": 
    app.run_server(debug=True, port=2000)