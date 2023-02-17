from django.urls import path
from .import views
from .views import PostList


urlpatterns = [
    path('',PostList.as_view(), name='blog'),
    path('<str:slug>/', views.post_detail, name='post_detail'),
    path('delete_comment/<int:comment_id>/', views.delete_comment,
         name='delete_comment'),
    
  
]