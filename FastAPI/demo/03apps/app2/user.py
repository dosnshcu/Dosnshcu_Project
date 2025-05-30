from fastapi import APIRouter

user_router = APIRouter()

@user_router.post("/register")
def register_post():
    return {"message": "register_post"}

@user_router.post("/login")
def login_post():
    return {"message": "login_post"}