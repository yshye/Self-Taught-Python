# 引入path
from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    # 目前还没有urls
    path('article-list/', views.article_list, name='list'),
    path('<int:pk>/article-detail', views.article_detail, name='detail'),
    path('article-create', views.article_create, name='create'),
    path('<int:pk>/article-delete', views.article_delete, name='delete'),
    path('<int:pk>/article-safe-delete', views.article_safe_delete, name='safe-delete'),
    path('<int:pk>/article-update', views.article_update, name='update'),
    path('create-view/', views.ArticleCreateView.as_view(), name='create-view'),
]
