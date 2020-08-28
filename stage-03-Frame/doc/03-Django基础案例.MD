## Django基础案例

[<< 返回目录](../README.MD)

### 1. 项目准备
#### 1.1 创建项目
```shell script
django-admin startproject bookmanager
```
#### 1.2 创建应用
```shell script
python manager.py startapp book
```
#### 1.3 安装应用
settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 添加子应用
    'book.apps.BookConfig'
]
```

#### 1.4 配置本地化
setting.py
```python
#设置中文
LANGUAGE_CODE = 'zh-Hans'
#亚洲上海时区
TIME_ZONE = 'Asia/Shanghai'
```
####  1.5 配置模版路径
- 在应用同级目录下，创建`templates`模版文件夹
- setting.py
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 配置模版
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

#### 1.6 项目中匹配urls
- book应用下创建`urls.py`文件
```python
from django.conf.urls import url


urlpatterns = [
]

```
- 在项目的`urls.py`文件内添加应用urls
```python
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('book.urls'))
]
```

#### 1.7 准备视图
book/views.py
```python
# 定义视图：提供书籍列表信息
def book_list(request):

    return HttpResponse('OK!')
```

#### 1.8 配置应用`urls.py`
book/urls.py
```python
from django.conf.urls import url
from book.views import *

urlpatterns = [
    url(r'^booklist/$', bool_list),
]

```

#### 1.9 开启服务器
```shell script
 # 进入项目文件中, 开启项目对应的服务器
 python manage.py runserver

 # 浏览器中输入网址
 http://127.0.0.1:8000/booklist/
```

### 2. 配置MySQL数据库
Django默认使用的是sqlite数据库，这里我们配置为mysql数据库
#### 2.1 在MySQL中创建数据库
```sql
create database book charset=utf8;
```
#### 2.2 修改`DATABASE`配置信息
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'book'  # 数据库名字
    }
}
```
#### 2.3 安装数据库驱动
```shell script
pip install PyMySQL
```
#### 2.4 在工程同名子目录的`__init__.py`文件中添加
```python
import pymysql

pymysql.install_as_MySQLdb()
```
* 作用是让Django的ORM能以mysqldb的方式来调用PyMySQL。

### 3. 数据库迁移
- 模型在`应用/models.py`文件中
- 模型需要继承`django.db.models.Model`

#### 3.1 定义模型
```python
from django.db import models


# 准备书籍列表信息的模型类
class BookInfo(models.Model):
    # 创建字段，字段类型...
    name = models.CharField(max_length=20, verbose_name='名称')
    pub_date = models.DateField(verbose_name='发布日期',null=True)
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'bookinfo'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name

# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name

```

#### 3.2 数据库迁移
> 将模型迁移到数据库
##### 1> 生成迁移文件
```shell script
python manage.py makemigrations
```
##### 2> 同步到数据库中
```shell script
python manage.py migrate
```
* 执行成功后，可在数据库中查看到新增了对应的数据表

### 4. 添加测试数据
```mysql
insert into bookinfo(name, pub_date, readcount,commentcount, is_delete) values
('射雕英雄传', '1980-5-1', 12, 34, 0),
('天龙八部', '1986-7-24', 36, 40, 0),
('笑傲江湖', '1995-12-24', 20, 80, 0),
('雪山飞狐', '1987-11-11', 58, 24, 0);

insert into peopleinfo(name, gender, book_id, description, is_delete)  values
    ('郭靖', 1, 1, '降龙十八掌', 0),
    ('黄蓉', 0, 1, '打狗棍法', 0),
    ('黄药师', 1, 1, '弹指神通', 0),
    ('欧阳锋', 1, 1, '蛤蟆功', 0),
    ('梅超风', 0, 1, '九阴白骨爪', 0),
    ('乔峰', 1, 2, '降龙十八掌', 0),
    ('段誉', 1, 2, '六脉神剑', 0),
    ('虚竹', 1, 2, '天山六阳掌', 0),
    ('王语嫣', 0, 2, '神仙姐姐', 0),
    ('令狐冲', 1, 3, '独孤九剑', 0),
    ('任盈盈', 0, 3, '弹琴', 0),
    ('岳不群', 1, 3, '华山剑法', 0),
    ('东方不败', 0, 3, '葵花宝典', 0),
    ('胡斐', 1, 4, '胡家刀法', 0),
    ('苗若兰', 0, 4, '黄衣', 0),
    ('程灵素', 0, 4, '医术', 0),
    ('袁紫衣', 0, 4, '六合拳', 0);
```

### 5. 数据操作-增、改、删
> 利用 shell 工具进行数据操作

#### 5.1 进入shell界面
```shell script
py manage.py shell
```
#### 5.2 增加
- 通过创建模型类对象，执行对象的save()方法保存到数据库中
```shell script
>>> from book.models import BookInfo,PeopleInfo
>>> book = BookInfo(
...         name='python入门',
...         pub_date='2010-1-1'
...     )
>>> book.save()
>>> book
<BookInfo: python入门>
```

- 通过模型类.objects.create()保存。
```shell script
>>> PeopleInfo.objects.create(
...         name='itheima',
...         book=book
...     )
<PeopleInfo: itheima>
```
#### 5.2 修改
- 修改模型类对象的属性，然后执行save()方法
```shell script
>>> person = PeopleInfo.objects.get(name='itheima')
>>> person.name = 'itcast'
>>> person.save()
>>> person
<PeopleInfo: itcast>
```
- 使用模型类.objects.filter().update()，会返回受影响的行数
```shell script
>>> PeopleInfo.objects.filter(name='itcast').update(name='传智播客')
1
```
#### 5.3 删除
- 模型类对象delete
```shell script
>>> person = PeopleInfo.objects.get(name='传智播客')
>>> person.delete()
(1, {'book.PeopleInfo': 1})
```
- 模型类.objects.filter().delete()
```shell script
>>> BookInfo.objects.filter(name='python入门').delete()
(1, {'book.BookInfo': 1, 'book.PeopleInfo': 0})
```

### 6. 数据操作-查询
#### 6.1 基本查询
- `get`查询单一结果，如果不存在会抛出模型类`.DoesNotExist`异常。
- `all`查询多个结果。
- `count`查询结果数量。
```shell script
>>> BookInfo.objects.get(id=1)
<BookInfo: 射雕英雄传>

>>> BookInfo.objects.get(pk=2)
<BookInfo: 天龙八部>

>>> BookInfo.objects.get(pk=20)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/python/.virtualenvs/py3_django_1.11/lib/python3.5/site-packages/django/db/models/manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/python/.virtualenvs/py3_django_1.11/lib/python3.5/site-packages/django/db/models/query.py", line 380, in get
    self.model._meta.object_name
book.models.DoesNotExist: BookInfo matching query does not exist.


>>> BookInfo.objects.all()
<QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>, <BookInfo: 笑傲江湖>, <BookInfo: 雪山飞狐>]>

>>> BookInfo.objects.count()
4
```
#### 6.2 过滤查询
- `filter`过滤出多个结果
- `exclude`排除掉符合条件剩下的结果
- `get`过滤单一结果

##### 1> 相等
> `exact`：表示判等。
```shell script
BookInfo.objects.filter(id__exact=1)
可简写为：
BookInfo.objects.filter(id=1)
```

##### 2> 模糊查询
- `contains`：是否包含。
> 说明：如果要包含%无需转义，直接写即可。
```shell script
BookInfo.objects.filter(name__contains='传')
<QuerySet [<BookInfo: 射雕英雄传>]>
```
- `startswith`、`endswith`：以指定值开头或结尾。
```shell script
>>> BookInfo.objects.filter(name__endswith='部')
<QuerySet [<BookInfo: 天龙八部>]>
```

\* 以上运算符都区分大小写，在这些运算符前加上`i`表示不区分大小写，如`iexact`、`icontains`、`istartswith`、`iendswith`.

##### 3> 空查询
- `isnull`：是否为null。
```shell script
>>> BookInfo.objects.filter(name__isnull=True)
<QuerySet []>
```

##### 4> 范围查询
- `in`：是否包含在范围内。
```shell script
>>> BookInfo.objects.filter(id__in=[1,3,5])
<QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 笑傲江湖>]>

```

##### 5> 比较查询
- `gt` 大于 (greater then)
- `gte` 大于等于 (greater then equal)
- `lt` 小于 (less then)
- `lte` 小于等于 (less then equal)
- 不等于的运算符，使用`exclude()`过滤器。
```shell script
# 查询编号大于3的图书
>>> BookInfo.objects.filter(id__gt=3)
<QuerySet [<BookInfo: 雪山飞狐>]>
```

##### 6> 日期查询
`year`、`month`、`day`、`week_day`、`hour`、`minute`、`second`：对日期时间类型的属性进行运算。
```shell script
# 查询1980年发表的图书。
>>> BookInfo.objects.filter(pub_date__year=1980)
<QuerySet [<BookInfo: 射雕英雄传>]>
# 查询1990年1月1日后发表的图书。
>>> BookInfo.objects.filter(pub_date__gt='1990-1-1')
<QuerySet [<BookInfo: 笑傲江湖>]>
```

### 7. F和Q对象
#### 7.1 F对象
> F对象被用作属性和属性的比较

**基本语法**
```text
F(属性名)
```
- 查询阅读量大于等于评论量的图书。
```shell script
>>> from django.db.models import F
>>> BookInfo.objects.filter(readcount__gt=F('commentcount'))
<QuerySet [<BookInfo: 雪山飞狐>]>
```
- 查询阅读量大于2倍评论量的图书。
```shell script
>>> BookInfo.objects.filter(readcount__gt=F('commentcount')*2)
<QuerySet [<BookInfo: 雪山飞狐>]>
```

#### 7.2 Q对象
多个过滤器逐个调用表示逻辑与关系，同`sql`语句中`where`部分的`and`关键字。
```shell script
>>> BookInfo.objects.filter(readcount__gt=20,id__lt=3)
<QuerySet [<BookInfo: 天龙八部>]>

# 或者

>>> BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
<QuerySet [<BookInfo: 天龙八部>]>
```

> 如果需要实现逻辑或`or`的查询，需要使用`Q()`对象结合`|`运算符。

##### Q查询的基本语法
```shell script
Q(属性名__运算符=值)
```
- 查询阅读量大于20的图书，改写为Q对象如下。
```shell script
>>> BookInfo.objects.filter(Q(readcount__gt=20))
```

- Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或。
```shell script
# 查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
>>> BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
<QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>, <BookInfo: 雪山飞狐>]>
```
- Q对象前可以使用~操作符，表示非not。
```shell script
# 查询编号不等于3的图书。
>>> BookInfo.objects.filter(~Q(id=3))
<QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>, <BookInfo: 雪山飞狐>]>
```

### 8. 聚合查询
> 使用`aggregate()`过滤器调用聚合函数。聚合函数包括：`Avg`平均，`Count`数量，`Max`最大，`Min`最小，`Sum`求和，被定义在`django.db.models`中。

- 查询图书的总阅读量。
```shell script
>>> from django.db.models import Sum
>>> BookInfo.objects.aggregate(Sum('readcount'))
{'readcount__sum': 126}
```

- Count一般不使用`aggregate()`
```shell script
>>> BookInfo.objects.count()
```

### 9. 排序
使用order_by对结果进行排序
```shell script
# 默认升序
>>> BookInfo.objects.all().order_by('readcount')
<QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 笑傲江湖>, <BookInfo: 天龙八部>, <BookInfo: 雪山飞狐>]>

# 降序
>>> BookInfo.objects.all().order_by('-readcount')
<QuerySet [<BookInfo: 雪山飞狐>, <BookInfo: 天龙八部>, <BookInfo: 笑傲江湖>, <BookInfo: 射雕英雄传>]>
```

### 10. 关联查询
#### 10.1 一对应
> 模型类对象.多对应的模型类名小写_set 
```shell script
>>> book = BookInfo.objects.get(id=1)
>>> book.peopleinfo_set.all()
<QuerySet [<PeopleInfo: 郭靖>, <PeopleInfo: 黄蓉>, <PeopleInfo: 黄药师>, <PeopleInfo: 欧阳锋>, <PeopleInfo: 梅超风>]>
```

#### 10.2 多对应
> 模型类对象.多对应的模型类中的关系类属性名
```shell script
>>> person = PeopleInfo.objects.get(id=1)
>>> person.book
<BookInfo: 射雕英雄传>
>>> person.book_id
1
```

#### 10.3 关联过滤查询
> 关联模型类名小写__属性名__条件运算符=值

##### 由多模型类条件查询一模型类数据:
- 查询图书，要求图书人物为"郭靖"
```shell script
>>> book = BookInfo.objects.filter(peopleinfo__name='郭靖')
>>> book
<QuerySet [<BookInfo: 射雕英雄传>]>
```

- 查询图书，要求图书中人物的描述包含"八"
```shell script
>>> book = BookInfo.objects.filter(peopleinfo__description__contains='八')
>>> book
<QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>]>
```
- 查询图书，要求图书中人物的描述包含"八"
```shell script
>>> book = BookInfo.objects.filter(peopleinfo__description__contains='八')
>>> book
<QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>]>
```

##### 由一模型类条件查询多模型类数据:
> 一模型类关联属性名__一模型类属性名__条件运算符=值

- 查询书名为“天龙八部”的所有人物。
```shell script
>>> people = PeopleInfo.objects.filter(book__name='天龙八部')
>>> people
<QuerySet [<PeopleInfo: 乔峰>, <PeopleInfo: 段誉>, <PeopleInfo: 虚竹>, <PeopleInfo: 王语嫣>]>
```

- 查询图书阅读量大于30的所有人物
```shell script
>>> people = PeopleInfo.objects.filter(book__readcount__gt=30)
>>> people
<QuerySet [<PeopleInfo: 乔峰>, <PeopleInfo: 段誉>, <PeopleInfo: 虚竹>, <PeopleInfo: 王语嫣>, <PeopleInfo: 胡斐>, <PeopleInfo: 苗若兰>, <PeopleInfo: 程灵素>, <PeopleInfo: 袁紫衣>]>

```

### 11. 查询集QuerySet
#### 11.1 概念
Django的ORM中存在查询集的概念。

查询集，也称查询结果集、QuerySet，表示从数据库中获取的对象集合。

当调用如下过滤器方法时，Django会返回查询集（而不是简单的列表）：

- `all()`：返回所有数据。
- `filter()`：返回满足条件的数据。
- `exclude()`：返回满足条件之外的数据。
- `order_by()`：对结果进行排序。

对查询集可以再次调用过滤器进行过滤，如
```shell script
>>> books = BookInfo.objects.filter(readcount__gt=30).order_by('pub_date')
>>> books
<QuerySet [<BookInfo: 天龙八部>, <BookInfo: 雪山飞狐>]>
```

也就意味着查询集可以含有零个、一个或多个过滤器。过滤器基于所给的参数限制查询的结果。

从SQL的角度讲，查询集与select语句等价，过滤器像where、limit、order by子句。

判断某一个查询集中是否有数据：

- `exists()`：判断查询集中是否有数据，如果有则返回True，没有则返回False。
#### 11.2 两大特性
##### 1）惰性执行
创建查询集不会访问数据库，直到调用数据时，才会访问数据库，调用数据的情况包括迭代、序列化、与if合用

例如，当执行如下语句时，并未进行数据库查询，只是创建了一个查询集books
```shell script
books = BookInfo.objects.all()
```
继续执行遍历迭代操作后，才真正的进行了数据库的查询
```shell script
for book in books:
    print(book.name)
```

###### 2）缓存
使用同一个查询集，第一次使用时会发生数据库的查询，然后Django会把结果缓存下来，再次使用这个查询集时会使用缓存的数据，减少了数据库的查询次数。

- 情况一：如下是两个查询集，无法重用缓存，每次查询都会与数据库进行一次交互，增加了数据库的负载。

```shell script
from book.models import BookInfo

[book.id for book in BookInfo.objects.all()]

[book.id for book in BookInfo.objects.all()]
```
- 情况二：经过存储后，可以重用查询集，第二次使用缓存中的数据。

```shell script
books=BookInfo.objects.all()

[book.id for book in books]

[book.id for book in books]
```

#### 11.3 限制查询集
可以对查询集进行取下标或切片操作，等同于sql中的limit和offset子句。

注意：不支持负数索引。

对查询集进行切片后返回一个新的查询集，不会立即执行查询。

如果获取一个对象，直接使用[0]，等同于[0:1].get()，但是如果没有数据，[0]引发IndexError异常，[0:1].get()如果没有数据引发DoesNotExist异常。

示例：获取第1、2项，运行查看。
```shell script
>>> books = BookInfo.objects.all()[0:2]
>>> books
<QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>]>
```

#### 11.4 分页
```shell script
#查询数据
books = BookInfo.objects.all()
#导入分页类
from django.core.paginator import Paginator
#创建分页实例
paginator=Paginator(books,2)
#获取指定页码的数据
page_skus = paginator.page(1)
#获取分页数据
total_page=paginator.num_pages
```
