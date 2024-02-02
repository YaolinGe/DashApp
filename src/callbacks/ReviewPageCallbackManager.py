"""
This module handles the data analysis related callbacks
"""
import pandas as pd
import os

from dash import Dash, Output, Input, html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from plotly.subplots import make_subplots

from controller.paths import datafolder_path
from controller.DataSources import DataSources
from model.DataHandler import preprocess_and_smooth


class ReviewPageCallbackManager:

    def __init__(self):
        self._file_exists = False
        self._files = [file for file in os.listdir(datafolder_path) if file.endswith(".csv")]

    def register_callbacks(self, app: Dash = None):

        @app.callback(
            Output(component_id='review-graph', component_property='children'),
            Input(component_id='review-interval-update', component_property='n_intervals'),
        )
        def update_figure(n):
            self._files = [file for file in os.listdir(datafolder_path) if file.endswith(".csv")]
            if self._files:
                self._file_exists = True

            if self._file_exists:
                return self.show_sensor_graph(n)
            else:
                return dbc.Alert(
                    "No data file found! Have you uploaded data files?",
                    color="danger",  # Choose a color that matches the alert context (e.g., "primary", "danger")
                    style={
                        "fontSize": "20px",  # Larger font size for the title
                        "margin-top": "20px",  # Add some space between the alert and the content
                        "width": "100%",
                        "textAlign": "center"
                    }
                )

    def show_sensor_graph(self, n):
        fig = make_subplots(rows=5, cols=1, subplot_titles=DataSources, shared_xaxes=True, vertical_spacing=0.05)
        for i, DataSource in enumerate(DataSources, start=1):
            filename = self.get_file_name(DataSource)
            if filename:
                df = pd.read_csv(os.path.join(datafolder_path, filename))
                df = preprocess_and_smooth(df)
                fig.add_trace(go.Scatter(x=df["Time"], y=df["Value"], name=DataSource, showlegend=False), row=i, col=1)

        fig.update_layout(
            height=800,
            title_text="Synchronized Sensor Data at 0.01s Intervals",
            hovermode='x unified',  # Unified hover mode across all plots
            xaxis=dict(
                showspikes=True,  # Show spike lines for the x-axis
                spikemode='across',  # Show spike lines across all subplots
                spikesnap='cursor',  # Snap to the closest data point
                showline=True,  # Show a line at the spike
                spikecolor="grey",  # Color of the spike line
                spikethickness=1  # Thickness of the spike line
            )
        )
        # Apply spike lines settings to all subplots if you have multiple x-axes
        for i in range(1, 6):  # Adjust the range according to the number of rows/subplots you have
            fig.update_xaxes(
                showspikes=True,
                spikemode='across',
                spikesnap='cursor',
                showline=True,
                spikecolor="grey",
                spikethickness=1,
                row=i,  # Apply to each row
                col=1  # Assuming a single column of subplots
            )
        fig.update_xaxes(title_text="Time (seconds)")

        return dcc.Graph(figure=fig),

    def get_file_name(self, data_source):
        for file in self._files:
            if data_source.lower() in file.lower():
                return file
        return None


# Usage
if __name__ == "__main__":
    app = Dash(__name__)
    callback_manager = ReviewPageCallbackManager()
    callback_manager.register_callbacks(app=app)
    # Additional setup and running the app
