from django.urls import path
from .views import (ArticlesView, ArticleView)

urlpatterns = [
	path("", ArticlesView.as_view()),
	path("<slug:slug>/", ArticleView.as_view())
]