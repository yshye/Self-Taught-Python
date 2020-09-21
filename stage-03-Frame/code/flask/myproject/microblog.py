from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)


# 装饰器将该函数注册为一个shell上下文函数。 当`flask shell`命令运行时，它会调用这个函数并在shell会话中注册它返回的项目。
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, "Post": Post}
