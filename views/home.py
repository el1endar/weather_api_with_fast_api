from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from fastapi.responses import RedirectResponse


router = APIRouter()
templates = Jinja2Templates('templates')


@router.get('/')
def index(request: Request):
    return templates.TemplateResponse('home/index.html', {'request': request})


@router.get('/favicon.ico')
def favicon():
    return RedirectResponse(url='static/img/favicon.ico')
