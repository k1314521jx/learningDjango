from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.margnet import *

def login(request):
    # 包含用户提交的所有信息
    # 获取用户提交方法
    # print(request.method)
    error_msg = ""
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'root' and pwd == "123":
            # 去跳转到
            return redirect('/login')
        else:
            # 用户密码不配
            error_msg = "用户名或密码错误"
    return render(request,'login.html', {'error_msg': error_msg})

USER_LIST = [
    {'id': 1, 'username': 'alex', 'email': 'asdfasdf', "gender": '男'},
    {'id': 2, 'username': 'eriuc', 'email': 'asdfasdf', "gender": '男'},
    {"id": 3,'username': 'seven', 'email': 'asdfasdf', "gender": '男'},
]


def home(request):
    # print(request.GET.get('nid'))

    USER_LIST = []

    if request.method == "POST":
        # 获取用户提交的数据 POST请求中
        u = request.POST.get('username')
        # for movie in get_magnet(u):
        USER_LIST = get_magnet(u)
            # USER_LIST.append(movie)
    return render(request, 'test/home.html', {'user_list': USER_LIST})


# def login(request):
#     # string = """
#     # <form>
#     #     <input type='text' />
#     # </form>
#     #
#     # """
#     # f = open('templates/login.html', 'r', encoding='utf-8')
#     # data = f.read()
#     # f.close()
#     # return HttpResponse(data)
#     return render(request,'login.html')

# def home(request):
#     return HttpResponse('<h1>CMDB</h1>')

# 主机管理
# 防火墙
# 。。。