from fastapi import APIRouter, Request, status
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, RedirectResponse

from app.schemas.member import NewMember, ModifyMember, TempMember
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

@member_router.get('/member/reset_passwd', response_class=HTMLResponse)
def reset_passwd(req: Request):
    return templates.TemplateResponse('/member/reset_passwd.html', {'request': req})

@member_router.post('/member/reset_passwd')
def reset_passwd(req: Request, mdto: TempMember):
    new_password = MemberService.generate_temp_password()
    result = MemberService.update_member_passwd(mdto, new_password)
    update_cnt = result.rowcount

    result_msg = ''
    if update_cnt > 0 :
        result_msg = f'임시비밀번호 {new_password}로 변경 되었습니다.'
    else :
        result_msg = '일치하는 회원정보가 없습니다. 다시 입력해 주세요.'

    return JSONResponse(content={"result_msg": result_msg})