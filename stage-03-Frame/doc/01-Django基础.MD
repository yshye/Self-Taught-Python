## Django基础

[<< 返回目录](../README.MD)

### 1. 介绍
Django 最初被设计用于具有快速开发需求的新闻类站点，目的是要实现简单快捷的网站开发。

### 2. 安装与验证
- Django 要求先安装 Python。参见下个问题中的表格，它介绍了各个 Django 版本所支持的 Python 版本。
- Django 默认使用 SQLite , 它随着Python一起安装。在生产环境中, 我们推荐使用 PostgreSQL; 但是我们同样支持 MariaDB, MySQL, SQLite, 和Oracle.
#### 2.1 我应该使用哪个版本的 Python 来配合 Django?
Django 版本	|Python 版本
---|---
1.11	|2.7, 3.4, 3.5, 3.6, 3.7 (1.11.17 添加)
2.0	|3.4，3.5，3.6，3.7
2.1	|3.5，3.6，3.7
2.2	|3.5, 3.6, 3.7, 3.8 (2.2.8 添加)
3.0, 3.1	|3.6, 3.7, 3.8


2.安装django
> py -m pip install Django

3.验证
> py -m django --version

### 3. 创建一个Django项目
```shell script
django-admin startproject projectName
```
### 4. 运行
```shell script
# 默认运行
py manage.py runserver

# 修改端口
py manage.py runserver 8080
```
### 5. 添加一个应用
```shell
py manage.py startapp applicationName
```
### 6. 数据库配置
Python内置SQLite，可选数据库有postgreSql、MySQL、Oracle<br />/setting.py 中 DATABASES 'default'中配置<br />
**ENGINE** : ` 'django.db.backends.sqlite3'`，`'django.db.backends.postgresql'`，`'django.db.backends.mysql'`，或 `'django.db.backends.oracle`<br />**NAME: **数据库名称<br />比如 [`USER`]() 、 [`PASSWORD`]() 、 [`HOST`]() 等等。想了解更多数据库设置方面的内容，请看文档：[`DATABASES`]() 。
> 如果你使用了 SQLite 以外的数据库，请确认在使用前已经创建了数据库。你可以通过在你的数据库交互式命令行中使用 "`CREATE DATABASE database_name;`" 命令来完成这件事。
> 另外，还要确保该数据库用户中提供 `mysite/settings.py` 具有 "create database" 权限。这使得自动创建的 [test database](../topics/testing/overview.html#the-test-database) 能被以后的教程使用。
> 如果你使用 SQLite，那么你不需要在使用前做任何事——数据库会在需要的时候自动创建。



- [`django.contrib.admin`](../ref/contrib/admin/index.html#module-django.contrib.admin) -- 管理员站点， 你很快就会使用它。
- [`django.contrib.auth`](../topics/auth/index.html#module-django.contrib.auth) -- 认证授权系统。
- [`django.contrib.contenttypes`](../ref/contrib/contenttypes.html#module-django.contrib.contenttypes) -- 内容类型框架。
- [`django.contrib.sessions`](../topics/http/sessions.html#module-django.contrib.sessions) -- 会话框架。
- [`django.contrib.messages`](../ref/contrib/messages.html#module-django.contrib.messages) -- 消息框架。
- [`django.contrib.staticfiles`](../ref/contrib/staticfiles.html#module-django.contrib.staticfiles) -- 管理静态文件的框架。


**自动创建数据表：**
```shell script
py manage.py migrate
```
**自动创建模型:**
```shell script
python manage.py makemigrations 应用名称
```
**数据库迁移:**
```shell script
# models文件生成一个迁移文件
python manage.py makemigrations 应用名称

# 执行迁移
python manage.py migrate

# 查看DDL
python manage.py sqlmigrate 应用名称 0001
```
输出的示例：
```sql
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" (
    "id" serial NOT NULL PRIMARY KEY,
    "question_text" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
    "id" serial NOT NULL PRIMARY KEY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL,
    "question_id" integer NOT NULL
);
ALTER TABLE "polls_choice"
  ADD CONSTRAINT "polls_choice_question_id_c5b4b260_fk_polls_question_id"
    FOREIGN KEY ("question_id")
    REFERENCES "polls_question" ("id")
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");

COMMIT;
```
### 7. 进入交互式python命令行
```shell script
py manage.py shell
```


### 8. 管理页面
#### 8.1 创建管理账户
```shell script
py manage.py createsuperuser
```
#### 8.2 访问
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

