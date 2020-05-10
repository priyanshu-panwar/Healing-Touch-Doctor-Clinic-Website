from django.urls import path
from . import views
import re

app_name = 'blog'
urlpatterns = [
    #path('<int:year>/<str:month>/', ArticleMonthArchiveView.as_view(), name="archive_month"),
    path('test/', views.test, name='test'),
	path('', views.home, name='home'),
    #path('', PostListView.as_view(), name='home'),
    #path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #path('post/new/', views.post_create, name='post-create'),
    #path('post/new/', PostCreateView.as_view(), name='post-create'),
    #path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    #path('post/<int:pk>/delete/', views.post_delete, name='post-delete'),
    #path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]