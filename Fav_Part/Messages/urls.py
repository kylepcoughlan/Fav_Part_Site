from django.urls import path
from . import views
from .views import toggle_like

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('like/<int:post_id>/', toggle_like, name='toggle_like'),
    path('<int:post_id>/',views.get_post_data, name='get_post_data'),
]
