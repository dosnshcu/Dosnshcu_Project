import pathlib
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")  # 路径操作装饰器
def home():  # 路径操作函数
    return {'message': 'hello world'}

if __name__ == "__main__":
    # 自动获取当前文件名（去掉 .py 后缀）
    module_name = pathlib.Path(__file__).stem
    print(module_name)
    uvicorn.run(f"{module_name}:app", host="127.0.0.1", port=8000, reload=True)