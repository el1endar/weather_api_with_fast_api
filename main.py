import sys

sys.path.append("../models")
sys.path.append("../services")
sys.path.append("../config")

from fastapi import FastAPI
import uvicorn
from starlette.staticfiles import StaticFiles

from api import weather_api
from views import home


app = FastAPI()


def configure():
    configure_routing()


def configure_routing():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(weather_api.router)


if __name__ == "__main__":
    configure()
    uvicorn.run(app, port=8000, host='127.0.0.1')

else:
    configure()
