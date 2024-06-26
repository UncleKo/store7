from django.urls import path

from .models import BlogDetailPage
from .views import category_posts, TagPostListView, archives, add_comment, update_comment, delete_comment, comment_approve


app_name = 'blog'


urlpatterns = [
  path('category/<str:cat_slug>/', category_posts, name='category-view'),
  path('tag/<str:tag_slug>/', TagPostListView.as_view(), name='tag-view'),
  path('archives/', archives, name='post-archives'),

  path('post/<int:post_id>/comment/create', add_comment, name='comment-create'),
  path('comment/<int:comment_id>/update/', update_comment, name='comment-update'),
  path('comment/<int:comment_id>/delete/', delete_comment, name='comment-delete'),
  path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
]