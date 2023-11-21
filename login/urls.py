# from django.urls import path
# from . import views
#
# urlpatterns = [
#     # path('', views.)
#     path('home/', views.home, name='home'),
#     path('home/login', views.login, name='login'),
#     path('home/logout', views.logout, name='logout'),
# ]

from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/login/', views.login, name='login'),  # 수정: / 추가
    path('home/logout/', views.logout, name='logout'),  # 수정: / 추가
]
