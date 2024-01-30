"""
This module handles all the callbacks of the Dash App.
"""
import os
import base64
import subprocess
import tempfile

from dash import Dash, callback, Output, Input, State
from dash.exceptions import PreventUpdate
from dash.long_callback import DiskcacheLongCallbackManager
import diskcache
from dash import html

from pages import page1, page2, HomePage, NOF_404

cache = diskcache.Cache("./cache")
long_callback_manager = DiskcacheLongCallbackManager(cache)


class CallbackManager:

    def register_callbacks(self, app: Dash = None):
        @app.callback(Output('page-content', 'children'),
                  Input('url', 'pathname'))
        def display_page(pathname):
            if pathname == '/page1':
                return page1.layout
            elif pathname == '/page2':
                return page2.layout
            elif pathname == "/":
                return HomePage.layout
            else:
                return NOF_404.layout

        @app.callback(
            # Output(component_id='file-uploaded-marker', component_property='style'),
            Output(component_id='output', component_property='children'),
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

        exe_path = os.path.join(os.getcwd(), "tools", "CutFileParserCLI.exe")
        try:
            result = subprocess.run([exe_path, tmp_filename], capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            print("Error occurred:", e)
            return html.Div([html.H5("Error in processing file")])
        finally:
            os.remove(tmp_filename)

        return html.Div([html.H5(f"Filename: {filename}"), html.Pre(result.stdout if result.stdout else "No output")])


# Usage
if __name__ == "__main__":
    app = Dash(__name__)
    callback_manager = CallbackManager()
    callback_manager.register_callbacks(app=app)
    # Additional setup and running the app
