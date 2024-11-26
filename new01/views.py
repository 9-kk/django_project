from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Post
# Create your views here.


def register_page(request):
    # 用户创建表单并传递
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "accounts/register.html", context)


def login_page(request):
    return render(request, "accounts/login.html")


def show_name(request):
    context = {'name_list': Post.objects.all()}
    return render(request, 'web01.html', context=context)
