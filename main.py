from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import urllib.parse
from pydantic import BaseModel

app = FastAPI()
temp = Jinja2Templates(directory="templates")


class UrlRequest(BaseModel):
    url: str

def convertUrl(url):
    base_url = 'https://img.youtube.com/vi/'

    # maxresdefault for the max resolution
    v_id = urllib.parse.urlparse(url).query[2:] + '/maxresdefault.jpg'
    imgUrl = urllib.parse.urljoin(base_url, v_id)

    return imgUrl


@app.get("/")
def home(request: Request):

    return temp.TemplateResponse("home.html", {
        "request": request
    })

@app.post("/images")
def get_images(url_request: UrlRequest):
    """
    Generate thumbnail images and display them
    """
    imgUrl = convertUrl(url_request.url)

    return {
        "status": "success", 
        "imgUrl": imgUrl
    }
