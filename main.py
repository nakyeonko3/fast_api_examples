from fastapi import FastAPI, Request
from typing import Union
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests as outrequests
from datetime import datetime

from request_url import getUrl_thread
from make_csv import read_csvfile_last_value

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# def getUrl():
#     return outrequests.get('https://api.waifu.pics/sfw/waifu')


@app.get("/")
def hello(request:Request):
     return templates.TemplateResponse("item.html",{"request":request, "id":23})

@app.get("/items")
def getItems(): 
    start_time = datetime.now()
    url_data = read_csvfile_last_value(file_name="urls.csv")
    end_time = datetime.now()
    print(f'time:{end_time - start_time}')
    return {'url':url_data}

getUrl_thread()
# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse("item.html", {"request": request, "id": id})
#query문이 뭔지 모르겠고

# decorator가 하는일이 뭔지도 모르겠고
# 비동기
# 어떻게 보내지는지 
# 통신이 어떻게 이루어지는 지 모르겠음
# 테스트 해보고 어디가 느린지 확인 해보자