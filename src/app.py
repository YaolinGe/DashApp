"""
Dash App for Data Analysis

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-12
"""
from controller.CleanUp import clean_up
from components.AppFactory import create_app
from callbacks.CallbackManager import CallbackManager
from callbacks.NavBarCallbackManager import NavBarCallbackManager

clean_up()

app = create_app(name="OD Turning Data Analysis App")


# Register all essential callbacks
nav_bar_callback_manager = NavBarCallbackManager()
nav_bar_callback_manager.register_callbacks(app=app)

callback_manager = CallbackManager()
callback_manager.register_callbacks(app=app)


if __name__ == "__main__":
    app.run_server(debug=True, port=2000)
