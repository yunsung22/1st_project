from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

mf_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
mf_router.mount('/static', StaticFiles(directory='views/static'), name='static')

# 푸터 #

@mf_router.get('/accessibility', response_class=HTMLResponse)
def accessibility(req: Request):
    return templates.TemplateResponse('main_footer/Accessibility.html', {'request': req})

@mf_router.get('/giftcards', response_class=HTMLResponse)
def giftcards(req: Request):
    return templates.TemplateResponse('main_footer/Giftcards.html', {'request': req})

@mf_router.get('/faq', response_class=HTMLResponse)
def fqa(req: Request):
    return templates.TemplateResponse('main_footer/FAQ.html', {'request': req})


@mf_router.get('/legal', response_class=HTMLResponse)
def legal(req: Request):
    return templates.TemplateResponse('main_footer/legal.html', {'request': req})


@mf_router.get('/policy', response_class=HTMLResponse)
def policy(req: Request):
    return templates.TemplateResponse('main_footer/policy.html', {'request': req})




