from django.db import models

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

	publish_date = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

	objects = models.Manager()

	def __str__(self):
		return self.title