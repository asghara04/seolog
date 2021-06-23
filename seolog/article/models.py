from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
	title = models.CharField(
		max_length=250,
		verbose_name="title"
	)
	slug = models.SlugField(
		max_length=250,
		verbose_name="slug",
		unique=True
	)
	image = models.ImageField(
		upload_to="Article Images/%Y/%m",
		verbose_name="image"
	)
	description = models.TextField(
		max_length=400,
		verbose_name="description"
	)

	body = models.TextField(
		max_length=10000,
		verbose_name="body"
	)

	author = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		verbose_name="author"
	)

	pubdate = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

	objects = models.Manager()

	def __str__(self):
		return self.title

	class Meta:
		ordering = ("-id",)