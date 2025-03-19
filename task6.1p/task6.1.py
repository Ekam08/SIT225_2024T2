import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load Gyroscope Data
data = pd.read_csv("gyro_data.csv")

# Initialize Dash App
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div([
    html.H1("Gyroscope Data Overview"),

    html.Label("Choose Graph Style:"),
    dcc.Dropdown(
        id='chart-choice',
        options=[
            {'label': 'Scatter Plot', 'value': 'scatter'},
            {'label': 'Line Graph', 'value': 'line'},
            {'label': 'Histogram', 'value': 'histogram'},
            {'label': 'Distribution Plot', 'value': 'distribution'}
        ],
        value='scatter'
    ),

    html.Label("Pick Data Variables:"),
    dcc.Dropdown(
        id='variable-choice',
        options=[
            {'label': 'X', 'value': 'x'},
            {'label': 'Y', 'value': 'y'},
            {'label': 'Z', 'value': 'z'},
            {'label': 'All (X, Y, Z)', 'value': 'all'}
        ],
        multi=True,
        value=['x', 'y', 'z']
    ),

    html.Label("Enter Sample Size:"),
    dcc.Input(id='sample-count', type='number', value=100, min=1, step=1),

    html.Button('Previous Batch', id='prev-btn', n_clicks=0),
    html.Button('Next Batch', id='next-btn', n_clicks=0),

    dcc.Graph(id='chart-output'),
    dash_table.DataTable(id='data-summary')
])

# Callback for Graph & Data Table Updates
@app.callback(
    [Output('chart-output', 'figure'), Output('data-summary', 'data')],
    [Input('chart-choice', 'value'),
     Input('variable-choice', 'value'),
     Input('sample-count', 'value'),
     Input('prev-btn', 'n_clicks'),
     Input('next-btn', 'n_clicks')]
)
def update_chart(chart_type, variables, sample_size, prev_clicks, next_clicks):
    # Compute start index for pagination
    start_index = max(0, (next_clicks - prev_clicks) * sample_size)
    subset = data.iloc[start_index: start_index + sample_size]

    if 'all' in variables:
        variables = ['x', 'y', 'z']

    # Generate Graph based on user selection
    if chart_type == 'line':
        fig = px.line(subset, x=subset.index, y=variables, title="Line Graph")
    elif chart_type == 'scatter':
        fig = px.scatter(subset, x=subset.index, y=variables, title="Scatter Plot")
    elif chart_type == 'histogram':
        fig = px.histogram(subset, x=variables, title="Histogram")
    elif chart_type == 'distribution':
        fig = px.histogram(subset, x=variables, marginal="box", title="Distribution Plot")

    # Generate summary statistics
    summary = subset[variables].describe().reset_index().to_dict('records')

    return fig, summary

# Run the App
if __name__ == '__main__':
    app.run_server(debug=True)
