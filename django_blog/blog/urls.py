from django.urls import path
from .views import PostSearchView

urlpatterns = [
    # other URLs...
    path('search/', PostSearchView.as_view(), name='post-search'),
]
