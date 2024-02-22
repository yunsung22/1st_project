from fastapi import APIRouter, Request, status, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from app.schemas.jumun import Jumun, NewJumun
from app.services.cart import CartService
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
    elif 'mno' in req.session:
        mno = req.session['mno']
        cart = CartService.select_cart(mno)
        if not cart:
            return templates.TemplateResponse('bagx.html', {'request': req})
        return templates.TemplateResponse('bag.html', {'request': req, 'cart': cart})




@jumun_router.post('/jumun', response_class=HTMLResponse)
def jumun(req: Request,jmcno=Form(), jmmno=Form()):
    jmcart = CartService.select_jumun_cart(jmcno)
    jmuser = CartService.select_jumun_user(jmmno)
    return templates.TemplateResponse('/jumun.html', {'request': req, 'jmcart':jmcart, 'jmuser':jmuser})



@jumun_router.post('/payment')
def payment(req: Request, jmdto: NewJumun):
    res_url = '/jumun_error'
    result = JumunService.insert_jumun(jmdto)
    if result.rowcount > 0:
        cno = jmdto.cno

        delete_result = CartService.delete_cart(cno)
        if delete_result:
            res_url = '/payment'
        else:
            res_url ='/payment_error'
    return RedirectResponse(res_url, status_code=status.HTTP_302_FOUND)

@jumun_router.get('/payment', response_class=HTMLResponse)
def paymentok(req: Request):
    return templates.TemplateResponse('/payment.html', {'request': req})

@jumun_router.get('/oderhistory', response_class=HTMLResponse)
def oderhistory(req: Request):
    jmpay = JumunService.select_orderhistory(req.session['mno'])
    return templates.TemplateResponse('/oderhistory.html', {'request': req, 'jmpay':jmpay})