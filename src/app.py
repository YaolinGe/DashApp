# """
# Dash App for Data Analysis

# Author: Yaolin Ge
# Email: geyaolin@gmail.com
# Date: 2024-01-12
# """
# from components.AppFactory import create_app

# app = create_app(name="OD Turning Data Analysis App")

# server = app.server


# if __name__ == "__main__":
#     # app.run_server(debug=True, port=2000)
#     app.run(debug=True)
#     # app.run_server(debug=True, host='0.0.0.0')


"""
Dash App for Data Analysis

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-12
"""
import os
from components.AppFactory import create_app

app = create_app(name="OD Turning Data Analysis App")

server = app.server

if __name__ == "__main__":
    # Check if the HOST environment variable is set
    host = os.environ.get('HOST', '127.0.0.1')  # Default to '127.0.0.1' if HOST is not set

    # You can also specify the port here if needed
    port = 8050  # Replace with your desired port number

    app.run(debug=True, host=host, port=port)
