import uvicorn
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

df= pd.read_csv("/home/data/0700历史数据.csv")
line1 = go.Line(title='tencent stock',x=df['日期'],y=df['收盘'])
# Create the Dash application, make sure to adjust requests_pathname_prefx
app_dash = dash.Dash(__name__, requests_pathname_prefix='/dash/')
app_dash.layout = html.Div(children=[
    html.H1(children='Hello Wuyuhao'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [line1],
            'layout': {
                'title': 'Tencent Stock Price Visualization'
            }
        }
    )
])

# Now create your regular FASTAPI application

app = FastAPI()

@app.get("/hello_fastapi")
def read_main():
    return {"message": "Hello World"}

# Now mount you dash server into main fastapi application
app.mount("/dash", WSGIMiddleware(app_dash.server))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)