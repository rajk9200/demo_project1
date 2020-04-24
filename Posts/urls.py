

from django.urls import path
from . import views
urlpatterns = [
    path('addPost/', views.add_post, name='addpost'),

]
