from django.urls import path
from .views import article_list, article_detail

urlpatterns = [
   # path('', views.home, name="home"),
   # path('room/', views.room, name="room"),
    path('article/', article_list),
    path('detail/<int:pk>/', article_detail),
]