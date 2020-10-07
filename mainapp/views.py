from django.shortcuts import render, redirect
from django.contrib import auth
# Create your views here.
def index(request):
    if(request.user.username == "admin"):
        auth.logout(request)
        print("관리자계정이면 로그아웃")
        return redirect('/')
    return render(request, 'index.html')