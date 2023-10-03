from django.urls import path, re_path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    # path('data/', views.display_restaurants),
    re_path(r'^$', views.HomePageView.as_view(), name='home'),
    re_path(r'^about$', views.AboutPageView.as_view(), name='about'),
    re_path(r'^data$', views.DataPageView.as_view(), name='data'),
    re_path(r'^search$', views.search),
    re_path(r'^like$', views.like),
    re_path(r'dislike$', views.dislike),
]