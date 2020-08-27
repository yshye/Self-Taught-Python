from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from userprofile.forms import UserLoginForm, UserRegisterForm
# 引入验证登录的装饰器
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm
from .models import Profile


@login_required(login_url='/userprofile/login')
def profile_edit(request, pk):
    user = User.objects.get(pk=pk)
    if Profile.objects.filter(user_id=pk).exists():
        profile = Profile.objects.get(user_id=pk)
    else:
        profile = Profile.objects.create(user=user)
    # profile = Profile.objects.get(user_id=id)
    if request.method == "POST":
        if request.user != user:
            return HttpResponse('无权限')
        # 上传的文件保存在 request.FILES 中，通过参数传递给表单类
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_cd = profile_form.cleaned_data
            profile.phone = profile_cd['phone']
            profile.bio = profile_cd['bio']
            # 添加在 profile.bio = profile_cd['bio'] 后面
            # 如果 request.FILES 存在文件，则保存
            if 'avatar' in request.FILES:
                profile.avatar = profile_cd["avatar"]
            profile.save()
            return redirect('userprofile:edit', pk=pk)
        else:
            return HttpResponse('注册表单输入有误，请重新输入')
    elif request.method == "GET":
        profile_form = ProfileForm()
        context = {'profile_form': profile_form, 'profile': profile, 'user': user}
        return render(request, 'userprofile/edit.html', context)
    else:
        return HttpResponse('请使用GET或POST请求数据')


@login_required(login_url='/userprofile/login')
def user_delete(request, pk):
    if request.method == "POST":
        user = User.objects.get(pk=pk)
        if request.user == user:
            logout(request)
            user.delete()
            return redirect('article:list')
        else:
            return HttpResponse('你没有删除权限')
    else:
        return HttpResponse('仅接受POST请求')


# 用户注册
def user_register(request):
    if request.method == "POST":
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save()
            login(request, new_user)
            return redirect('article:list')
        else:
            # 输入密码不规范都会被检测为invalid,而不仅仅是密码不相同
            return HttpResponse("请再次检查输入密码是否符合标准。")
    elif request.method == "GET":
        user_register_form = UserRegisterForm()
        context = {'form': user_register_form}
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse('请使用GET或者POST请求数据！')


# 退出登录
def user_logout(request):
    logout(request)
    return redirect("article:list")


# 登录
def user_login(request):
    if request.method == "POST":
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确去陪数据库中的某个用户
            # 如果均匹配则返回一个user对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存到session中，实现登录操作
                login(request, user)
                return redirect("article:list")
            else:
                return HttpResponse("账户或密码输入错误，请重新输入！")
        else:
            return HttpResponse("账户或密码输入不合法")
    elif request.method == "GET":
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, "userprofile/login.html", context)
    else:
        return HttpResponse('请使用GET或POST请求数据！')
