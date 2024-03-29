from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/easter-egg-hunt")
def health_check():
    return "Healthy boi"


app.mount(
    "/easter-egg-hunt/so-it-begins",
    StaticFiles(directory="static/so_it_begins", html=True),
)

app.mount("/easter-egg-hunt/boom", StaticFiles(directory="static/boom", html=True))
app.mount(
    "/easter-egg-hunt/vinegar", StaticFiles(directory="static/vinegar", html=True)
)
app.mount("/easter-egg-hunt/birds", StaticFiles(directory="static/birds", html=True))
app.mount(
    "/easter-egg-hunt/victory", StaticFiles(directory="static/victory", html=True)
)
