from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('', views.login_index, name='login_index'),
    path('login/create', views.login_index, name='create_account'),
    path('logout', views.logout_account, name='logout_account'),
]