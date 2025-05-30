from fastapi import APIRouter

shop_router = APIRouter()

@shop_router.get("/shop")
def shop_get():
    return {"message": "shop_get"}