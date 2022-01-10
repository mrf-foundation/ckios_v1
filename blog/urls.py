from . import views
from django.urls import path
from apps.user import views as user_views
from django.views.generic import ListView, DetailView
from django.urls import path
from .views import HomeView, PostView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('post/', HomeView.as_view(), name='index'),
    path('<slug:slug>/', PostView.as_view(),  name='post_list'),
    #path('PostView/', PostView.as_view(),  name='post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]