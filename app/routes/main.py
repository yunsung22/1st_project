from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.services.product import ProductService

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

# wintersale 들어가는 경로
@main_router.get('/oxfords', response_class=HTMLResponse)
def oxfords(req: Request):
    pdlist = ProductService.select_product()
    return templates.TemplateResponse('oxfords.html', {'request': req, 'pdlist': pdlist})


@main_router.get('/itemview/{prdno}', response_class=HTMLResponse)
def view(req: Request, prdno: str):
    pd = ProductService.selectone_product(prdno)
    return templates.TemplateResponse('item_detail.html', {'request': req, 'p': pd[0], 'pd': pd[1]})


# 푸터 #

@main_router.get('/accessibility', response_class=HTMLResponse)
def accessibility(req: Request):
    return templates.TemplateResponse('Accessibility.html', {'request': req})

@main_router.get('/giftcards', response_class=HTMLResponse)
def giftcards(req: Request):
    return templates.TemplateResponse('Giftcards.html', {'request': req})

@main_router.get('/faq', response_class=HTMLResponse)
def fqa(req: Request):
    return templates.TemplateResponse('FAQ.html', {'request': req})


@main_router.get('/legal', response_class=HTMLResponse)
def legal(req: Request):
    return templates.TemplateResponse('legal.html', {'request': req})


@main_router.get('/policy', response_class=HTMLResponse)
def policy(req: Request):
    return templates.TemplateResponse('policy.html', {'request': req})




