from django.urls import path
from . import views as v

urlpatterns = [
    path('' , v.home , name = "home"),
    path('login_user/' , v.login_user , name = "login_user"),
    path('logout_user/' , v.logout_user , name = "logout_user"),
    path('signup_user/' , v.signup_user , name = "signup_user")
]