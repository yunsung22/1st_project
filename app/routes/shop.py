from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.services.product import ProductService

shop_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
shop_router.mount('/static', StaticFiles(directory='views/static'), name='static')

# oxfords 들어가는 경로
@shop_router.get('/oxfords', response_class=HTMLResponse)
def oxfords(req: Request):
    pdlist = ProductService.select2_product()
    return templates.TemplateResponse('main_header/shop/oxfords.html', {'request': req, 'pdlist': pdlist})

# knitwear 들어가는 경로
@shop_router.get('/knitwear', response_class=HTMLResponse)
def knitwear(req: Request):
    pdlist = ProductService.select2_product()
    return templates.TemplateResponse('main_header/shop/knitwear.html', {'request': req, 'pdlist': pdlist})

# checkered 들어가는 경로
@shop_router.get('/checkered', response_class=HTMLResponse)
def checkered(req: Request):
    pdlist = ProductService.select2_product()
    return templates.TemplateResponse('main_header/shop/checkered.html', {'request': req, 'pdlist': pdlist})

# carryover 들어가는 경로
@shop_router.get('/carryover', response_class=HTMLResponse)
def carryover(req: Request):
    pdlist = ProductService.select2_product()
    return templates.TemplateResponse('main_header/shop/carryover.html', {'request': req, 'pdlist': pdlist})



@shop_router.get('/itemview/{prdno}', response_class=HTMLResponse)
def view(req: Request, prdno: str):
    pd = ProductService.selectone_product(prdno)
    return templates.TemplateResponse('main_header/shop/item_detail.html', {'request': req, 'p': pd[0], 'pd': pd[1]})

