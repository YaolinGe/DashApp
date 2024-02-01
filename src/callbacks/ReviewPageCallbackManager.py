"""
This module handles the data analysis related callbacks
"""
import pandas as pd
import os

from dash import Dash, Output, Input, html, dcc
import plotly.graph_objs as go
from plotly.subplots import make_subplots

from controller.paths import datafolder_path

files = [file for file in os.listdir(datafolder_path) if file.endswith(".csv")]
data_sources = ['Deflection', 'Load', 'Vibration', 'Finish', 'Temperature']
file_exists = False

if len(files) > 0:
    file_exists = True


def preprocess_and_smooth(df):
    # Convert Time to total seconds
    df['Time'] = pd.to_timedelta(df['Time']).dt.total_seconds()

    # Round Time to nearest 0.01 second for synchronization
    df['Time'] = (df['Time'] * 100).round() / 100

    # Group by Time and average the Values for smoothing
    df = df.groupby('Time', as_index=False)['Value'].mean()

    return df


class ReviewPageCallbackManager:

    def register_callbacks(self, app: Dash = None):

        @app.callback(
            Output(component_id='sensor-graph', component_property='children'),
            Input(component_id='interval-update', component_property='n_intervals'),
        )
        def update_figure(n):
            if not file_exists:
                return html.Div(
                    [
                        html.H1("No data file found! "
                                "Have you uploaded data files? ")
                    ],
                    style={
                        "padding-top": "2vh",
                    }
                )
            else:
                return self.show_sensor_graph(n)

    @staticmethod
    def show_sensor_graph(n):
        fig = make_subplots(rows=5, cols=1, subplot_titles=data_sources, shared_xaxes=True, vertical_spacing=0.05)
        for i, data_source in enumerate(data_sources, start=1):
            filename = ReviewPageCallbackManager.get_file_name(data_source)
            if filename:
                df = pd.read_csv(os.path.join(datafolder_path, filename))
                df = preprocess_and_smooth(df)
                fig.add_trace(go.Scatter(x=df["Time"], y=df["Value"], name=data_source, showlegend=False), row=i, col=1)

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

    @staticmethod
    def get_file_name(sensor):
        for file in files:
            if sensor.lower() in file.lower():
                return file
        return None


# Usage
if __name__ == "__main__":
    app = Dash(__name__)
    callback_manager = ReviewPageCallbackManager()
    callback_manager.register_callbacks(app=app)
    # Additional setup and running the app
