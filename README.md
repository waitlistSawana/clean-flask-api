# Clean Flask APP

参考自 Flask 官方的 tutorial

https://flask.palletsprojects.com/en/3.0.x/

帮助您迅速开始一个 flask api 服务器的构建，项目可以用来：

- 创建路由和函数并引用 -- `cleanflask/__init__.py` flask 基本的 app.route 路由 

- 使用蓝图创建子路由 -- `cleanflask/blurprint.py` 

- 本地 sqlite 数据库 -- `cleanflask/schema.sql` 和 `cleanflask/db.py`

## todo

- [ ] 一键部署到 Vercel
 
## 安装项目文件

方式 1 ： `requirements.txt`

```bash
pip install -r requirements.txt
```

方式 2 ： `pyproject.toml`

```bash
pip install -e .
```

方法 3 : `cleanflask-1.0.0-py2.py3-none-any.whl`

```bash
pip install cleanflask-1.0.0-py2.py3-none-any.whl
```

## 启动

本地运行程序

```bash
flask --app cleanflask run --debugger --reload --port 5050
```

安装 sqlite 数据库

```bash
flask --app cleanflask init-db
```

## 测试 api

使用插件 " REST Client " 

`debug/apitest.http`

## 覆盖率测试

请参考 flask 官方 tutorial https://flask.palletsprojects.com/en/3.0.x/tutorial/tests/

## 部署

请参阅网站托管平台的文档