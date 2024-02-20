from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

mh_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
mh_router.mount('/static', StaticFiles(directory='views/static'), name='static')

# 헤더 #

# 룩북 들어가는 경로
@mh_router.get('/lookbook', response_class=HTMLResponse)
def lookbook(req: Request):
    return templates.TemplateResponse('main_header/Lookbook.html', {'request': req})


# 인덱스 들어가는 경로
@mh_router.get('/index', response_class=HTMLResponse)
def index(req: Request):
    return templates.TemplateResponse('main_header/index.html', {'request': req})


# about 들어가는 경로
@mh_router.get('/about', response_class=HTMLResponse)
def about(req: Request):
    return templates.TemplateResponse('main_header/About.html', {'request': req})


