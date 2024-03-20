from django.urls import path
from . import views

urlpatterns = [
    path('main-page/', views.open_main_page, name='main-page'),
    path('add-page/', views.add_task, name='add-page'),
    path('settings/', views.show_settings, name='settings'),
]
