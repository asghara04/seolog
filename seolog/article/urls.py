from django.urls import path
from .views import ArticlesView

urlpatterns = [
	path("all/", ArticlesView.as_view()),
]