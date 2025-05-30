import pathlib

from fastapi import FastAPI
from app1.shop import shop_router
from app2.user import user_router
import uvicorn
app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user中心接口"])
app.include_router(shop_router, prefix="/shop", tags=["shop中心接口"])

if __name__ == '__main__':
    module_name = pathlib.Path(__file__).stem
    print(module_name)
    uvicorn.run(f"{module_name}:app", host="127.0.0.1", port=8000, reload=True)
