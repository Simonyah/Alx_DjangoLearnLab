from django.urls import path
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import PostSearchView

urlpatterns += [
    path('search/', PostSearchView.as_view(), name='post-search'),
    path('tags/<str:tag_name>/', views.PostsByTagView.as_view(), name='posts-by-tag'),
]

urlpatterns = [
    # existing urls for posts...
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
