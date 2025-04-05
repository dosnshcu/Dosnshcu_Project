# 1.导入flask核心类
from flask import Flask


# 2.初始化web应用程序的实例化对象
app = Flask(__name__)  # __name__拿到当前文件名称
class config(object):
    DEBUG = True

app.config.from_object(config)

# 4.可以通过实例对象app提供的route装饰器，绑定视图与uri地址的关系
@app.route('/')
def index():
    # 5.默认flask支持函数式视图，视图的函数名不能重复，否则报错！！！
    # 视图的返回值将被flaSk包装成响应对象的HTML文档内容，返回给客户端。
    return 'hello world1211'

if __name__ == '__main__':
    print(app.config)
    # 3.运行flask提供的测试服务器程序
    app.run(host='0.0.0.0', port=5000)