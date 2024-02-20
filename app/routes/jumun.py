from fastapi import APIRouter, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from app.services.jumun import JumunService

jumun_router = APIRouter()
# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
jumun_router.mount('/static', StaticFiles(directory='views/static'), name='static')

# 장바구니 x
@jumun_router.get('/bag', response_class=HTMLResponse)
def bagx(req: Request):
    if 'userid' not in req.session:
        return RedirectResponse(url='/member/login', status_code=status.HTTP_303_SEE_OTHER)
    elif 'jumun' in req.session:
        jmno = req.session['jmno']
        jumun = JumunService.select_jumun(jmno)[0]
        return templates.TemplateResponse('bag.html', {'request': req, 'jumun': jumun})
    else:
        return templates.TemplateResponse('bagx.html', {'request': req})



        # if 'jumun' :
        #     return templates.TemplateResponse('bag.html', {'request': req, 'jumun': jumun, 'member':member})
        # else :
        #     return

# 장바구니 o
# @jumun_router.get('/bag', response_class=HTMLResponse)
# def bag(req: Request):
#     if 'jmno' not in req.session:
#         return RedirectResponse(url='/member/login', status_code=status.HTTP_303_SEE_OTHER)
#     else:
#         member = MemberService.select_one_member(req.session['userid'])
#         jmno = req.session['jmno']
#         jumun = JumunService.select_jumun(jmno)[0]
#         return templates.TemplateResponse('jumun.html', {'request': req, 'jumun': jumun, 'member':member})


@jumun_router.get('/jumun', response_class=HTMLResponse)
def jumun(req: Request):
    return templates.TemplateResponse('/jumun.html', {'request': req})

@jumun_router.get('/payment', response_class=HTMLResponse)
def payment(req: Request):
    return templates.TemplateResponse('payment.html', {'request': req})

# @jumun_router.get('/orderhistory', response_class=HTMLResponse)
# def orderhistory(req: Request):
#     return templates.TemplateResponse('orderhistory.html', {'request': req})



