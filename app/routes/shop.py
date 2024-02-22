from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette import status
from starlette.responses import RedirectResponse

from app.services.cart import CartService
from app.services.product import ProductService

shop_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
shop_router.mount('/static', StaticFiles(directory='views/static'), name='static')


# oxfords 들어가는 경로
@shop_router.get('/shop/{category}', response_class=HTMLResponse)
def shop_category(req: Request, category: str):
    pdlist = ProductService.select2_product(category)
    return templates.TemplateResponse('main_header/shop/item_gallery.html', {'request': req, 'pdlist': pdlist, 'category': category})


@shop_router.get('/itemview/{prdno}', response_class=HTMLResponse)
def view(req: Request, prdno: str):
    pd = ProductService.selectone_product(prdno)
    return templates.TemplateResponse('main_header/shop/item_detail.html', {'request': req, 'p': pd[0], 'pd': pd[1]})


@shop_router.get('/bagok/{prdno}/{mno}', response_class=HTMLResponse)
def cart(req: Request, prdno:str, mno:str):
    res_url = '/bag_error'
    result=CartService.insert_cart(prdno,mno)

    if result.rowcount > 0:
        req.session['cno'] = result.inserted_primary_key[0]
        res_url = f'/bag'
    return RedirectResponse(res_url, status_code=status.HTTP_302_FOUND)









