# Python Dash Application for .cut File Visualization

## Sensor Data Available
```
Box1Accelerometer2GRaw0
Box1Accelerometer2GRaw1
Box1Accelerometer2GRaw2
Box1Accelerometer50GRaw0
Box1Accelerometer50GRaw1
Box2StrainRaw0
Box2StrainRaw1
Box3Clock
Box1ClockPeripheral
Box2ClockPeripheral
Deflection
Load
SurfaceFinish
Vibration
Temperature
```

## How to set up Docker to deploy the app in the container
- host needs to use `0.0.0.0` for the cloud setup, but it needs to be updated when launching in the local machine.

## Overview
This application, built using Dash in Python, visualizes data from `.cut` files processed by the `CutFileParserCLI` tool. It offers interactive data visualization capabilities, enabling users to explore and analyze the extracted data efficiently.

## Features
- **Interactive Visualizations**: Utilize Plotly for dynamic data plots.
- **.cut File Processing**: Seamlessly upload and handle `.cut` files.
- **Data Customization**: Offers features to customize data presentation.

## Getting Started

### Prerequisites
- Python 3.x
- Dash
- Pandas
- Plotly

### Installation
Install the necessary packages using pip:

```bash
pip install dash pandas plotly
```

## Running the App
To start the Dash app, run:
```python
python app.py
```

## Usage
Uploading .cut Files
Detail the steps for uploading and processing .cut files.
Interacting with the Dashboard
Instructions on using various interactive elements of the dashboard.

## Development
Structure
`app.py`: Main Dash application entry point.
`controller/`: Business logic and data processing.
`model/`: Data management and manipulation.
`view/`: UI components and layout.

## Contributing
Guidelines for contributing to the project.

## License
Relevant licensing information.

## Contact
Contact info for the project maintainer or team.

## Acknowledgements
Credits to third-party libraries or contributors.
