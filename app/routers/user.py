from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.database import get_db
from app.schemas.user import UserCreate, UserUpdate
from app.crud.user import get_users, get_user, create_user, update_user, delete_user

router = APIRouter(prefix="/test", tags=["Users"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def list_users(request: Request, db: Session = Depends(get_db)):
    users = get_users(db)
    return templates.TemplateResponse(
        "user/list_users.html", {"request": request, "users": users}
    )


@router.get("/create")
def create_user_form(request: Request):
    return templates.TemplateResponse("user/create_user.html", {"request": request})


# @router.post("/create")
# def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
#     create_user(db, user)
#     return RedirectResponse(url="/users", status_code=303)


# @router.get("/{user_id}/edit")
# def edit_user_form(user_id: int, request: Request, db: Session = Depends(get_db)):
#     user = get_user(db, user_id)
#     return templates.TemplateResponse(
#         "user/update_user.html", {"request": request, "user": user}
#     )


@router.post("/{user_id}/edit")
def edit_user(user_id: int, updated_data: UserUpdate, db: Session = Depends(get_db)):
    update_user(db, user_id, updated_data)
    return RedirectResponse(url="/users", status_code=303)


@router.post("/{user_id}/delete")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    delete_user(db, user_id)
    return RedirectResponse(url="/users", status_code=303)
