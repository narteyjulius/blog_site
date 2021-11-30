from django.urls import path
from . import views
# from .views import profile, edit_profile

app_name = 'users'

urlpatterns = [
    # path('<str:id>/', views.profile, name='my_profile'),
    path('', views.profile, name='my_profile'),
    path('edit-profile/<str:id>/', views.update_profile, name='edit_profile'),


    # path('users/<int:id>/', views.profile, name='my_profile'),
    # path('<int:pk>/', views.profile, name='my_profile'),

    # path('uers/<str:pk>/', views.profile, name='my_profile'),


    # path('edit-profile/', views.edit_profile, name='edit_profile'),
    
]