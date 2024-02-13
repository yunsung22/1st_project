from fastapi import APIRouter, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.schemas.product import NewProduct
from app.services.product import ProductService

admin_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
admin_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@admin_router.get('/mgproduct', response_class=HTMLResponse)
def mgproduct(req: Request):
    return templates.TemplateResponse('admin/mgproduct.html', {'request': req})


@admin_router.get('/rgproduct', response_class=HTMLResponse)
def rgproduct(req: Request):
    return templates.TemplateResponse('admin/rgproduct.html', {'request': req})


@admin_router.post('/rgproduct')
def rgproductok(pdto: NewProduct):
    result = ProductService.insert_product(pdto)
    res_url = '/error'
    if result.rowcount > 0: res_url = '/admin/mgproduct'
    return RedirectResponse(res_url, status_code=status.HTTP_302_FOUND)


@admin_router.get('/mguser', response_class=HTMLResponse)
def mguser(req: Request):
    return templates.TemplateResponse('admin/mguser.html', {'request': req})


@admin_router.get('/mgVOC', response_class=HTMLResponse)
def mgVOC(req: Request):
    return templates.TemplateResponse('admin/mgVOC.html', {'request': req})