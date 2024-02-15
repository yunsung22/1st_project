from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from app.schemas.member import NewMember, ModifyMember
from app.services.member import MemberService

member_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
member_router.mount('/static', StaticFiles(directory='views/static'), name='static')

@member_router.get('/member/join', response_class=HTMLResponse)
def join(req: Request):
    return templates.TemplateResponse('/member/join.html', {'request': req})

@member_router.post('/member/join')
def joincheck(mdto: NewMember):
    result = MemberService.insert_member(mdto)
    return result.rowcount

@member_router.get('/member/joinok', response_class=HTMLResponse)
def joinok(req: Request):
    return templates.TemplateResponse('/member/joinok.html', {'request': req})

@member_router.get('/member/login', response_class=HTMLResponse)
def login(req: Request):
    return templates.TemplateResponse('/member/login.html', {'request': req})


@member_router.get('/member/myinfo', response_class=HTMLResponse)
def myinfo(req: Request):
    mno = 1
    member = MemberService.select_one(mno)[0]
    return templates.TemplateResponse('/member/myinfo.html', {'request': req, 'member': member})

@member_router.get('/member/modify', response_class=HTMLResponse)
def modify(req: Request):
    mno = 1
    member = MemberService.select_one(mno)[0]
    return templates.TemplateResponse('/member/modify.html', {'request': req, 'member': member})

@member_router.post('/member/modify')
def modify_member(req: Request, mdto: ModifyMember):
    mno = 1
    result = MemberService.update_member(mdto, mno)
    update_cnt = result.rowcount

    return JSONResponse(content={"update_cnt": update_cnt})