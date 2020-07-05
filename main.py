from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
temp = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return temp.TemplateResponse("home.html", {
        "request": request
    })