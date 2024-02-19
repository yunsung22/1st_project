from math import ceil
from typing import List, Dict

from fastapi import APIRouter, Request, status, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.schemas.product import NewData, NewProduct, PrdAttach, RowData
from app.services.product import ProductService

admin_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
admin_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@admin_router.get('/mgproduct/{cpg}', response_class=HTMLResponse)
def mgproduct(req: Request, cpg: int):
    stpg = int((cpg - 1) / 10) * 10 + 1
    pdlist, cnt = ProductService.select_product(cpg)
    allpage = ceil(cnt / 15)
    return templates.TemplateResponse('admin/mgproduct.html', {'request': req, 'pdlist':pdlist,
        'cpg': cpg, 'stpg': stpg, 'allpage': allpage, 'baseurl': '/admin/mgproduct/'})


@admin_router.post('/mgproduct')
def mgproductok(rows_data: Dict[int, RowData]):
    result = ProductService.update_product(rows_data)
    res_url = '/error'
    if result.rowcount > 0: res_url = '/admin/mgproduct/1'
    return RedirectResponse(res_url, status_code=status.HTTP_302_FOUND)


@admin_router.get('/rgproduct', response_class=HTMLResponse)
def rgproduct(req: Request):
    return templates.TemplateResponse('admin/rgproduct.html', {'request': req})


@admin_router.post('/rgproduct')
def rgproductok(dto: NewData):
    pdto = NewProduct(prdname=dto.prdname, category=dto.category, stack=dto.stack, price=dto.price)
    result = ProductService.insert_product(pdto)
    padto = PrdAttach(prdno=result.inserted_primary_key[0], img1=dto.img1, img2=dto.img2, img3=dto.img3, img4=dto.img4)
    result = ProductService.insert_prdattach(padto)

    res_url = '/error'
    if result.rowcount > 0: res_url = '/admin/mgproduct/1'
    return RedirectResponse(res_url, status_code=status.HTTP_302_FOUND)


@admin_router.post('/upload')
async def upload(images: List[UploadFile] = File()):
    list = await ProductService.process_upload(images)
    return {"message":"이미지업로드 성공", "filename" : list}


@admin_router.get('/mguser', response_class=HTMLResponse)
def mguser(req: Request):
    return templates.TemplateResponse('admin/mguser.html', {'request': req})


@admin_router.get('/mgVOC', response_class=HTMLResponse)
def mgVOC(req: Request):
    return templates.TemplateResponse('admin/mgVOC.html', {'request': req})