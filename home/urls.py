

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('resultpage/', views.result_page, name='resultpage'),
    path('details/<int:pk>/', views.details, name='details'),
]
