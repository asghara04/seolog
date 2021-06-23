from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
	author = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field="username"
	)

	class Meta:
		model = Article
		fields = ["id", "title", "slug", "image", "description", "body", "author", "pubdate", "update"]