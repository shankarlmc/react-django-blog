from django.urls import path
from .views import (
    PostList,
    PostDetail,
    UserList,
    UserDetail,
)

urlpatterns = [
    path('posts/<int:pk>', PostDetail.as_view()),
    path('posts/', PostList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('user/', UserList.as_view()),
]
