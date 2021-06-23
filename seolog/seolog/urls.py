from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
	path("api/articles/", include("article.urls")),
    path('admin/', admin.site.urls),
]
