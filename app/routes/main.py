from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

main_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
main_router.mount('/static', StaticFiles(directory='views/static'), name='static')

# 헤더 #

# 인덱스 들어가는 경로
@main_router.get('/lookbook', response_class=HTMLResponse)
def index(req: Request):
    return templates.TemplateResponse('Lookbook.html', {'request': req})


# 룩북 들어가는 경로
@main_router.get('/index', response_class=HTMLResponse)
def lookbook(req: Request):
    return templates.TemplateResponse('index.html', {'request': req})


# about 들어가는 경로
@main_router.get('/about', response_class=HTMLResponse)
def about(req: Request):
    return templates.TemplateResponse('About.html', {'request': req})


# 푸터 #

@main_router.get('/accessibility', response_class=HTMLResponse)
def accessibility(req: Request):
    return templates.TemplateResponse('Accessibility.html', {'request': req})

@main_router.get('/giftcards', response_class=HTMLResponse)
def giftcards(req: Request):
    return templates.TemplateResponse('Giftcards.html', {'request': req})
# 장바구니 #
@main_router.get('/bag', response_class=HTMLResponse)
def giftcards(req: Request):
    return templates.TemplateResponse('bag.html', {'request': req})

@main_router.get('/jumun', response_class=HTMLResponse)
def giftcards(req: Request):
    return templates.TemplateResponse('jumun.html', {'request': req})