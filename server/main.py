import os
import pandas as pd
import uvicorn
from fastapi import FastAPI
pd.options.plotting.backend = "plotly"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
dataset = os.path.join(DATA_DIR, '0700历史数据.csv')
app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "Yuhao"}

@app.get('/xyz')
def read_data():
    df = pd.read_csv(dataset)
    return df.head(n=2)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)