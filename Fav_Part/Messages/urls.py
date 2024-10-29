from django.urls import path
from . import views
from .views import like_post

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('like/<int:post_id>/', like_post, name='like_post'),
]
