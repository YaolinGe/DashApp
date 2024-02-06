"""
This module handles all the callbacks of the Dash App.
"""
import os
import base64
import subprocess
import tempfile
import platform

from dash import Dash, Output, Input, State
from dash.exceptions import PreventUpdate
from dash.long_callback import DiskcacheLongCallbackManager
import diskcache
from dash import html


cache = diskcache.Cache("./cache")
long_callback_manager = DiskcacheLongCallbackManager(cache)

platform_name = platform.system()


class CutFileParserCallbackManager:

    def register_callbacks(self, app: Dash = None):

        @app.callback(
            [Output(component_id='output', component_property='children'),
             Output(component_id='upload-div', component_property='style')],
            Input(component_id='datafiles', component_property='contents'),
            State(component_id='datafiles', component_property='filename'),
            running=[
                (Output(component_id='loading-output', component_property='children'), True, False),
            ],
            manager=long_callback_manager
        )
        def update_output(contents, filename):
            return self.process_file(contents, filename)

    @staticmethod
    def process_file(contents, filename):
        if contents is None:
            raise PreventUpdate

        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)

        with tempfile.NamedTemporaryFile(delete=False, suffix=filename) as tmp_file:
            tmp_file.write(decoded)
            tmp_filename = tmp_file.name

        if platform_name == "Windows":
            exe_path = os.path.join(os.getcwd(), "tools", "CutFileParserCLI.exe")
        elif platform_name == "Linux":
            exe_path = os.path.join(os.getcwd(), "tools", "linuxParser", "CutFileParserCLI")
        else:
            raise Exception("Unsupported platform")

        try:
            result = subprocess.run([exe_path, tmp_filename], capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            print("Error occurred:", e)
            return html.Div([html.H5("Error in processing file")])
        finally:
            os.remove(tmp_filename)

        try:
            # Your file processing logic here...
            new_style = {"padding": "10px", "border": "thin lightgrey solid", "height": "35vh",
                         "text-align": "center", "margin": "auto", "display": "flex",
                         "justifyContent": "center", "alignItems": "center",
                         "backgroundColor": "green", "overflow": "auto"}  # Change backgroundColor to green
            return html.Div([html.H5(f"Filename: {filename}"), html.Pre("File processed successfully!"),
                             html.Pre(result.stdout if result.stdout else "No output")]), new_style
        except Exception as e:
            # If an error occurs, keep the original style but change the content
            original_style = {"padding": "10px", "border": "thin lightgrey solid", "height": "35vh",
                              "text-align": "center", "margin": "auto", "display": "flex",
                              "justifyContent": "center", "alignItems": "center",
                              "backgroundColor": "lightYellow", "overflow": "auto"}
            return html.Div([html.H5("Error in processing file")]), original_style


# Usage
if __name__ == "__main__":
    app = Dash(__name__)
    callback_manager = CutFileParserCallbackManager()
    callback_manager.register_callbacks(app=app)
    # Additional setup and running the app
