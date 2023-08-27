from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view()),
]