# Django打包和发布

目前，打包 Python 程序需要工具，有许多工具可以完成此项工作。在此教程中，我们将使用 [setuptools](https://pypi.org/project/setuptools/) 来打包我们的程序。这是推荐的打包工具（与 `发布` 分支合并）。我们仍旧使用 [pip](https://pypi.org/project/pip/) 来安装和卸载这个工具。现在，你需要安装这两个包。如果你需要帮助，你可以参考 [如何通过 pip 安装 Django](../topics/install.html#installing-official-release)，你可以通过相同的方式安装 `setuptools`。

### 打包你的应用
Python 的 打包 将以一种特殊的格式组织你的应用，意在方便安装和使用这个应用。Django 本身就被打包成类似的形式。对于一个小应用，例如 polls，这不会太难。<br />

1. 首先，在你的 Django 项目目录外创建一个名为 django-polls 的文件夹，用于盛放 polls。

为你的应用选择一个名字
> 当为你的包选一个名字时，避免使用像 PyPI 这样已存在的包名，否则会导致冲突。当你创建你的发布包时，可以在模块名前增加 django- 前缀，这是一个很常用也很有用的避免包名冲突的方法。同时也有助于他人在寻找 Django 应用时确认你的 app 是 Django 独有的。
> 

应用标签（指用点分隔的包名的最后一部分）在 INSTALLED_APPS 中 必须 是独一无二的。避免使用任何与 Django contrib packages 文档中相同的标签名，比如 auth，admin，messages。


2. 将 polls 目录移入 django-polls 目录。



3. 创建一个名为 django-polls/README.rst 的文件，包含以下内容：
```
Polls
Polls is a Django app to conduct Web-based polls. For each question,
visitors can choose between a fixed number of answers.
Detailed documentation is in the "docs" directory.
Quick start
1. Add "polls" to your INSTALLED_APPS setting like this::
INSTALLED_APPS = [
...
'polls',
]
2. Include the polls URLconf in your project urls.py like this::
path('polls/', include('polls.urls')),
3. Run python manage.py migrate to create the polls models.
4. Start the development server and visit http://127.0.0.1:8000/admin/
to create a poll (you'll need the Admin app enabled).
5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
```

4. 创建一个 django-polls/LICENSE 文件。选择一个非本教程使用的授权协议，但是要足以说明发布代码没有授权证书是 不可能的 。Django 和很多兼容 Django 的应用是以 BSD 授权协议发布的；不过，你可以自己选择一个授权协议。只要确定你选择的协议能够限制未来会使用你的代码的人。
4. 下一步我们将创建 setup.cfg`和`setup.py 文件用于说明如何构建和安装应用的细节。关于此文件的完整介绍超出了此教程的范围，但是 setuptools docs 有详细的介绍。创建文件 django-polls/setup.py 包含以下内容：

django-polls/setup.cfg
```
[metadata]
name = django-polls
version = 0.1
description = A Django app to conduct Web-based polls.
long_description = file: README.rst
url = https://www.example.com/
author = Your Name
author_email = yourname@example.com
license = BSD-3-Clause  # Example license
classifiers =
Environment :: Web Environment
Framework :: Django
Framework :: Django :: X.Y  # Replace "X.Y" as appropriate
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Topic :: Internet :: WWW/HTTP
Topic :: Internet :: WWW/HTTP :: Dynamic Content
[options]
include_package_data = true
packages = find:
```
django-polls/setup.py
```python
from setuptools import setup
setup()
```

6. 默认包中只包含 Python 模块和包。为了包含额外文件，我们需要创建一个名为 MANIFEST.in 的文件。上一步中关于 setuptools 的文档详细介绍了这个文件。为了包含模板、README.rst 和我们的 LICENSE 文件，创建文件 django-polls/MANIFEST.in 包含以下内容：
```
django-polls/MANIFEST.in
include LICENSE
include README.rst
recursive-include polls/static *
recursive-include polls/templates *
```

7. 在应用中包含详细文档是可选的，但我们推荐你这样做。创建一个空目录 django-polls/docs 用于未来编写文档。额外添加一行至 django-polls/MANIFEST.in
```
recursive-include docs *
```
注意，现在 docs 目录不会被加入你的应用包，除非你往这个目录加几个文件。许多 Django 应用也提供他们的在线文档通过类似 readthedocs.org 这样的网站。

8. 试着构建你自己的应用包通过 ptyhon setup.py sdist （在 django-polls`目录内）。这将创建一个名为`dist 的目录并构建你自己的应用包， django-polls-0.1.tar.gz。

更多关于打包的信息，见 Python 的 关于打包和发布项目的教程。<br />

### 使用你自己的包名
由于我们把 polls 目录移出了项目，所以它无法工作了。我们现在要通过安装我们的新 django-polls 应用来修复这个问题。<br />
<br />作为用户库安装
> 以下步骤将 django-polls 以用户库的形式安装。与安装整个系统的软件包相比，用户安装具有许多优点，例如可在没有管理员访问权的系统上使用，以及防止应用包影响系统服务和其他用户。
> 


> Note that per-user installations can still affect the behavior of system tools that run as that user, so using a virtual environment is a more robust solution (see below).



1. 为了安装这个包，使用 pip (你早已 安装 pip, 对吗？):
```shell
python -m pip install --user django-polls/dist/django-polls-0.1.tar.gz
```

2. 幸运的话，你的 Django 项目应该再一次正确运行。启动服务器确认这一点。



3. 通过 pip 卸载包:
```shell
python -m pip uninstall django-polls
```
### 发布你的应用
现在，你已经对 django-polls 完成了打包和测试，准备好向世界分享它！如果这不是一个例子应用，你现在就可以这样做。<br />

- 通过邮件将你的包发送给朋友。
- 将这个包上传至你的网站。
- 将你的包发布至公共仓库，比如 [the Python Package Index (PyPI)](https://pypi.python.org/pypi)。 [packaging.python.org](https://packaging.python.org/) 有一个不错的 [教程](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives) 说明如何发布至公共仓库。



### 使用和卸载
```shell
# 安装
python -m pip install --user django-polls/dist/django-polls-0.1.tar.gz

# 卸载
python -m pip uninstall django-polls
```


