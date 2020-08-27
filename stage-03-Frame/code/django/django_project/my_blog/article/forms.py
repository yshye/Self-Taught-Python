from django import forms
from .models import ArticlePost


# 写文章的表单
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型的来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body', 'tags')
