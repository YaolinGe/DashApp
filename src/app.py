"""
Dash App for Data Analysis

Author: Yaolin Ge
Email: geyaolin@gmail.com
Date: 2024-01-12
"""
from components.AppFactory import create_app

app = create_app(name="OD Turning Data Analysis App")


if __name__ == "__main__":
    # app.run_server(debug=True, port=2000)
    app.run(debug=True)
