from . import views
from django.urls import path 

urlpatterns = [
    path('signup', views.signup_view,name='signup_view'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')


]