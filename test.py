import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Example dataframe
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Value": [100, 200, 300, 400]
})

fig = px.bar(df, x="Category", y="Value", title="Example Bar Chart")

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Simple Dashboard'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


