from fastapi import APIRouter, Request, status, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from app.services.cart import CartService

jumun_router = APIRouter()
# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
jumun_router.mount('/static', StaticFiles(directory='views/static'), name='static')

# 장바구니 x
@jumun_router.get('/bag', response_class=HTMLResponse)
def bagx(req: Request):
    if 'userid' not in req.session:
        return RedirectResponse(url='/member/login', status_code=status.HTTP_303_SEE_OTHER)
    elif 'mno' in req.session:
        mno = req.session['mno']
        cart = CartService.select_cart(mno)
        print(len(cart))
        return templates.TemplateResponse('bag.html', {'request': req, 'cart': cart})
    else:
        return templates.TemplateResponse('bagx.html', {'request': req})





#  장바구니에서 카트번호, 고객번호 전달 후
#  결제페이지에서 다시 카트정보,고객정보 추출 후 출력
@jumun_router.post('/jumun', response_class=HTMLResponse)
def jumun(req: Request,jmcno=Form(), jmmno=Form()):
    jmcart = CartService.select_jumun_cart(jmcno)
    jmuser = CartService.select_jumun_user(jmmno)
    return templates.TemplateResponse('/jumun.html', {'request': req, 'jmcart':jmcart, 'jmuser':jmuser})

@jumun_router.get('/payment', response_class=HTMLResponse)
def payment(req: Request,pacno=Form(), pamno=Form()):
    pacart = CartService.select_pay_cart(pacno)
    pauser = CartService.select_pay_user(pamno)
    return templates.TemplateResponse('/pament.html', {'request': req, 'pacart':pacart, 'pauser':pauser})

# @jumun_router.get('/orderhistory', response_class=HTMLResponse)
# def orderhistory(req: Request):
#     return templates.TemplateResponse('orderhistory.html', {'request': req})