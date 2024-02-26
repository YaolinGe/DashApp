# Notes for DashApp
- `dcc.Graph` has properties such as `hoverData`, `clickData`, `selectedData`, `replayoutData` to add interactions to the visualization.
- Dash is stateless which is more robust and scalable.

## How to link conda environment to jupyter kernel
- `conda activate env`
- `conda install ipykernel`
- `python -m ipykernel install --user --name=OD --display-name "OD"` to create a ipykernel with the name desired.
