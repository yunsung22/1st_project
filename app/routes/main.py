from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.services.cart import CartService
from app.services.jumun import JumunService
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

# oxfords 들어가는 경로
@main_router.get('/oxfords', response_class=HTMLResponse)
def oxfords(req: Request):
    pdlist = ProductService.select_product()
    return templates.TemplateResponse('oxfords.html', {'request': req, 'pdlist': pdlist})

# knitwear 들어가는 경로
@main_router.get('/knitwear', response_class=HTMLResponse)
def knitwear(req: Request):
    pdlist = ProductService.select_product()
    return templates.TemplateResponse('knitwear.html', {'request': req, 'pdlist': pdlist})

# checkered 들어가는 경로
@main_router.get('/checkered', response_class=HTMLResponse)
def checkered(req: Request):
    pdlist = ProductService.select_product()
    return templates.TemplateResponse('checkered.html', {'request': req, 'pdlist': pdlist})

# carryover 들어가는 경로
@main_router.get('/carryover', response_class=HTMLResponse)
def carryover(req: Request):
    pdlist = ProductService.select_product()
    return templates.TemplateResponse('carryover.html', {'request': req, 'pdlist': pdlist})



@main_router.get('/itemview/{prdno}', response_class=HTMLResponse)
def view(req: Request, prdno: str):
    pd = ProductService.selectone_product(prdno)
    return templates.TemplateResponse('item_detail.html', {'request': req, 'p': pd[0], 'pd': pd[1]})

@main_router.get('/bagok/{prdno}/{userid}', response_class=HTMLResponse)
def bagok(req: Request, prdno: str, userid: str):

    pd = CartService.insert_cart(prdno, userid)
    pd = None
    return "templates.TemplateResponse('bag.html', {'request': req})"
    # return "templates.TemplateResponse('item_detail.html', {'request': req})"

@main_router.get('/jumunok/{prdno}/{userid}', response_class=HTMLResponse)
def jumunok(req: Request, prdno: str, userid: str):
    pd = JumunService.insert_jumun(prdno, userid)
    pd = None
    return "templates.TemplateResponse('bag.html', {'request': req})"
    # return "templates.TemplateResponse('item_detail.html', {'request': req})"

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




