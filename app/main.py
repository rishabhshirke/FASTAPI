from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routers import user
from app.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.templates = templates


app.include_router(user.router)


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("user/list_users.html", {"request": request})
