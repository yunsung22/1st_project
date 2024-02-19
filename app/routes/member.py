from fastapi import APIRouter, Request, status
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, RedirectResponse

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

@member_router.post('/member/login')
def login(req: Request, userid: str = Form(), passwd: str = Form()):
    result = MemberService.check_login(userid, passwd)

    if result:
        req.session['userid'] = result.userid
        req.session['mno'] = result.mno
        return RedirectResponse(url='/member/myinfo', status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse(url='/member/login', status_code=status.HTTP_303_SEE_OTHER)

@member_router.get('/member/logout')
def logout(req: Request):
    req.session.clear()
    return RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)

@member_router.get('/member/myinfo', response_class=HTMLResponse)
def myinfo(req: Request):

    if 'userid' not in req.session:
        return RedirectResponse(url='/member/login', status_code=status.HTTP_303_SEE_OTHER)
    else:
        member = MemberService.select_one_member(req.session['userid'])
        return templates.TemplateResponse('/member/myinfo.html', {'request': req, 'member': member})

@member_router.get('/member/modify', response_class=HTMLResponse)
def modify(req: Request):

    if 'userid' not in req.session:
        return RedirectResponse(url='/member/login', status_code=status.HTTP_303_SEE_OTHER)
    else:
        mno = req.session['mno']
        member = MemberService.select_one(mno)[0]
        return templates.TemplateResponse('/member/modify.html', {'request': req, 'member': member})

@member_router.post('/member/modify')
def modify_member(req: Request, mdto: ModifyMember):

    if 'userid' not in req.session:
        return RedirectResponse(url='/member/login', status_code=status.HTTP_303_SEE_OTHER)
    else:
        mno = req.session['mno']
        result = MemberService.update_member(mdto, mno)
        update_cnt = result.rowcount
        return JSONResponse(content={"update_cnt": update_cnt})

@member_router.post('/member/check_id')
def check_id(req: Request, mdto: NewMember):
    member_count = MemberService.select_user_id_count(mdto)
    return member_count