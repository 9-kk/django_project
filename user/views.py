from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from user.models import UserData


# Create your views here.


class TestView(View):

    def get(self, request):
        # 查询所有业务信息
        userList_obj = UserData.objects.all()
        print(userList_obj, type(userList_obj))
        # 转成字典
        userList_dict = userList_obj.values()
        print(userList_dict, type(userList_dict))
        # 外层的容器转存list
        userList = list(userList_dict)
        print(userList, type(userList))
        return JsonResponse({'code': 200, 'info': '测试', 'data': userList})


# @csrf_exempt
class RegisterView(View):

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserData()
        user.username = username
        user.password = password
        user.save()
    # return render(request, '../templates/accounts/register.html')


class LoginView(View):

    @csrf_exempt
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = UserData.objects.get(username=username, password=password)
        if password == user.password:
            return HttpResponse('登录成功')
        else:
            return HttpResponse('登录失败')
    # return render(request, '../templates/accounts/login.html')

