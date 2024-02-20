from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from httpie import status
from app.services.jumun import JumunService
from app.services.member import MemberService

jumun_router = APIRouter()
# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
jumun_router.mount('/static', StaticFiles(directory='views/static'), name='static')

# 장바구니 x
@jumun_router.get('/bagx', response_class=HTMLResponse)
def bagx(req: Request):
    if 'jmno' not in req.session:
        return templates.TemplateResponse('bagx.html', {'request': req})

# 장바구니 o
@jumun_router.get('/bag', response_class=HTMLResponse)
def bag(req: Request):
    # if 'userid' not in req.session:
    #     return RedirectResponse(url='/member/login', status_code=status.HTTP_303_SEE_OTHER)
    # else:
    #     member = MemberService.select_one_member(req.session['userid'])
    #     jmno = req.session['jmno']
    #     jumun = JumunService.select_one(jmno)[0]
    #     return templates.TemplateResponse('jumun.html', {'request': req, 'jumun': jumun, 'member':member})
    return templates.TemplateResponse('/bag.html', {'request': req})

@jumun_router.get('/jumun', response_class=HTMLResponse)
def jumun(req: Request):
    if 'jmno' not in req.session:
        return RedirectResponse(url='/member/login', status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse('/jumun.html', {'request': req})

@jumun_router.get('/payment', response_class=HTMLResponse)
def payment(req: Request):
    return templates.TemplateResponse('payment.html', {'request': req})

# @jumun_router.get('/orderhistory', response_class=HTMLResponse)
# def orderhistory(req: Request):
#     return templates.TemplateResponse('orderhistory.html', {'request': req})



