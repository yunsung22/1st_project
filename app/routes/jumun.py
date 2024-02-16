from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

jumun_router = APIRouter()
# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
jumun_router.mount('/static', StaticFiles(directory='views/static'), name='static')

# 장바구니 x
@jumun_router.get('/bagx', response_class=HTMLResponse)
def bagx(req: Request):
    return templates.TemplateResponse('bagx.html', {'request': req})

# 장바구니 o
@jumun_router.get('/bag', response_class=HTMLResponse)
def bag(req: Request):
    return templates.TemplateResponse('bag.html', {'request': req})


@jumun_router.get('/jumun', response_class=HTMLResponse)
def jumun(req: Request):
    return templates.TemplateResponse('jumun.html', {'request': req})

@jumun_router.get('/payment', response_class=HTMLResponse)
def payment(req: Request):
    return templates.TemplateResponse('payment.html', {'request': req})



