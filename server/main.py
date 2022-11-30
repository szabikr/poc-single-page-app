from fastapi import FastAPI as FastApi
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from data import get_data

app = FastApi()
app.mount("/web", StaticFiles(directory="web"), name="web")

@app.get("/api/data")
def read_data():
    data = get_data()
    return {"Hello": data}

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <h1>Hyia from Python, try {root_url}/web/index.html</h1>
    """
