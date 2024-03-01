"""
This module handles the data analysis related callbacks
"""
import pandas as pd
import os
import numpy as np
from scipy.fft import fft

from dash import Dash, Output, Input, html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from plotly.subplots import make_subplots

from controller.paths import datafolder_path
from controller.DataSources import DataSources
from model.DataHandler import resample_timestamp

import matplotlib.pyplot as plt


class FFTPageCallbackManager:

    def __init__(self):
        self._file_exists = False
        self._files = [file for file in os.listdir(datafolder_path) if file.endswith(".csv")]

    def register_callbacks(self, app: Dash = None):

        @app.callback(
            Output(component_id='fft-graph', component_property='children'),
            [Input(component_id='fft-data-source', component_property='value'),
             Input(component_id='fft-time-slider', component_property='value'),
             Input(component_id='fft-window-size', component_property='value')]
        )
        def update_figure(data_source, time_slider, window_size):
            self._files = [file for file in os.listdir(datafolder_path) if file.endswith(".csv")]
            if self._files:
                self._file_exists = True

            if self._file_exists:
                return self.show_sensor_graph(data_source, time_slider, window_size)
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

    def show_sensor_graph(self, data_source, time_slider, window_size):
        fig = make_subplots(
            rows=2, cols=2,
            specs=[[{"colspan": 2, "type": "scatter"}, None],
                   [{"type": "scatter"}, {"type": "scatter"}]],
            shared_xaxes=True,
            vertical_spacing=0.1,
            subplot_titles=(f"{data_source} Time Series", "Selected Time Window", "FFT Analysis")
        )
        if not data_source:
            return dcc.Graph()  ## -> Need a better solution here.
        else:
            filename = self.get_file_name(data_source)
        if filename:
            # Process the data to match the desired time format and value format
            df = pd.read_csv(os.path.join(datafolder_path, filename))
            df = resample_timestamp(df).to_numpy()
            xplot = df[:, 0]
            yplot = df[:, 1]
            number_of_samples = len(xplot)
            sampling_interval = np.mean(np.diff(xplot))
            sampling_rate = 1 // sampling_interval

            ind_current_timestamp = int(number_of_samples * time_slider / 100)
            window_half_length = int(window_size / 2)
            ind_window_start = max(0, ind_current_timestamp - window_half_length)
            ind_window_end = min(df.shape[0]-1, ind_current_timestamp + window_half_length)

            # Plotting the main sensor data on the first row
            fig.add_trace(go.Scatter(x=xplot, y=yplot, name=data_source, showlegend=False), row=1, col=1)
            fig.add_vline(x=xplot[ind_current_timestamp], line_width=1, line_dash="dash", line_color="red",
                          row=1, col=1)
            fig.add_vrect(x0=xplot[ind_window_start], x1=xplot[ind_window_end],
                          fillcolor="lightyellow", opacity=0.5, line_width=0, row=1, col=1)

            xplot_selected_time_window = xplot[ind_window_start:ind_window_end]
            yplot_selected_time_window = yplot[ind_window_start:ind_window_end]
            fig.add_trace(go.Scatter(x=xplot_selected_time_window, y=yplot_selected_time_window,
                                     name="Selected Time Window", showlegend=False),row=2, col=1)

            # Plot FFT analysis
            signal = yplot_selected_time_window - np.mean(yplot_selected_time_window)
            number_of_samples_in_window = len(signal)
            half_number_of_samples = number_of_samples_in_window // 2
            f_signal = fft(signal)
            xf_signal = np.linspace(0, sampling_rate, number_of_samples_in_window)
            df_fft = pd.DataFrame({"Frequency": xf_signal[:half_number_of_samples],
                                   "Amplitude": np.abs(f_signal)[:half_number_of_samples]/number_of_samples_in_window})
            fig.add_trace(go.Scatter(x=df_fft["Frequency"], y=df_fft["Amplitude"],
                                     name="FFT Analysis", showlegend=False), row=2, col=2)

        # Update layout
        fig.update_layout(
            height=600,
            title_text=f"Analysis of {data_source} Data",
            hovermode='x unified',
            updatemenus=[dict(type="buttons",
                              buttons=[dict(label="Play",
                                            method="animate",
                                            args=[None])])],
        )

        # Updating axis labels and configurations
        fig.update_xaxes(title_text="Time (s)", row=1, col=1)
        fig.update_xaxes(title_text="Time (s)", row=2, col=1)
        fig.update_xaxes(title_text="Frequency (Hz)", row=2, col=2)
        fig.update_yaxes(title_text="Amplitude", row=2, col=2)
        fig.update_yaxes(title_text="Value", row=1, col=1)
        fig.update_yaxes(title_text="Value", row=2, col=1)

        return dcc.Graph(figure=fig),

    def get_file_name(self, data_source):

        for file in self._files:
            if data_source.lower() in file.lower():
                return file
        return None


# Usage
if __name__ == "__main__":
    app = Dash(__name__)
    callback_manager = FFTPageCallbackManager()
    callback_manager.register_callbacks(app=app)
    # Additional setup and running the app
