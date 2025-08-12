from django.urls import path
from .views import *
# from .views import HomeNews, CreateNews, ViewNews, NewsByCategory, UpdateNews

urlpatterns = [
    path('', info, name='home'),  # ✅ 'home' nomi berildi
    path('category/<int:pk>/', category, name='category'),
    path('add_news/', add_news, name='add_news'),
    path('update_new/<int:pk>/',update_new,name = 'update_new'),
    path('detail_new/<int:pk>/',detail_new,name = 'detail_new'),
    path('del_new/<int:pk>/',del_new,name = 'del_new'),
    # path('',HomeNews.as_view(),name = 'home'),
    # path('add_news',CreateNews.as_view(),name = 'add_+news'),
    # path('update_new/<int:pk>/',UpdateNews.as_view(), name = 'update_new'),
    # path('detail_new/<int:pk>/',ViewNews.as_view(),name = 'detail_new'),
    # path('category/<int:pk>/', NewsByCategory.as_view(), name='category'),
]
