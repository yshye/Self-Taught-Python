# redirect - 重定向
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
import markdown

from comment.models import Comment
from .models import ArticlePost, ArticleColumn

from .forms import ArticlePostForm
# 引入User模型
from django.contrib.auth.models import User
# 引入分页模块
from django.core.paginator import Paginator
# 引入 Q 对象
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.edit import CreateView


# 更新文章
# 提醒用户登录
@login_required(login_url='/userprofile/login/')
def article_update(request, pk):
    article = ArticlePost.objects.get(pk=pk)
    if request.user != article.author:
        return HttpResponse('抱歉，你没有修改文章的权限！')
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            # 新增的代码
            if request.POST['column'] != 'none':
                article.column = ArticleColumn.objects.get(id=request.POST['column'])
            else:
                article.column = None
            article.save()
            return redirect("article:detail", pk=pk)
        else:
            return HttpResponse('表单内容有误，请重新填写！')
    # 如果用户 GET 请求获取数据
    else:
        article_post_form = ArticlePostForm()
        # 新增及修改的代码
        columns = ArticleColumn.objects.all()
        context = {
            'article': article,
            'article_post_form': article_post_form,
            'columns': columns,
        }
        return render(request, 'article/update.html', context)


# 删除文章(安全)
def article_safe_delete(request, pk):
    if request.method == "POST":
        article = ArticlePost.objects.get(pk=pk)
        article.delete()
        return redirect('article:list')
    else:
        return HttpResponse("请使用POST请求删除")


# 删除文章(非安全)
def article_delete(request, pk):
    article = ArticlePost.objects.get(pk=pk)
    # 调用删除的方法
    article.delete()
    # 完成后返回文章列表
    return redirect("article:list")


# 写文章
# 提醒用户登录
@login_required(login_url='/userprofile/login/')
def article_create(request):
    if request.method == "POST":
        # 获取提交的数据，并赋值给表单实例
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的诗句是否满足模型要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1的用户作为作者
            # 如果你进行过删除数据表的操作，可能id不是1，需要重新查询下数据库中的id
            new_article.author = User.objects.get(id=request.user.id)
            # 新增的代码
            if request.POST['column'] != 'none':
                new_article.column = ArticleColumn.objects.get(id=request.POST['column'])

            # 将新文章保存到数据库中
            new_article.save()
            # 新增代码，保存 tags 的多对多关系
            article_post_form.save_m2m()
            # 完成后返回文章列表
            return redirect('article:list')
        else:
            return HttpResponse('表单内容有误，请重新填写')
    else:
        # 创建表单实例
        article_post_form = ArticlePostForm()
        # 新增及修改的代码
        columns = ArticleColumn.objects.all()
        # 赋值上下文
        context = {'article_post_form': article_post_form, 'columns': columns}
        # 返回模版
        return render(request, 'article/create.html', context)


class ArticleCreateView(CreateView):
    model = ArticlePost

    fields = '__all__'
    # 或者只填写部分字段，比如：
    # fields = ['title', 'content']

    template_name = 'article/create_by_class_view.html'


class ArticleListView(ListView):
    # 上下文的名称
    context_object_name = 'articles'
    # 查询集
    queryset = ArticlePost.objects.all()
    # 模板位置
    template_name = 'article/list.html'


def article_list(request):
    # articles = ArticlePost.objects.all()
    # context = {'articles': articles}
    # return render(request, 'article/list.html', context)
    # 修改变量名称（articles -> article_list）

    # article_all = ArticlePost.objects.all()

    # 根据GET请求中查询条件
    # 返回不同排序的对象数组
    # if request.GET.get('order') == 'total_views':
    #     article_all = ArticlePost.objects.all().order_by('-total_views')
    #     order = 'total_views'
    # else:
    #     article_all = ArticlePost.objects.all()
    #     order = 'normal'

    search = request.GET.get('search')
    order = request.GET.get('order')
    column = request.GET.get('column')
    tag = request.GET.get('tag')
    # 初始化查询集
    article_all = ArticlePost.objects.all()

    # 搜索查询集
    if search:
        article_all = article_all.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    else:
        search = ''

    # 栏目查询集
    if column is not None and column.isdigit():
        article_all = article_all.filter(column=column)

    # 标签查询集
    if tag and tag != 'None':
        article_all = article_all.filter(tags__name__in=[tag])

    # 查询集排序
    if order == 'total_views':
        article_all = article_all.order_by('-total_views')
    # 每页显示 2 篇文章
    paginator = Paginator(article_all, 6)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 articles
    articles = paginator.get_page(page)

    context = {
        'articles': articles,
        'order': order,
        'search': search,
        'column': column,
        'tag': tag,
    }
    return render(request, 'article/list.html', context)


def article_detail(request, pk):
    article = ArticlePost.objects.get(pk=pk)

    # 取出评论
    comments = Comment.objects.filter(article=pk)
    # 浏览量 +1
    article.total_views += 1
    article.save(update_fields=['total_views'])
    # 修改 Markdown 语法渲染
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )
    # 将markdown语法渲染成html样式
    article.body = md.convert(article.body)
    context = {'article': article, 'toc': md.toc, 'comments': comments}
    return render(request, 'article/detail.html', context)
