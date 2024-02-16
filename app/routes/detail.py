from inspect import stack

from fastapi import APIRouter, Form, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi import status

from app.schemas.product import NewProduct
from app.services.detail import DetailService

detail_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')
detail_router.mount('/static',StaticFiles(directory='views/static'),name='static')

@detail_router.get('/detail/list/{cpg}', response_class=HTMLResponse)
def list(req: Request, cpg: int):
    # stpg = int((cpg -1) / 10 ) * 10 + 1   #페이지네이션 시작값
    galist, cnt = DetailService.select_detail(cpg)
    # allpage = ceil(cnt / 25) # 총 페이지 수
    return templates.TemplateResponse('detail/list.html',
    {'request': req, 'galist': galist, 'cpg':cpg, 'stpg':1, 'allpage': 1, 'baseurl':'/detail/list/'})

@detail_router.get('/detail/list/{ftype}/{fkey}/{cpg}', response_class=HTMLResponse)
def find(req: Request, ftype: str, fkey: str, cpg: int):
    stpg = int((cpg -1) / 10 ) * 10 + 1
    # galist, cnt = BoardService.find_select_detail(ftype,'%' + fkey + '%', cpg)
    # allpage = ceil(cnt / 25)
    return templates.TemplateResponse('detail/list.html',
                                      {'request': req, 'galist': None, 'cpg':cpg, 'stpg':stpg, 'allpage': 1,
                                       'baseurl': f'/detail/list/{ftype}/{fkey}/'})


@detail_router.get('/detail/write', response_class=HTMLResponse)
def write(req: Request):
    return templates.TemplateResponse('detail/write.html', {'request': req})


@detail_router.post('/detail/write')
async def writeok(prdname: str = Form(),price: int = Form(),contents: str = Form(),
                  stack: int = Form(), salepoint:int = Form(), attach: UploadFile = File() ):
    res_url = '/detail/list/1'
    # print(title, userid, contents)
    # print(attach.filename, attach.content_type, attach.size)

    fname, fsize = await DetailService.process_upload(attach)
    gdto = NewProduct(prdname=prdname, price=price, contents=contents, stack=stack, salepoint=salepoint)
    DetailService.insert_detail(gdto, fname, fsize)

    return RedirectResponse(res_url, status_code=status.HTTP_302_FOUND)


@detail_router.get('/detail/view/{prdno}', response_class=HTMLResponse)
def view(req: Request, prdno: str):
    gal = DetailService.selectone_detail(prdno)
    # DetailService.update_count_detail(gno)
    return templates.TemplateResponse('detail/view.html', {'request': req, 'g': gal[0], 'ga': gal[1]})


