from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView, View, TemplateView
from django.contrib.auth.models import User


class LoginIndexView(TemplateView):
	template_name = 'account/index.html'

login_index = LoginIndexView.as_view()


def logout_account(request):
    logout(request)
    print(request,"Logged out,please come back again.")
    return redirect('account:login_index')