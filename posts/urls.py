from . import views
from django.urls import path 

urlpatterns = [
    path('post/', views.index,name='index'),
    path('post/<str:pk>', views.post, name='post')
]