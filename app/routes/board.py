from math import ceil

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi import status
from app.schemas.board import NewBoard
from app.services.board import BoardService

board_router = APIRouter()

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
board_router.mount('/static', StaticFiles(directory='views/static'), name='static')

@board_router.get('/list/{cpg}', response_class=HTMLResponse)
def list(req: Request, cpg: int):
    stpg = int((cpg -1) / 10 ) * 10 + 1   #페이지네이션 시작값
    bdlist, cnt = BoardService.select_board(cpg)
    allpage = ceil(cnt / 25) # 총 페이지 수
    return templates.TemplateResponse('board/list.html',
                                      {'request': req, 'bdlist': bdlist, 'cpg':cpg, 'stpg':stpg, 'allpage': allpage, 'baseurl':'/list/'})

@board_router.get('/list/{ftype}/{fkey}/{cpg}', response_class=HTMLResponse)
def find(req: Request, ftype: str, fkey: str, cpg: int):
    stpg = int((cpg -1) / 10 ) * 10 + 1
    bdlist, cnt = BoardService.find_select_board(ftype,'%' + fkey + '%', cpg)
    allpage = ceil(cnt / 25)
    return templates.TemplateResponse('board/list.html',
                                      {'request': req, 'bdlist': bdlist, 'cpg':cpg, 'stpg':stpg, 'allpage': allpage,
                                       'baseurl': f'/list/{ftype}/{fkey}/'})

# 고객센터 글쓰기 들어가기
@board_router.get('/write', response_class=HTMLResponse)
def write(req: Request):
    return templates.TemplateResponse('board/write.html', {'request': req})


# 고객센터 글 쓰기
@board_router.post('/write')
def writeok(bdto: NewBoard):
    res_url = '/captcha_error'
    if BoardService.check_captcha(bdto): #captcha 체크가 true라면
        result = BoardService.insert_board(bdto)
        res_url = '/error'
        if result.rowcount > 0: res_url = '/list/1'
    return RedirectResponse(res_url, status_code=status.HTTP_302_FOUND)



# 고객센터 글읽기
@board_router.get('/view/{bno}', response_class=HTMLResponse)
def view(req: Request, bno: str):
    bd = BoardService.selectone_board(bno)[0]
    BoardService.update_count_board(bno)
    return templates.TemplateResponse('board/view.html', {'request': req, 'bd': bd})
