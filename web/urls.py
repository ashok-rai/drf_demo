from django.urls import path
from web.views import PostListAPIView

urlpatterns = [
	path('', PostListAPIView.as_view(), name='post_list'),
]
