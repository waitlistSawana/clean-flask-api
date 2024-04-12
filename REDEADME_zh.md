# Clean Flask APP

https://flask.palletsprojects.com/en/3.0.x/

帮助您迅速开始一个 flask api 服务器的构建，项目集成了

## 安装项目文件

方式 1 ： `requirements.txt`

```pip install -r requirements.txt```

方式 2 ： `pyproject.toml`

```pip install -e .```

方法 3 : `cleanflask-1.0.0-py2.py3-none-any.whl`

```pip install cleanflask-1.0.0-py2.py3-none-any.whl```

## 启动

本地运行程序

```flask --app cleanflask run --debugger --port 5050```

安装 sqlite 数据库

```flask --app cleanflask init-db```

## 测试 api

使用插件 " REST Client " 插件

`debug/apitest.http`

## 覆盖率测试

请参考 flask 官方 tutorial https://flask.palletsprojects.com/en/3.0.x/tutorial/tests/

## 部署

请参阅网站托管平台的文档