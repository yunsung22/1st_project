from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

admin_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
admin_router.mount('/static', StaticFiles(directory='views/static'), name='static')


@admin_router.get('/mgproduct', response_class=HTMLResponse)
def mgproduct(req: Request):
    return templates.TemplateResponse('admin/mgproduct.html', {'request': req})


# @admin_router.post('/mgproduct')
# def mgproduct(mdto: NewMember):
#     result = MemberService.insert_member(mdto)
#     return result.rowcount


@admin_router.get('/mguser', response_class=HTMLResponse)
def mguser(req: Request):
    return templates.TemplateResponse('admin/mguser.html', {'request': req})


@admin_router.get('/mgVOC', response_class=HTMLResponse)
def mgVOC(req: Request):
    return templates.TemplateResponse('admin/mgVOC.html', {'request': req})